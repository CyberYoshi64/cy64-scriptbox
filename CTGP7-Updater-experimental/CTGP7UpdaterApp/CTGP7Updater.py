import os
import urllib3
import shutil
import psutil
import struct
from typing import List

urlmgr = urllib3.PoolManager(headers={"Connection":"Keep-Alive"})
def urlopen(url:str, **kwarg):
    out = urlmgr.request("GET", url, chunked=True, preload_content=False, **kwarg)
    if out.status != 200: raise Exception("Failed opening URL '{}': Received staus code {}".format(url, out.status))
    return out

class CTGP7Updater:

    VERSION_NUMBER = "1.1.2-dev"

    _BASE_URL_DYN_LINK = "https://ctgp7.page.link/baseCDNURL"
    _INSTALLER_VERSION = "installerver"
    _INSTALLER_FILE_DIFF = "installinfo.txt"
    _UPDATER_CHGLOG_FILE = "changeloglist"
    _UPDATER_FILE_URL = "fileListPrefix.txt"
    _FILES_LOCATION = "data"
    _FILES_LOCATION_CITRA = "dataCitra"
    _LATEST_VER_LOCATION = "latestver"
    _DL_ATTEMPT_TOTALCNT = 30
    _VERSION_FILE_PATH = ["config", "version.bin"]
    _PENDINGUPDATE_PATH = ["config", "pendingUpdate.bin"]
    _ISCITRAFLAG_PATH = ["config", "citra.flag"]
    _REINSTALLFLAG_PATH = ["config", "forceInstall.flag"]
    _PATCHFLAG_PATH = ["config", "forcePatch.flag"]
    _SLACK_FREE_SPACE = 20000000

    _MODE_INSTALL, _MODE_UPDATE, _MODE_INTCHECK = range(3)

    class FileListEntry:

        def __init__(self, ver: int, method, path: str, url: str) -> None:
            self.filePath = path
            self.forVersion = ver # Unused
            self.fileMethod = method
            self.havePerformed = False
            self.isStoppedCallback = None
            self.fileProgressCallback = None
            self.url = url
            self.fileOnlyName = self.filePath[self.filePath.rfind(os.path.sep) + 1:]
            self.remoteName = self.filePath[self.filePath.rfind(os.path.sep+"CTGP-7"+os.path.sep) + 7:].replace("\\","/")

        def __eq__(self, __o: object) -> bool:
            return isinstance(__o, CTGP7Updater.FileListEntry) and \
                self.filePath == __o.filePath and \
                self.url == __o.url and \
                self.fileMethod == __o.fileMethod and \
                self.forVersion == __o.forVersion
            
        def __str__(self) -> str:
            return "ver: \"{}\" method: \"{}\" path: \"{}\" url: \"{}\"".format(self.forVersion, self.fileMethod, self.filePath, self.url)
        
        def __repr__(self) -> str:
            return self.__str__()
        
        def setCallbacks(self, isStopped, progress):
            self.isStoppedCallback = isStopped
            self.fileProgressCallback = progress

        # Export struct for pendingUpdate.bin
        def exportToPend(self) -> bytes:
            return struct.pack("<BI", \
                ord(self.fileMethod),\
                self.forVersion) + \
                self.remoteName.encode("utf8") + b'\0'
        
        def _downloadFile(self):
            _DOWN_PART_EXT = ".part" # Better safe than sorry
            countRetry = 0
            userCancel = False
            oldPos = -1
            while (True):
                try:
                    CTGP7Updater.mkFoldersForFile(self.filePath)
                    if self.url.find("dummy.txt")>=0: return
                    u = urlopen(self.url, timeout=10)
                    with open(self.filePath + _DOWN_PART_EXT, 'wb') as downFile:

                        fileDownSize = int(u.headers.get("Content-Length", 1))
                        progDiv = max(1, fileDownSize // 10)

                        fileDownCurr = 0; block_sz = 32768
                        while True:
                            if userCancel or (self.isStoppedCallback is not None and self.isStoppedCallback()):
                                userCancel = True
                                raise Exception("User cancelled installation")
                            buffer = u.read(block_sz)
                            if not buffer:
                                break

                            fileDownCurr += len(buffer)
                            downFile.write(buffer)

                            if (self.fileProgressCallback is not None and (fileDownCurr//progDiv)!=oldPos):
                                self.fileProgressCallback(fileDownCurr, fileDownSize, self.fileOnlyName)
                                oldPos = fileDownCurr//progDiv
                    CTGP7Updater.fileMove(self.filePath+_DOWN_PART_EXT, self.filePath)
                    break
                except KeyboardInterrupt:
                    userCancel = True # Terminal uses Ctrl+C to signal cancelling
                except Exception as e:
                    if (countRetry >= CTGP7Updater._DL_ATTEMPT_TOTALCNT or userCancel):
                        CTGP7Updater.fileDelete(self.filePath+_DOWN_PART_EXT)
                        raise Exception("Failed to download file \"{}\": {}".format(self.fileOnlyName, e))
                    else:
                        countRetry += 1

        def perform(self, lastPerformValue:str):
            if self.fileMethod == "M" or self.fileMethod == "C": # Modify
                self._downloadFile()
                return None
            elif self.fileMethod == "D": # Delete
                CTGP7Updater.fileDelete(self.filePath)
                return None
            elif self.fileMethod == "F": # (Rename) From
                return self.filePath
            elif self.fileMethod == "T": # (Rename) To
                if (lastPerformValue is not None):
                    CTGP7Updater.fileMove(lastPerformValue, self.filePath)
                else:
                    raise Exception("Rename to statement for \"{}\" is missing rename from statement".format(self.fileOnlyName))
                return None
            elif self.fileMethod == "I": # Ignore file
                return lastPerformValue
            else:
                raise Exception("Unknown file mode: {}".format(self.fileMethod))

    def __init__(self, opMode=_MODE_INSTALL, isCitra=False) -> None:
        self.operationMode = opMode
        self.basePath = ""
        self.downloadCount = 0
        self.currDownloadCount = 0
        self.fileDownCurr = 0
        self.fileDownSize = 0
        self.fileList:List[CTGP7Updater.FileListEntry] = [] 
        self.latestVersion = ""
        self.logFunction = None
        self.isStopped = False
        self.downloadSize = 0
        self.currentUpdateIndex = 0
        self.isCitra = isCitra
    
    @staticmethod
    def isDev() -> bool:
        return CTGP7Updater.VERSION_NUMBER.find("dev")>=0

    @staticmethod
    def getCitraDir() -> str:
        if os.name == "nt": return "%s\\Citra\\sdmc"%os.environ['APPDATA']
        if os.name == "posix": return "%s/.local/share/citra-emu/sdmc"%os.environ['HOME']
        return "./sdmc"
    
    @staticmethod
    def fileDelete(file:str) -> None:
        try: os.stat(file)    # Windows refuses to rename
        except: pass          # if destination exists, so
        else: os.remove(file) # delete beforehand.

    @staticmethod
    def fileMove(oldf:str, newf:str) -> None:
        CTGP7Updater.fileDelete(newf)
        os.rename(oldf,newf)

    @staticmethod
    def getDefaultCdnUrlAsString():
        return CTGP7Updater._downloadString(CTGP7Updater._BASE_URL_DYN_LINK).strip()

    def fetchDefaultCDNURL(self):
        try:
            self.baseURL = self._downloadString(CTGP7Updater._BASE_URL_DYN_LINK).replace("\r", "").replace("\n", "")
        except Exception as e:
            raise Exception("Failed to init updater: {}".format(e))
        pass
    
    @staticmethod
    def mkFoldersForFile(fol:str):
        g=fol[0:fol.rfind(os.path.sep)]
        os.makedirs(g, exist_ok=True)
    
    def _buildFilePath(self, path: str):
        return os.path.join(os.path.join(self.basePath, "CTGP-7"), path.replace("/", os.path.sep)[1:])
    
    def _buildFileURL(self, path: str, isCitra: bool):
        return self.baseURL + (CTGP7Updater._FILES_LOCATION_CITRA if isCitra else CTGP7Updater._FILES_LOCATION) + path

    def _parseAndSortDlList(self, dll:list):
        allFilePaths=[]; allFileModes=[]; ret=[]; oldf=""
        self.downloadCount = 0

        for i in range(len(dll)):
            mode=dll[i][0]; path=dll[i][1]

            if mode=="S":
                try:
                    self.downloadSize = int(path[1:])
                except Exception as e:
                    raise Exception("Failed to parse needed download size: {}".format(e))
            else:
                filePathIndex = 0
                if (mode == "C" and not self.isCitra):
                    dll[i] = ("I", dll[i][1])
                    mode = "I"
                if (mode == "C" or mode == "M" or mode == "D"):
                    while (filePathIndex < len(allFilePaths)):
                        if (path == allFilePaths[filePathIndex] and (allFileModes[filePathIndex] == "M" or allFileModes[filePathIndex] == "D" or (mode == "C" and allFileModes[filePathIndex] == "C"))):
                            allFileModes[filePathIndex] = "I"
                        filePathIndex += 1
                allFilePaths.append(path); allFileModes.append(mode)
        
        for i in range(len(allFilePaths)):
            if allFileModes[i]=="M" or allFileModes[i]=="C": self.downloadCount+=1
            ret.append(CTGP7Updater.FileListEntry(self.currentUpdateIndex, allFileModes[i], self._buildFilePath(allFilePaths[i]), self._buildFileURL(allFilePaths[i], allFileModes[i] == "C")))

        return ret

    def _checkNeededExtraSpace(self, diskSpace):
        return 0 if not self.downloadSize else max(0, self.downloadSize + CTGP7Updater._SLACK_FREE_SPACE - diskSpace)

    @staticmethod
    def _downloadString(url: str) -> str:
        try:
            output = urlopen(url, timeout=10).read()
            return output.decode('utf-8')
        except Exception as e:
            raise Exception("Failed download string from URL '{}': {}".format(url, e))

    def stop(self):
        self.isStopped = True
    
    def _isStoppedCallback(self):
        return self.isStopped

    def _logFileProgressCallback(self, fileDownCurr, fileDownSize, fileOnlyName):
        self._log("File {}/{}: '{}' ({:.1f}%){}".format(self.currDownloadCount, self.downloadCount, fileOnlyName, (fileDownCurr / fileDownSize) * 100, "\r"*(fileDownCurr<fileDownSize)))
    
    def setBaseURL(self, url):
        self.baseURL = url

    def setLogFunction(self, func):
        self.logFunction = func

    def _log(self, msg: str):
        if (self.logFunction):
            self.logFunction({"m":msg})

    def _prog(self, curr: float, tot: float):
        if (self.logFunction):
            self.logFunction({"p":(curr, tot)})

    @staticmethod
    def _isValidNintendo3DSSDCard(path:str):
        return os.path.exists(os.path.join(path, "Nintendo 3DS"))

    @staticmethod
    def doesInstallExist(path):
        return os.path.exists(os.path.join(path, "CTGP-7"))

    @staticmethod
    def isVersionValid(path):
        file = os.path.join(path, "CTGP-7", *CTGP7Updater._VERSION_FILE_PATH)
        if not os.path.exists(file):
            return False
        size = os.stat(file).st_size
        return (size>=3 and size<=8)

    @staticmethod
    def hasBrokenFlag(path):
        return os.path.exists(os.path.join(path, "CTGP-7", *CTGP7Updater._REINSTALLFLAG_PATH))

    @staticmethod
    def hasPendingInstall(path):
        return os.path.exists(os.path.join(path, "CTGP-7", *CTGP7Updater._PENDINGUPDATE_PATH))

    def setBaseDirectory(self, path: str):
        if not (os.path.exists(path)):
            raise Exception("Installation path invalid.")
        self.basePath = path

    def getLatestVersion(self):
        try:
            self.latestVersion = self._downloadString(self.baseURL + CTGP7Updater._LATEST_VER_LOCATION).replace("\n", "").replace("\r", "")
        except Exception as e:
            raise Exception("Failed to get latest version: {}".format(e))

    def makeReinstallFlag(self):
        try:
            p = os.path.join(self.basePath, "CTGP-7", *self._REINSTALLFLAG_PATH)
            CTGP7Updater.mkFoldersForFile(p)
            with open(p, 'wb') as f:
                f.write(b"Oopsies... you gotta reinstall, bro.")
        except:
            pass

    # Using this to simplify reading from pendingUpdate.bin
    # fb is a BufferedReader
    @staticmethod
    def _readUntilNulByte(fb) -> bytes:
        if not hasattr(fb,"read"): return b""
        out:bytes = b''
        while True:
            char = fb.read(1)
            if char == b'\0' or char == b'': break
            out += char
        return out

    def loadUpdateInfo(self):
        fileModeList = []
        
        if (self.operationMode == self._MODE_INSTALL):
            # Installation (read full list)
            self._log("Downloading file list...")
            try:
                fileList = self._downloadString(self.baseURL + CTGP7Updater._INSTALLER_FILE_DIFF).split("\n")
                for file in fileList:
                    if file=="": continue
                    fileModeList.append((file[0],file[1:].strip()))
                self.fileList = self._parseAndSortDlList(fileModeList)

            except Exception as e:
                raise Exception("Failed to get list of files: {}".format(e))
        elif (self.operationMode == self._MODE_UPDATE):
            # Update
            self._log("Preparing update...")
            pendUpdName = os.path.join(self.basePath, "CTGP-7", *self._PENDINGUPDATE_PATH)
            
            # If a pending update present, use it
            if os.path.exists(pendUpdName):
                
                try:
                    entriesLeft:int = 0
                    with open(pendUpdName,"rb") as puf:
                        entriesLeft = int.from_bytes(puf.read(4), "little")
                        self.latestVersion = CTGP7Updater._readUntilNulByte(puf).decode("utf")
                        for i in range(entriesLeft):
                            fileMethod = str(puf.read(1),"ascii")
                            int.from_bytes(puf.read(4),"little") # Somehow used; I don't care about it
                            fileName = CTGP7Updater._readUntilNulByte(puf).decode("utf-8")
                            fileModeList.append((fileMethod, fileName))
                    self.fileList = self._parseAndSortDlList(fileModeList)
                except Exception as e:
                    self.makeReinstallFlag()
                    raise Exception("An issue occured while parsing the pending update: {}".format(e))
            else:
                # Read current version and load file lists up to latest version
                try:
                    configPath = os.path.join(self.basePath, "CTGP-7", *CTGP7Updater._VERSION_FILE_PATH)
                    with open(configPath, "rb") as vf:
                        localVersion = vf.read().decode("utf-8")
                except Exception as e:
                    self.makeReinstallFlag()
                    raise Exception("Could not read the version file: {}".format(e))

                fileListURL = self._downloadString(self.baseURL + CTGP7Updater._UPDATER_FILE_URL).replace("\n", "").replace("\r", "")
                changelogData = self._downloadString(self.baseURL + CTGP7Updater._UPDATER_CHGLOG_FILE).split(";")
                for index in range(len(changelogData)):
                    changelogData[index] = changelogData[index].split(":")[0]

                while True:
                    try:    changelogData.remove("")
                    except: break

                try:
                    chglogIdx = changelogData.index(localVersion)
                except:
                    self.makeReinstallFlag()
                    raise Exception("Current version not known. The version file might be corrupted or has been modified or an update has been revoked.")
                if chglogIdx == len(changelogData)-1:
                    raise Exception("There are no updates available. If this is not correct, please try again later.")

                progTotal = len(changelogData) - chglogIdx
                for index in range(chglogIdx + 1, len(changelogData)):
                    try:
                        self._log("Obtaining update info for v{}...\r".format(changelogData[index]))
                        self._prog(index - chglogIdx, progTotal-1)
                        fileList = self._downloadString(fileListURL % changelogData[index]).split("\n")
                        for file in fileList:
                            if file=="": continue
                            fileModeList.append((file[0],file[1:].strip()))
                        self.fileList = self._parseAndSortDlList(fileModeList)

                    except Exception as e:
                        raise Exception("Failed to get list of files: {}".format(e))
        if (self.operationMode == self._MODE_INTCHECK):
            try:
                patchFlag = os.path.join(self.basePath, "CTGP-7", *self._PATCHFLAG_PATH)
                self.fileDelete(patchFlag)
                with open(patchFlag,"wb") as f:
                    f.write(b"lol")
            except Exception as e:
                raise Exception("Unable to be create patch flag: {}".format(e))

            try:
                configPath = os.path.join(self.basePath, "CTGP-7", *self._VERSION_FILE_PATH)
                with open(configPath, "rb") as vf:
                    localVersion = vf.read().decode("utf-8")
            except Exception as e:
                self.makeReinstallFlag()
                raise Exception("Could not read the version file: {}".format(e))

            if localVersion != self.latestVersion:
                raise Exception("Cannot continue: This installation is not up-to-date. Please update this installation before performing an integrity check.")

            self._log("Preparing integrity check...")
            try:
                fileList = self._downloadString(self.baseURL + self._INSTALLER_FILE_DIFF).split("\n")
                for file in fileList:
                    if file=="": continue
                    if file[0]!="S":
                        fileName = file[1:].strip()
                        if fileName.find("tooInstall")<0 and fileName[-5:]!=".flag" and not os.path.exists(
                            os.path.join(self.basePath, "CTGP-7"+fileName.replace("/",os.sep))
                        ):
                            fileModeList.append((file[0],fileName))
                if not len(fileModeList):
                    raise Exception("No files are missing. There's nothing to do.")
                self.fileList = self._parseAndSortDlList(fileModeList)
            except Exception as e:
                raise Exception("Couldn't prepare integrity check: {}".format(e))

    def verifySpaceAvailable(self):
        available_space = psutil.disk_usage(self.basePath).free
        neededSpace = self._checkNeededExtraSpace(available_space)
        if (neededSpace > 0):
            raise Exception("Not enough free space on destination folder. Additional {} MB needed to proceed with installation.".format(neededSpace // 1000000))
    
    @staticmethod
    def findNintendo3DSRoot():
        try:
            mount_points = psutil.disk_partitions()
            candidates = []
            for m in mount_points:
                try:
                    if (CTGP7Updater._isValidNintendo3DSSDCard(m.mountpoint)):
                        candidates.append(m.mountpoint)
                except:
                    pass
        except:
            pass
        return candidates

    @staticmethod
    def checkProgramVersion():
        baseURL = CTGP7Updater.getDefaultCdnUrlAsString()
        ver = CTGP7Updater._downloadString(baseURL + CTGP7Updater._INSTALLER_VERSION).strip()
        return ver != CTGP7Updater.VERSION_NUMBER.split("-")[0]

    def makePendingUpdate(self):
        header:bytes = self.latestVersion.encode("ascii") + b'\0'
        flist:bytes = b''; pendingCount:int = 0
        for entry in self.fileList:
            if not entry.havePerformed:
                flist += entry.exportToPend()
                pendingCount += 1
        header = int.to_bytes(pendingCount, 4, "little") + header

        fileName = os.path.join(self.basePath, "CTGP-7", *self._PENDINGUPDATE_PATH)
        self.mkFoldersForFile(fileName)
        self.fileDelete(fileName)
        with open(fileName,"wb") as puf:
            puf.write(header + flist)

    def startUpdate(self):
        mainfolder = os.path.join(self.basePath, "CTGP-7")
        hbrwfolder = os.path.join(self.basePath, "3ds")

        try:
            os.makedirs(mainfolder, exist_ok=True)
            os.makedirs(hbrwfolder, exist_ok=True)
        except Exception as e:
            raise Exception("Failed to create directories: {}".format(e))

        if self.isCitra:
            configPath = os.path.join(self.basePath, "CTGP-7", *self._ISCITRAFLAG_PATH)
            self.mkFoldersForFile(configPath)
            with open(configPath, "wb") as vf:
                vf.write(b'It\'s really a lemon, no?')
        prevReturnValue = None
        self.currDownloadCount = 0
        for entry in self.fileList:
            entry.setCallbacks(self._isStoppedCallback, self._logFileProgressCallback)
            if (entry.fileMethod == "M" or entry.fileMethod == "C"):
                self._prog(self.currDownloadCount, self.downloadCount)
                self.currDownloadCount += 1

            try:
                prevReturnValue = entry.perform(prevReturnValue)
                entry.havePerformed = True
            except (Exception, KeyboardInterrupt) as e:
                self._log("Aborting installation...")
                if (self.operationMode == self._MODE_UPDATE):
                    self._log("Marking update as pending...")
                    self.makePendingUpdate()
                if type(e)==KeyboardInterrupt: raise Exception("User cancelled installation") # Terminal
                raise Exception(e)

        if self.downloadCount:
            self._prog(self.currDownloadCount, self.downloadCount)
        
        ciaFile = os.path.join(mainfolder, "cia", "CTGP-7.cia")
        hbrwFile = os.path.join(mainfolder, "cia", "CTGP-7.3dsx")
        hbrwFileFinal = os.path.join(hbrwfolder, "CTGP-7.3dsx")
        tooInstallCiaFile = os.path.join(mainfolder, "cia", "tooInstall.cia")
        tooInstallHbrwFile = os.path.join(mainfolder, "cia", "tooInstall.3dsx")
        
        self._log("Finishing up...")

        try:
            configPath = os.path.join(mainfolder, *CTGP7Updater._VERSION_FILE_PATH)
            self.mkFoldersForFile(configPath)
            with open(configPath, "wb") as vf:
                vf.write(self.latestVersion.encode("ascii"))
        except Exception as e:
            self.makeReinstallFlag()
            raise Exception("Failed to write version info: {}".format(e))
        
        try:
            self.fileDelete(os.path.join(self.basePath, "CTGP-7", *self._PENDINGUPDATE_PATH))
            if os.path.exists(tooInstallHbrwFile):
                self.fileMove(tooInstallHbrwFile,hbrwFile)
                shutil.copyfile(hbrwFile, hbrwFileFinal)
            if os.path.exists(tooInstallCiaFile):
                self.fileMove(tooInstallCiaFile,ciaFile)
        except Exception as e:
            raise Exception("Failed to finish cleanup: {}".format(e))

        self._log("")

    def cleanInstallFolder(self):
        if (self.operationMode != self._MODE_INSTALL): return
        mainfolder = os.path.join(self.basePath, "CTGP-7")
        if (os.path.exists(mainfolder)):
            self._log("Removing previous installation...")
            shutil.rmtree(mainfolder)

    """
    Check, if the SD specified is for Citra.

    Return values:
        True  - Path is Citra SD
        False - Path is not Citra (3DS)
        None  - Uncertain, ask in front-end

        FIXME: Can only detect locally installed on main
               drive; fails if Citra is installed externally.

        TODO: Figure out how to read Citra config
    """
    @staticmethod
    def isCitraDirectory(path:str):
        if os.name == "nt":
            citraPath = os.path.join(os.environ["APPDATA"],"Citra","sdmc")
        else:
            citraPath = os.path.join(os.environ["HOME"],".local","share","citra-emu","sdmc")
        
        try:
            if os.path.samefile(path, citraPath): # Linux is case-sensitive, Windows may use inconsistent casing, ruining simple checks
                                                  # Added bonus: symlinks would work this way too.
                return True
            else:
                if os.path.exists(os.path.join(path, "boot.firm")):
                    return False
                if os.path.exists(os.path.join(path, *CTGP7Updater._ISCITRAFLAG_PATH)):
                    return True
            return None
        except:
            return None
