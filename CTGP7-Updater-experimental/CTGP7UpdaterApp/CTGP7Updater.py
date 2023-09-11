import os, sys, hashlib
import shutil, psutil
import urllib3, struct
from typing import List
from CTGP7UpdaterApp.constants import CONSTANT as const
import CTGP7UpdaterApp.utils as utils
import CTGP7UpdaterApp.lang as lang

urlmgr = urllib3.PoolManager(headers={"Connection":"Keep-Alive"})
def urlopen(url:str, **kwarg):
    out = urlmgr.request("GET", url, chunked=True, preload_content=False, **kwarg)
    if out.status != 200: raise Exception(utils.strfmt(lang.get("failOpenURL"), url, out.status))
    return out

class CTGP7Updater:
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
            self.remoteName = self.filePath[self.filePath.rfind(os.path.sep+const._BASE_MOD_FOLDER_PATH+os.path.sep) + 7:].replace("\\","/")

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
                    u = urlopen(self.url, timeout=10)
                    with open(self.filePath + _DOWN_PART_EXT, 'wb') as downFile:

                        fileDownSize = int(u.headers.get("Content-Length", 1))
                        progDiv = max(1, fileDownSize // 10)

                        fileDownCurr = 0; block_sz = 32768
                        while True:
                            if userCancel or (self.isStoppedCallback is not None and self.isStoppedCallback()):
                                userCancel = True
                                raise Exception(lang.get("userCancel"))
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
                    if (countRetry >= const._DL_ATTEMPT_TOTALCNT or userCancel):
                        CTGP7Updater.fileDelete(self.filePath+_DOWN_PART_EXT)
                        raise Exception(utils.strfmt(lang.get("failDownloadFile"), self.fileOnlyName, e))
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
                    raise Exception(utils.strfmt(lang.get("failRenameToNoFrom"), self.fileOnlyName))
                return None
            elif self.fileMethod == "I": # Ignore file
                return lastPerformValue
            else:
                raise Exception(utils.strfmt(lang.get("failUnknownMode"), self.fileOnlyName, self.fileMethod))

    def __init__(self, opMode=const._MODE_INSTALL, isCitra=False) -> None:
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
        return const.VERSION_NUMBER["category"] == const.VERSION_CAT_DEV
    
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
        return CTGP7Updater._downloadString(const._BASE_URL_DYN_LINK).strip()

    def fetchDefaultCDNURL(self):
        try:
            self.baseURL = self._downloadString(const._BASE_URL_DYN_LINK).replace("\r", "").replace("\n", "")
        except Exception as e:
            raise Exception(utils.strfmt(lang.get("failInit"), e))
        pass
    
    @staticmethod
    def mkFoldersForFile(fol:str):
        g=fol[0:fol.rfind(os.path.sep)]
        os.makedirs(g, exist_ok=True)
    
    def _buildFilePath(self, path: str):
        return os.path.join(os.path.join(self.basePath, const._BASE_MOD_FOLDER_PATH), path.replace("/", os.path.sep)[1:])
    
    def _buildFileURL(self, path: str, isCitra: bool):
        return self.baseURL + (const._FILES_LOCATION_CITRA if isCitra else const._FILES_LOCATION) + path

    def _parseAndSortDlList(self, dll:list):
        allFilePaths=[]; allFileModes=[]; ret=[]; oldf=""
        self.downloadCount = 0

        for i in range(len(dll)):
            mode=dll[i][0]; path=dll[i][1]

            if mode=="S":
                try:
                    self.downloadSize = int(path[1:])
                except Exception as e:
                    raise Exception(utils.strfmt(lang.get("failParseSizeParam"), e))
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
        return 0 if not self.downloadSize else max(0, self.downloadSize + const._SLACK_FREE_SPACE - diskSpace)

    @staticmethod
    def _downloadString(url: str, encoding="utf-8", errors="replace"):
        try:
            output = urlopen(url, timeout=10).read()
            if encoding!="raw":
                return output.decode(encoding, errors)
            else:
                return output
        except Exception as e:
            raise Exception(utils.strfmt(lang.get("failDownloadStr"), url, e))

    def stop(self):
        self.isStopped = True
    
    def _isStoppedCallback(self):
        return self.isStopped

    def _logCheckProgressCallback(self, fileIndex, fileCount, fileCurr, fileSize, fileOnlyName):
        self._logprog(utils.strfmt(
            lang.get("intCheckProg"),
            fileOnlyName,
            fileIndex, fileCount,
            int((fileCurr / fileSize) * 1000) / 10
        ) + "\r"*(fileCurr<fileSize),
        fileIndex, fileCount)

    def _logFileProgressCallback(self, fileDownCurr, fileDownSize, fileOnlyName):
        self._logprog(utils.strfmt(
            lang.get("installProg"),
            fileOnlyName,
            self.currDownloadCount, self.downloadCount,
            int((fileDownCurr / fileDownSize) * 1000) / 10
        ) + "\r"*(fileDownCurr<fileDownSize),
        self.currDownloadCount, self.downloadCount)

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

    def _logprog(self, msg: str, curr: float, tot: float):
        if (self.logFunction):
            self.logFunction({"m":msg, "p":(curr, tot)})

    def _info(self, msg: str, substr=None):
        if (self.logFunction):
            self.logFunction({"i":(msg, substr)})

    @staticmethod
    def _isValidNintendo3DSSDCard(path:str):
        return os.path.exists(os.path.join(path, "Nintendo 3DS"))

    @staticmethod
    def doesInstallExist(path):
        return os.path.exists(os.path.join(path, const._BASE_MOD_FOLDER_PATH))

    def setBaseDirectory(self, path: str):
        if not (os.path.exists(path)):
            raise Exception(lang.get("invalidInstallDir"))
        self.basePath = path

    def getLatestVersion(self):
        try:
            self.latestVersion = self._downloadString(self.baseURL + const._LATEST_VER_LOCATION).replace("\n", "").replace("\r", "")
        except Exception as e:
            raise Exception(utils.strfmt(lang.get("failGetUpdateInfo"), e))

    def makeReinstallFlag(self):
        try:
            p = os.path.join(self.basePath, const._BASE_MOD_FOLDER_PATH, *const._REINSTALLFLAG_PATH)
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
        
        if (self.operationMode == const._MODE_INSTALL):
            self._log(lang.get("prepareInstall"))
            try:
                fileList = self._downloadString(self.baseURL + const._INSTALLER_FILE_DIFF).split("\n")
                for file in fileList:
                    if file=="": continue
                    fileModeList.append((file[0],file[1:].strip()))
                self.fileList = self._parseAndSortDlList(fileModeList)

            except Exception as e:
                raise Exception(utils.strfmt(lang.get("failGetFileList"), e))
        elif (self.operationMode == const._MODE_UPDATE):
            self._log(lang.get("prepareUpdate"))
            pendUpdName = os.path.join(self.basePath, const._BASE_MOD_FOLDER_PATH, *const._PENDINGUPDATE_PATH)

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
                    raise Exception(utils.strfmt(lang.get("failParsePendUpd"), e))
            else:
                try:
                    configPath = os.path.join(self.basePath, const._BASE_MOD_FOLDER_PATH, *const._VERSION_FILE_PATH)
                    with open(configPath, "rb") as vf:
                        localVersion = vf.read().decode("utf-8")
                except Exception as e:
                    self.makeReinstallFlag()
                    raise Exception(utils.strfmt(lang.get("failReadVerInfo"), e))

                fileListURL = self._downloadString(self.baseURL + const._UPDATER_FILE_URL).replace("\n", "").replace("\r", "")
                changelogData = self._downloadString(self.baseURL + const._UPDATER_CHGLOG_FILE).split(";")
                for index in range(len(changelogData)):
                    changelogData[index] = changelogData[index].split(":")[0]

                while True:
                    try:    changelogData.remove("")
                    except: break

                try:
                    chglogIdx = changelogData.index(localVersion)
                except:
                    self.makeReinstallFlag()
                    raise Exception(False, lang.get("versionNotKnown"))
                if chglogIdx == len(changelogData)-1:
                    raise Exception(False, lang.get("updateNotFound"))

                progTotal = len(changelogData) - chglogIdx
                for index in range(chglogIdx + 1, len(changelogData)):
                    try:
                        self._log(utils.strfmt(lang.get("updateInfoVer"), changelogData[index]))
                        self._prog(index - chglogIdx, progTotal-1)
                        fileList = self._downloadString(fileListURL % changelogData[index]).split("\n")
                        for file in fileList:
                            if file=="": continue
                            fileModeList.append((file[0],file[1:].strip()))
                        self.fileList = self._parseAndSortDlList(fileModeList)

                    except Exception as e:
                        raise Exception(utils.strfmt(lang.get("failGetFileList"), e))
        elif (self.operationMode == const._MODE_INTCHECK):
            try:
                patchFlag = os.path.join(self.basePath, const._BASE_MOD_FOLDER_PATH, *const._PATCHFLAG_PATH)
                self.fileDelete(patchFlag)
                with open(patchFlag,"wb") as f:
                    f.write(b"lol")
            except Exception as e:
                raise Exception(utils.strfmt(lang.get("failCreateFile"), e))

            try:
                configPath = os.path.join(self.basePath, const._BASE_MOD_FOLDER_PATH, *const._VERSION_FILE_PATH)
                with open(configPath, "rb") as vf:
                    localVersion = vf.read().decode("utf-8")
            except Exception as e:
                self.makeReinstallFlag()
                raise Exception(utils.strfmt(lang.get("failReadVerInfo"), e))

            if localVersion != self.latestVersion:
                raise Exception(False, lang.get("intCheckNotUpToDate"))

            self._log(lang.get("intCheckPrep"))
            
            hashName, hashHash = [],[]
            try:
                h = self._downloadString(self.baseURL + const._INTCHECK_HASH_URL).split("\n")
                for i in h:
                    if len(i)<64 or i.find("\t")<0: continue
                    j = i.split("\t")
                    hashName.append(j[0])
                    hashHash.append(j[1])
            except: pass
            
            suffixExclude = [".flag", "/empty.txt","/expectedVer.bin"]
            try:
                fileList = self._downloadString(self.baseURL + const._INSTALLER_FILE_DIFF).split("\n")
                for file in fileList:
                    fileName = file[1:].strip()
                    fileNameF = fileName[fileName.rfind("/")+1:]
                    if self._isStoppedCallback(): raise Exception(lang.get("userCancel"))
                    if len(file)<3: continue
                    try:
                        for i in suffixExclude:
                            if fileName.endswith(i): raise InterruptedError()
                    except InterruptedError: continue
                    except Exception as e: raise e
                    if "MC".find(file[0])>=0:
                        if self.isCitra:
                            try:
                                assert file[0]!="C"
                                fileList.index("C"+fileName)
                                continue
                            except: pass
                        else:
                            if file[0]=="C": continue
                        if fileName.find("tooInstall")>0:
                            fileName = fileName.replace("tooInstall", const._BASE_MOD_NAME)
                        filePath = os.path.join(self.basePath, const._BASE_MOD_FOLDER_PATH+fileName.replace("/",os.sep))
                        isOK = os.path.exists(filePath)
                        if isOK:
                            try:
                                i = hashName.index(file)
                                h = hashHash[i]
                                with open(filePath,"rb") as f:
                                    size = f.seek(0,2)
                                    f.seek(0)
                                    ch = hashlib.sha256()
                                    while f.tell()<size:
                                        ch.update(f.read(32768))
                                        self._logCheckProgressCallback(fileList.index(file), len(fileList), f.tell(), size, fileNameF)
                                isOK = ch.digest()==bytes.fromhex(h)
                            except: pass
                        if not isOK:
                            fileModeList.append((file[0],file[1:]))
                self._logprog(lang.get("intCheckPrep"),1,1)
                self.fileList = self._parseAndSortDlList(fileModeList)
            except KeyboardInterrupt:
                raise Exception(lang.get("userCancel"))
            except Exception as e:
                raise Exception(utils.strfmt(lang.get("failPrepIntCheck"), e))
            if not len(fileModeList):
                raise Exception(False, lang.get("intCheckOK"))

    def verifySpaceAvailable(self):
        available_space = psutil.disk_usage(self.basePath).free
        neededSpace = self._checkNeededExtraSpace(available_space)
        if (neededSpace > 0):
            raise Exception(utils.strfmt(lang.get("failOutOfSpace"), neededSpace // 100000 / 10))
    
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
    def displayVersionCategory(s:int):
        if s == const.VERSION_CAT_DEV:
            return "-dev"
        if s == const.VERSION_CAT_RC:
            return "-rc"
        if s == const.VERSION_CAT_ALPHA:
            return "α"
        if s == const.VERSION_CAT_BETA:
            return "β"
        return ""

    @staticmethod
    def displayProgramVersion():
        cver = const.VERSION_NUMBER
        s = "{}.{}.{}".format(cver["major"], cver["minor"], cver["micro"])
        s += CTGP7Updater.displayVersionCategory(cver["category"])
        return s

    """
    checkProgramVersion()

    Return values:
    True  - Version is outdated
    False - Version is up-to-date
    """
    @staticmethod
    def checkProgramVersion():
        baseURL = CTGP7Updater.getDefaultCdnUrlAsString()
        cver = const.VERSION_NUMBER
        nver = CTGP7Updater._downloadString(baseURL + const._INSTALLER_VERSION, "raw").strip()
        try:
            if len(nver)>=3:
                nver = nver.decode("ascii","replace").split("-", 1)
                chk = nver[0].split(".")
                while (len(chk)<3): chk.append("0")
                if (int(chk[0]) > cver["major"]):
                    return True
                if (int(chk[1]) > cver["minor"]):
                    return True
                if (int(chk[2]) > cver["micro"]):
                    return True
            else: return True
            return False
        except Exception as e:
            raise Exception(utils.strfmt(lang.get("updateCheckFailParse"), e))

    def makePendingUpdate(self):
        header:bytes = self.latestVersion.encode("ascii") + b'\0'
        flist:bytes = b''; pendingCount:int = 0
        for entry in self.fileList:
            if not entry.havePerformed:
                flist += entry.exportToPend()
                pendingCount += 1
        header = int.to_bytes(pendingCount, 4, "little") + header

        fileName = os.path.join(self.basePath, const._BASE_MOD_FOLDER_PATH, *const._PENDINGUPDATE_PATH)
        self.mkFoldersForFile(fileName)
        self.fileDelete(fileName)
        with open(fileName,"wb") as puf:
            puf.write(header + flist)

    def startUpdate(self):
        mainfolder = os.path.join(self.basePath, const._BASE_MOD_FOLDER_PATH)
        hbrwfolder = os.path.join(self.basePath, "3ds")

        try:
            os.makedirs(mainfolder, exist_ok=True)
            os.makedirs(hbrwfolder, exist_ok=True)
        except Exception as e:
            raise Exception(utils.strfmt(lang.get("failMKDIR"), e))

        if self.isCitra:
            configPath = os.path.join(self.basePath, const._BASE_MOD_FOLDER_PATH, *const._ISCITRAFLAG_PATH)
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
                self._log(lang.get("abortInstall"))
                if (self.operationMode == const._MODE_UPDATE):
                    self._log(lang.get("abortUpdate"))
                    self.makePendingUpdate()
                if type(e)==KeyboardInterrupt: raise Exception(lang.get("userCancel"))
                raise Exception(e)

        if self.downloadCount:
            self._prog(self.currDownloadCount, self.downloadCount)
        
        ciaFile = os.path.join(self.basePath, *const._APPPACKAGE_CIA_PATH)
        ciaTemp = os.path.join(self.basePath, *const._APPPACKAGE_CIA_TEMP)
        hblFile = os.path.join(self.basePath, *const._APPPACKAGE_HBL_PATH1)
        hblFileFinal = os.path.join(self.basePath, *const._APPPACKAGE_HBL_PATH2)
        hblTemp = os.path.join(self.basePath, *const._APPPACKAGE_HBL_TEMP)
        
        self._log(lang.get("installFinishing"))

        if self.operationMode != const._MODE_DOWNLOAD:
            try:
                configPath = os.path.join(mainfolder, *const._VERSION_FILE_PATH)
                self.mkFoldersForFile(configPath)
                with open(configPath, "wb") as vf:
                    vf.write(self.latestVersion.encode("ascii"))
            except Exception as e:
                self.makeReinstallFlag()
                raise Exception(utils.strfmt(lang.get("failWriteVerInfo"), e))
        
        try:
            self.fileDelete(os.path.join(self.basePath, const._BASE_MOD_FOLDER_PATH, *const._PENDINGUPDATE_PATH))
            if os.path.exists(hblTemp):
                self.fileMove(hblTemp, hblFile)
                shutil.copyfile(hblFile, hblFileFinal)
            if os.path.exists(ciaTemp):
                self.fileMove(ciaTemp, ciaFile)
        except Exception as e:
            raise Exception(utils.strfmt(lang.get("failCleanup"), e))

        self._log("")

    def cleanInstallFolder(self):
        if (self.operationMode != const._MODE_INSTALL): return
        mainfolder = os.path.join(self.basePath, const._BASE_MOD_FOLDER_PATH)
        if (os.path.exists(mainfolder)):
            self._log(lang.get("installWiping"))
            shutil.rmtree(mainfolder)
