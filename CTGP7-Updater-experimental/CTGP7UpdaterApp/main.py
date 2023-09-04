import sys, os, shutil, ctypes, configparser

from PySide2.QtWidgets import * # type: ignore
from PySide2.QtCore import * # type: ignore
from PySide2.QtGui import * # type: ignore

from CTGP7UpdaterApp.constants import CONSTANT as const
import CTGP7UpdaterApp.lang as lang
import CTGP7UpdaterApp.utils as utils

from UI.ui_main import Ui_MainWindow
from UI.ui_dialog01 import Ui_Dialog as Ui_Dialog1
from UI.ui_intChkPick import Ui_Dialog as Ui_IntChkPick
from CTGP7UpdaterApp.dialogTemplate1 import ThreadedDialog
from CTGP7UpdaterApp.CTGP7Updater import CTGP7Updater
from CTGP7UpdaterApp.installationInfo import CTGP7InstallationInformation

class IntCheckWorkerSignals(QObject):
    progress = Signal(dict)
    error = Signal(str)
    prematureExit = Signal(str)
    success = Signal(list)
    stop = Signal()

class IntCheckWorker(QRunnable):

    def __init__(self, basedir, isCitra):
        super(IntCheckWorker, self).__init__()
        self.signals = IntCheckWorkerSignals()
        self.basedir = basedir
        self.isCitra = isCitra
        self.signals.stop.connect(self.onStop)
        self.updater = None
        self.finished = False

    def logData(self, data: dict):
        self.signals.progress.emit(data)
    
    def onStop(self):
        if (self.updater):
            self.updater.stop()

    @Slot()  # QtCore.Slot
    def run(self):
        try:
            self.logData({"m": lang.get("logInitialize")})
            self.updater = CTGP7Updater(const._MODE_INTCHECK, self.isCitra)
            self.updater.fetchDefaultCDNURL()
            self.updater.setLogFunction(self.logData)
            self.updater.getLatestVersion()
            self.updater.setBaseDirectory(self.basedir)
            self.updater.loadUpdateInfo()
        except Exception as e:
            if e.args[0]!=False:
                self.signals.error.emit(str(e))
            else:
                self.signals.prematureExit.emit(str(e.args[1]))
        else:
            files = []
            for i in self.updater.fileList:
                files.append((i.fileMethod, i.filePath[len(self.basedir)+len(const._BASE_MOD_FOLDER_PATH)+1:]))
            self.signals.success.emit(files)
        self.finished = True

class IntCheckWorker_Step2(QRunnable):

    def __init__(self, basedir, isCitra, flist):
        super(IntCheckWorker_Step2, self).__init__()
        self.signals = WorkerSignals()
        self.basedir = basedir
        self.isCitra = isCitra
        self.flist = flist
        self.signals.stop.connect(self.onStop)
        self.updater = None
        self.finished = False

    def logData(self, data: dict):
        self.signals.progress.emit(data)
    
    def onStop(self):
        if (self.updater):
            self.updater.stop()

    @Slot()  # QtCore.Slot
    def run(self):
        if not len(self.flist):
            self.signals.prematureExit.emit(lang.get("intCheckNoneSelected"))
            self.finished = True
            return
        try:
            self.logData({"m": lang.get("logInitialize")})
            self.updater = CTGP7Updater(const._MODE_DOWNLOAD, self.isCitra)
            self.updater.fetchDefaultCDNURL()
            self.updater.setLogFunction(self.logData)
            self.updater.setBaseDirectory(self.basedir)
            self.updater.fileList = self.updater._parseAndSortDlList(self.flist)
            self.updater.startUpdate()
        except Exception as e:
            if e.args[0]!=False:
                self.signals.error.emit(str(e))
            else:
                self.signals.prematureExit.emit(str(e.args[1]))
        else:
            self.signals.success.emit("")
        self.finished = True

class ChangeLogViewerRun(QRunnable, QThread):
    def __init__(self) -> None:
        super().__init__()
        self.closed = False
        self.signals = ThreadedDialog.RunSignals()
    
    @Slot()
    def setClosed(self):
        self.closed = True

    @Slot()
    def run(self):
        self.signals.title.emit(lang.get("chgLogViewTitle"))
        self.signals.text.emit(lang.get("chgLogViewDownload"))
        self.signals.progress.emit(0)
        try:
            baseURL = CTGP7Updater.getDefaultCdnUrlAsString()
            self.signals.progress.emit(33)
            hdr, text = [], []
            changelogData = CTGP7Updater._downloadString(baseURL + const._UPDATER_CHGLOG_FILE).split(";")
            self.signals.progress.emit(66)
            self.signals.text.emit(lang.get("chgLogViewParse"))
            for index in range(len(changelogData)):
                tex1 = changelogData[index]
                hdr.insert(0, tex1[:tex1.find(":")])
                tex1 = (tex1+":").replace(":","\n").replace("`","'")
                text.insert(0, tex1[tex1.find("\n")+1:].strip())
        except Exception as e:
            self.signals.minsize.emit(QSize(440, 200))
            self.signals.text.emit(Qt.MarkdownText)
            self.signals.text.emit(
                "## {}\n\n".format(lang.get("errorOccured"))+
                utils.strfmt(
                    lang.get("chgLogViewExcep"),
                    "[{}]({})".format(lang.get("discordURLName"), Window.HELP_DISCORD_LINK)
                )
            )
            self.signals.progress.emit(False)
            self.signals.detailedText.emit(False, str(e))
            return
        
        self.signals.text.emit("")
        self.signals.progress.emit(False)
        self.signals.minsize.emit(QSize(480, 300))
        
        tex1 = ""
        for i in range(len(hdr)):
            # tex1 += "### Ver. {}\n\n{}\n\n".format(hdr[i], text[i])
            tex1 += utils.strfmt("### " + lang.get("chgLogViewVerHeader"), hdr[i])
            tex1 += "\n\n{}\n\n".format(text[i])
        self.signals.detailedText.emit(False, tex1)
        self.signals.detailedText.emit(False, Qt.MarkdownText)

class WorkerSignals(QObject):
    progress = Signal(dict)
    error = Signal(str)
    prematureExit = Signal(str)
    success = Signal(str)
    stop = Signal()

class CTGP7InstallerWorker(QRunnable):

    def __init__(self, basedir, workMode, isCitra):
        super(CTGP7InstallerWorker, self).__init__()
        self.signals = WorkerSignals()
        self.basedir = basedir
        self.workMode = workMode
        self.isCitra = isCitra
        self.signals.stop.connect(self.onStop)
        self.updater = None
        self.finished = False

    def logData(self, data: dict):
        self.signals.progress.emit(data)
    
    def onStop(self):
        if (self.updater):
            self.updater.stop()

    @Slot()  # QtCore.Slot
    def run(self):
        try:
            self.logData({"m": lang.get("logInitialize")})
            self.updater = CTGP7Updater(self.workMode, self.isCitra)
            self.updater.fetchDefaultCDNURL()
            self.updater.setLogFunction(self.logData)
            self.updater.getLatestVersion()
            self.updater.setBaseDirectory(self.basedir)
            self.updater.cleanInstallFolder()
            self.updater.loadUpdateInfo()
            self.updater.verifySpaceAvailable()
            self.updater.startUpdate()
        except Exception as e:
            if e.args[0]!=False:
                self.signals.error.emit(str(e))
            else:
                self.signals.prematureExit.emit(str(e.args[1]))
        else:
            self.signals.success.emit(self.updater.latestVersion)
        self.finished = True

class Window(QMainWindow, Ui_MainWindow):
    
    HELP_DISCORD_LINK = "https://discord.com/invite/0uTPwYv3SPQww54l"
    HELP_GAMEBANANA_LINK = "https://gamebanana.com/mods/50221"
    HELP_GITHUB_LINK = "https://github.com/CyberYoshi64/CTGP7-UpdateTool/issues"

    def __init__(self, parent=None):
        self.isInit = True
        super().__init__(parent)
        lang.Initialize()
        self.setupUi(self)
        self.setDefaultText()
        self.connectSignalsSlots()
        self.workerMode = const._MODE_INSTALL
        self.isCitraPath = None
        self.hasPending = False
        self.didSaveBackup = False
        self.installerworker = None
        self.installationInfo = None
        self.checkOwnVersion()
        self.reSetup()
        self.scanForNintendo3DSSD()
        self.threadPool = QThreadPool()
        self.windowPool = []
        self.isInit = False

    def setDefaultText(self):
        self.setWindowTitle("{} v{}".format(lang.get("windowTitle"), CTGP7Updater.displayProgramVersion()))
        self.menuFile.setTitle(lang.get("barFile"))
        self.actionInstallMod.setText(lang.get("barInstall"))
        self.actionUpdateMod.setText(lang.get("barUpdate"))
        self.actionUninstall.setText(lang.get("barUninstall"))
        self.actionExit.setText(lang.get("appExit"))
        self.menuExperimental.setTitle(lang.get("barExperimental"))
        self.actionIntegChk.setText(lang.get("integChk"))
        self.actionShowChangelog.setText(lang.get("showChangelog"))
        self.menuAbout.setTitle(lang.get("barAbout"))
        self.actionAboutThisApp.setText(lang.get("aboutThisApp"))
        self.actionAboutQt.setText(lang.get("aboutQt"))
        self.menuGetHelp.setTitle(lang.get("menuGetHelp"))
        self.actionHelpGamebanana.setText(lang.get("helpGamebanana"))
        self.actionHelpGitHub.setText(lang.get("helpGitHub"))
        self.actionHelpDiscord.setText(lang.get("helpDiscord"))
        self.label_3.setText(lang.get("sdTarget"))
        self.sdRootText.setInputMask("")
        self.sdRootText.setPlaceholderText(lang.get("sdTextDefault"))
        self.sdBrowseButton.setText(lang.get("btnBrowse"))
        self.sdDetectButton.setText(lang.get("btnDetect"))
        self.miscInfoLabel.setText("")
        self.installButton.setText(lang.get("btnInstall"))
        self.updateButton.setText(lang.get("btnUpdate"))
        self.progressInfoLabel.setText("")

    def checkOwnVersion(self):
        try:
            if CTGP7Updater.checkProgramVersion():
                QMessageBox.information(self, lang.get("updateCheck"),
                    utils.strfmt(
                        lang.get("updateAvail"),
                        "<a href='{}'>{}</a>".format(self.HELP_GAMEBANANA_LINK, lang.get("updateURLName"))
                    ).replace("\n","<br>")
                )
        except Exception as e:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)
            msg.setText(
                utils.strfmt(
                        lang.get("updateCheckFail"),
                        "<a href='{}'>{}</a>".format(self.HELP_DISCORD_LINK, lang.get("discordURLName"))
                ).replace("\n","<br>")
            )
            msg.setDetailedText("{}\n\n{}: {}".format(
                str(e), lang.get("installerVerDesc"),
                CTGP7Updater.displayProgramVersion()
            ))
            msg.setWindowTitle(lang.get("updateCheck"))
            for b in msg.buttons():
                if (msg.buttonRole(b) == QMessageBox.ActionRole):
                    b.click()
                    break
            msg.exec_()

    def reportProgress(self, data: dict):
        if "m" in data:
            self.progressInfoLabel.setText(data["m"])
        if "p" in data:
            self.progressBar.setEnabled(True)
            self.progressBar.setValue((data["p"][0] / data["p"][1]) * 100)
        if "i" in data:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle(lang.get("info"))
            msg.setText(data["i"][0])
            msg.setDetailedText(data["i"][1])
            for b in msg.buttons():
                if (msg.buttonRole(b) == QMessageBox.ActionRole):
                    b.click()
                    break
            msg.exec_()
 
    def reSetup(self):
        try:    self.citraDir = self.getCitraDir()
        except: self.citraDir = None
        self.progressBar.setEnabled(False)
        self.sdBrowseButton.setEnabled(True)
        self.sdDetectButton.setEnabled(True)
        self.sdRootText.setEnabled(True)
        self.progressInfoLabel.setText("")
        self.applySDFolder(self.sdRootText.text())
        self.menuFile.setEnabled(True)
        self.menuExperimental.setEnabled(True)

    def prepateForWorker_Common(self):
        self.progressBar.setEnabled(True)
        self.sdBrowseButton.setEnabled(False)
        self.sdDetectButton.setEnabled(False)
        self.sdRootText.setEnabled(False)
        self.menuFile.setEnabled(False)
        self.menuExperimental.setEnabled(False)
        self.miscInfoLabel.setText("")
        self.setInstallBtnState(4)

    def prepareForWorker(self):
        self.installerworker.signals.progress.connect(self.reportProgress)
        self.installerworker.signals.success.connect(self.installOnSuccess)
        self.installerworker.signals.error.connect(self.installOnError)
        self.installerworker.signals.prematureExit.connect(self.installPrematureExit)
        self.prepateForWorker_Common()
    
    def prepareForIntCheckWorker1(self):
        self.installerworker.signals.progress.connect(self.reportProgress)
        self.installerworker.signals.success.connect(self.intCheckStep2)
        self.installerworker.signals.error.connect(self.intCheckError)
        self.installerworker.signals.prematureExit.connect(self.intCheckMessage)
        self.prepateForWorker_Common()
    
    def prepareForIntCheckWorker2(self):
        self.installerworker.signals.progress.connect(self.reportProgress)
        self.installerworker.signals.success.connect(self.intCheckSuccess)
        self.installerworker.signals.error.connect(self.intCheckError)
        self.installerworker.signals.prematureExit.connect(self.intCheckMessage)
        self.prepateForWorker_Common()
    
    def intCheckStep2(self, l:list):
        msg = QDialog(self)
        Ui_IntChkPick.setupUi(msg)
        msg.setWindowTitle(lang.get("intCheck"))
        msg.label.setText(utils.strfmt(lang.get("intCheckFilePick"), len(l)))
        for i in l:
            m = QListWidgetItem(msg.listWidget)
            m.setText(i[1])
            m.setCheckState(Qt.Unchecked)
            msg.listWidget.addItem(m)
        if msg.exec_():
            exclude = []
            for i in range(len(l)):
                m = msg.listWidget.item(i)
                if m.checkState() != Qt.Checked:
                    exclude.append(i)
            while len(exclude):
                l.pop(exclude.pop())
            self.installerworker = IntCheckWorker_Step2(self.sdRootText.text(), self.isCitraPath, l)
            self.prepareForIntCheckWorker2()
            self.threadPool.start(self.installerworker)
            return
        self.reSetup()

    def intCheckSuccess(self, l:list):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText(lang.get("intCheckSuccess"))
        msg.exec_()
        self.reSetup()

    def intCheckMessage(self, err:str):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Warning)
        msg.setText(err)
        msg.setWindowTitle(lang.get("warning"))
        msg.exec_()
        self.reSetup()

    def intCheckError(self, err:str):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Critical)
        msg.setText(err)
        msg.setWindowTitle(lang.get("error"))
        msg.exec_()
        self.reSetup()

    def installOnError(self, err:str):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Critical)
        msg.setText(
            "<h3>{}</h3>".format(lang.get("errorOccured"))+
            utils.strfmt(
            lang.get("errorDescGeneric").replace("\n","<br>"),
            "<a href='{}'>{}</a>".format(self.HELP_DISCORD_LINK, lang.get("discordURLName"))
        ))
        msg.setDetailedText("{}\n\n{}: {}".format(
            str(err), lang.get("installerVerDesc"),
            CTGP7Updater.displayProgramVersion()
        ))
        msg.setWindowTitle(lang.get("error"))
        for b in msg.buttons():
            if (msg.buttonRole(b) == QMessageBox.ActionRole):
                b.click()
                break
        msg.exec_()
        self.reSetup()#self.close()
    
    def installPrematureExit(self, err:str):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Warning)
        msg.setText(err)
        msg.setWindowTitle(lang.get("warning"))
        msg.exec_()
        self.reSetup()#self.close()
    
    def installOnSuccess(self, ver:str):
        QMessageBox.information(
            self, lang.get("success"),
            utils.strfmt(lang.get("installSuccess"), ver)
        )
        if (self.didSaveBackup):
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Question)
            msg.addButton(QMessageBox.Yes)
            msg.addButton(QMessageBox.No)
            msg.setDefaultButton(QMessageBox.No)
            msg.setWindowTitle(lang.get("saveBackup"))
            msg.setText(lang.get("saveBackupRestoreQuestion"))
            if (msg.exec_() == QMessageBox.Yes):
                savefolder = os.path.join(self.sdRootText.text(), *const._SAVEBAK_MOD_PATH)
                backupfolder = os.path.join(self.sdRootText.text(), const._SAVEBAK_BAK_PATH)
                try:
                    shutil.copytree(backupfolder, savefolder)
                except Exception as e:
                    self.installOnError(utils.strfmt(lang.get("failSaveBackupRestore"), e))
                    return
        self.reSetup()#self.close()

    def doSaveBackup(self):
        try:
            savefolder = os.path.join(self.sdRootText.text(), *const._SAVEBAK_MOD_PATH)
            backupfolder = os.path.join(self.sdRootText.text(), const._SAVEBAK_BAK_PATH)
            if (os.path.exists(savefolder)):
                self.reportProgress({"m": lang.get("logSaveBackupCreate")})
                if (os.path.exists(backupfolder)):
                    shutil.rmtree(backupfolder)
                os.rename(savefolder, backupfolder)
                self.didSaveBackup = True
                QMessageBox.information(self, lang.get("saveBackup"), utils.strfmt(lang.get("saveBackupCreatedAt"), backupfolder))
            elif (os.path.exists(backupfolder)):
                msg = QMessageBox(self)
                msg.setIcon(QMessageBox.Question)
                msg.addButton(QMessageBox.Yes)
                msg.addButton(QMessageBox.No)
                msg.setDefaultButton(QMessageBox.No)
                msg.setWindowTitle(lang.get("confirm"))
                msg.setText(lang.get("saveBackupFoundOld"))
                self.didSaveBackup = msg.exec_() == QMessageBox.Yes
            return True
        except Exception as e:
            self.installOnError(utils.strfmt(lang.get("failSaveBackupCreate"), e))
            return False

    def selectSDFromList(self, l:list)->str:
        dlg = QDialog(self)
        Ui_Dialog1.setupUi(dlg)
        dlg.setWindowTitle(lang.get("sdDetectionTitle"))
        dlg.label.setText(
            utils.strfmt(lang.get("sdDetectionHeader"), len(l))
        )
        for i in l: dlg.sdList.addItem(i)
        dlg.sdList.setCurrentRow(0)
        if dlg.exec_():
            return dlg.sdList.selectedItems()[0].text()
        return None

    def scanForNintendo3DSSD(self):
        fol = CTGP7Updater.findNintendo3DSRoot()
        if self.citraDir == False:
            QMessageBox.information(self, lang.get("warning"), lang.get("citraNoSD"))
        elif self.citraDir:
            doesCitraExist = os.path.exists(self.citraDir)
            if (doesCitraExist): fol.append(self.citraDir)
        if self.isInit and (len(fol)==1):
            if (fol[0] == self.citraDir):
                QMessageBox.information(self, lang.get("warning"), lang.get("sdFoundOnlyCitra"))
            self.sdRootText.setText(fol[0])
        elif (len(fol)<1):
            QMessageBox.information(self, lang.get("warning"), lang.get("sdNoneDetected"))
        else:
            if self.isInit:
                self.sdRootText.setText(fol[0])
            else:
                s = self.selectSDFromList(fol)
                if type(s)==str:
                    self.sdRootText.setText(s)
            
    def updateButtonPress(self):
        if self.hasPending:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Question)
            msg.addButton(QMessageBox.Yes)
            msg.addButton(QMessageBox.No)
            msg.setDefaultButton(QMessageBox.No)
            msg.setWindowTitle(lang.get("confirm"))
            msg.setText(
                "<h3>{}</h3>".format(lang.get("pendUpdate"))+
                lang.get("pendUpdateContinue").replace("\n","<br>")
            )
            if msg.exec_() == QMessageBox.No: return
        
        self.workerMode = const._MODE_UPDATE
        self.miscInfoLabel.setText("")
        self.installerworker = CTGP7InstallerWorker(self.sdRootText.text(), self.workerMode, self.isCitraPath)
        self.prepareForWorker()
        self.threadPool.start(self.installerworker)
    
    def removeButtonPress(self):
        haveSave = os.path.exists(os.path.join(self.sdRootText.text(), *const._SAVEBAK_MOD_PATH))
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Warning)
        if haveSave:
            msg.addButton(QMessageBox.Yes)
            msg.addButton(QMessageBox.No)
        else:
            msg.addButton(QMessageBox.StandardButton.Ok)
        msg.addButton(QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Cancel)
        msg.setWindowTitle(lang.get("warning"))
        if haveSave:
            msg.setText(lang.get("unInstallQuestion"))
        else:
            msg.setText(lang.get("unInstallQuestionNoSave"))
        res = msg.exec_()
        if res == QMessageBox.Cancel: return
        if haveSave:
            if res == QMessageBox.Yes:
                if not self.doSaveBackup(): return

        self.reportProgress({"m": lang.get("installWiping")})
        self.setInstallBtnState(0)
        try:
            updater = CTGP7Updater()
            updater.setLogFunction(self.reportProgress)
            updater.setBaseDirectory(self.sdRootText.text())
            updater.cleanInstallFolder()
        except Exception as e:
            self.installOnError(utils.strfmt(lang.get("unInstallError"),str(e)))
        else:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle(lang.get("info"))
            msg.setText(lang.get("unInstallOK"))
            msg.exec_()
            self.reSetup()

    def performIntegrityCheck(self):
        self.workerMode = const._MODE_INTCHECK
        self.miscInfoLabel.setText("")
        self.installerworker = IntCheckWorker(self.sdRootText.text(), self.isCitraPath)
        self.prepareForIntCheckWorker1()
        self.threadPool.start(self.installerworker)
    
    def installButtonPress(self):
        if (self.startButtonState > 0 and self.startButtonState < 4):
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle(lang.get("warning"))
            msg.addButton(QMessageBox.Yes)
            msg.addButton(QMessageBox.No)
            msg.setDefaultButton(QMessageBox.No)
            
            if (self.startButtonState == 2):
                
                msg.setText(lang.get("reinstallConfirmRegular"))
                if msg.exec_() == QMessageBox.No: return
            
            if (self.startButtonState == 3):
                msg.setText(lang.get("reinstallConfirmNeeded"))
                if msg.exec_() == QMessageBox.No: return
            
            if self.workerMode and (self.isCitraPath == None):
                msg = QMessageBox(self)
                msg.setWindowTitle(lang.get("question"))
                msg.setIcon(QMessageBox.Question)
                msg.setText(lang.get("installTargetAsk"))
                msg.addButton(lang.get("btn3DS"), QMessageBox.NoRole)
                dlgisCitra = msg.addButton(lang.get("btnCitra"), QMessageBox.NoRole)
                dlgCancel = msg.addButton(lang.get("btnCancel"), QMessageBox.NoRole)
                msg.setDefaultButton(dlgCancel)
                msg.exec_()
                if msg.clickedButton() == dlgCancel: return
                self.isCitraPath = (msg.clickedButton() == dlgisCitra)

            if not self.doSaveBackup(): return
            self.workerMode = const._MODE_INSTALL
            self.installerworker = CTGP7InstallerWorker(self.sdRootText.text(), self.workerMode, self.isCitraPath)
            self.prepareForWorker()
            self.threadPool.start(self.installerworker)
        elif (self.startButtonState == 4):
            if (self.installerworker):
                self.installerworker.signals.stop.emit()
            self.setInstallBtnState(0)

    def setInstallBtnState(self, state):
        self.startButtonState = state
        self.installButton.setEnabled(state != 0)
        self.updateButton.setText(lang.get("btnPendingUpdate") if self.hasPending else lang.get("btnUpdate"))
        self.updateButton.setEnabled(True)
        self.updateButton.setHidden(True)
        if (state == 0):
            self.installButton.setText("")
            self.installButton.clearFocus()
            self.updateButton.setText("")
            self.updateButton.clearFocus()
        elif (state == 1):
            self.installButton.setText(lang.get("btnInstall"))
        elif (state == 2):
            self.installButton.setText(lang.get("btnReinstall"))
            self.updateButton.setHidden(False)
        elif (state == 3):
            self.installButton.setText(lang.get("btnReinstall"))
        elif (state == 4):
            self.installButton.setText(lang.get("btnCancel"))
        self.updateButton.setEnabled(not self.updateButton.isHidden())
        self.actionInstallMod.setEnabled(self.installButton.isEnabled())
        self.actionUpdateMod.setEnabled(self.updateButton.isEnabled())

    def applySDFolder(self, folder: str):
        self.miscInfoLabel.setText("")
        self.setInstallBtnState(0)
        self.isCitraPath = self.isCitraDirectory(folder)
        self.actionUninstall.setEnabled(False)
        if (os.path.exists(folder)):
            self.installationInfo = CTGP7InstallationInformation(folder)
            self.miscInfoLabel.setText(utils.strfmt(
                lang.get("instVerdict"),
                self.installationInfo.stateDescription()
            ))
            
            self.actionUninstall.setEnabled(CTGP7Updater.doesInstallExist(folder))
            if self.installationInfo.good():
                self.hasPending = self.installationInfo.hasPendingUpdate
                self.miscInfoLabel.setStyleSheet("color: #480")
                self.setInstallBtnState(2)
            elif not CTGP7Updater._isValidNintendo3DSSDCard(folder):
                self.miscInfoLabel.setText(lang.get("sdMaybeUnrelated"))
                self.miscInfoLabel.setStyleSheet("color: #c60")
                self.setInstallBtnState(1)
            elif not CTGP7Updater.doesInstallExist(folder):
                self.miscInfoLabel.setText(lang.get("readyToInstall"))
                self.miscInfoLabel.setStyleSheet("color: #084")
                self.setInstallBtnState(1)
            else:
                self.miscInfoLabel.setStyleSheet("color: #f04")
                self.setInstallBtnState(3)
        else:
            self.miscInfoLabel.setText(lang.get("invalidPath"))
            self.miscInfoLabel.setStyleSheet("color: red")
            self.setInstallBtnState(0)

    # You never know when people don't know what "root" is
    # in terms of directories
    def tryCorrectSDPath(self, f:str) -> str:
        p = ['3ds', 'Nintendo 3DS', 'cias', 'cia', 'CTGP-7', 'gamefs', 'savefs', 'config', 'resources', 'MyStuff', 'luma', 'gm9', 'private']
        ff = f.split(os.sep)
        if os.name!="nt": ff[0]="/" # Linux needs this for absolute path
        run = True; l = len(ff)
        while run:
            for i in p:
                if len(ff)<3: run = False; break
                for j in range(-3,0):
                    if ff[j]==i: ff.pop()
            if len(ff) == l: break
            l = len(ff)
        newf = ""
        for i in ff:
            if i=="/": newf="/"
            else: newf += "%s%s" % (i, os.sep)
        return newf

    def getCitraDir(self) -> str:
        c = configparser.ConfigParser() # INI
        if os.name == "nt":
            p="%s\\Citra\\sdmc"%os.environ['APPDATA']
            c.read("%s\\Citra\\config\\qt-config.ini"%os.environ['APPDATA'])
        elif os.name == "posix":
            p="%s/.local/share/citra-emu/sdmc"%os.environ['HOME']
            c.read("%s/.config/citra-emu/qt-config.ini"%os.environ['HOME'])

        if not c.getboolean("Data%20Storage","use_virtual_sd"): return False
        if c.getboolean("Data%20Storage","use_custom_storage"):
            p = c.get("Data%20Storage","sdmc_directory")
        return p
    
    def isCitraDirectory(self, path:str):
        try:
            if os.path.samefile(path, self.citraDir): # Linux is case-sensitive, Windows may use inconsistent casing, ruining simple checks
                                                      # Added bonus: symlinks would work this way too.
                return True
            else:
                if os.path.exists(os.path.join(path, "Nintendo 3DS", "0"*32)):
                    return True
                if os.path.exists(os.path.join(path, *const._ISCITRAFLAG_PATH)):
                    return True
            return None
        except:
            return None


    def selectSDDirectory(self):
        dialog = QFileDialog()
        folder_path = dialog.getExistingDirectory(self, lang.get("sdSelectDest"), self.sdRootText.text())
        if (folder_path != ""):
            folder_path = folder_path.replace("/", os.path.sep).replace("\\", os.path.sep)
            self.sdRootText.setText(self.tryCorrectSDPath(folder_path))
    
    def dialogClose(self, dlg):
        try:
            self.windowPool.remove(dlg)
            dlg.close()
        except:
            pass

    def spawnThreadedDialog(self, thread, modality):
        dlg = ThreadedDialog.Dialog()
        dlg.scrollArea.setHidden(True)
        dlg.progBar.setHidden(True)
        dlg.buttonBox.setHidden(True)
        dlg.setWindowModality(modality)
        thread.signals.progress.connect(dlg._setProgress)
        thread.signals.title.connect(dlg._setTitle)
        thread.signals.text.connect(dlg._setText)
        thread.signals.size.connect(dlg._setSize)
        thread.signals.minsize.connect(dlg._setMinSize)
        thread.signals.detailedText.connect(dlg._setDetailedText)
        thread.signals.buttons.connect(dlg._setButtons)
        thread.signals.closed.connect(dlg.onClose)
        dlg.signals.closed.connect(self.dialogClose)
        dlg.signals.closed2.connect(thread.setClosed)
        self.windowPool.append(dlg)
        dlg.open()
        self.threadPool.start(thread)
        
    def changeLogViewer(self):
        if not lang.isNative(): QMessageBox.warning(self, lang.get("warning"), lang.get("nonEnglishWarn"))
        QMessageBox.warning(self, lang.get("warning"), lang.get("chglogWarning"))
        self.spawnThreadedDialog(ChangeLogViewerRun(), Qt.WindowModality.NonModal)

    def showHelpDialog(self):
        msg = QMessageBox(self)
        msg.setWindowTitle(lang.get("aboutThisAppTitle"))
        msg.setIcon(QMessageBox.Information)
        msg.setText(
            utils.strfmt(
            lang.get("aboutThisAppText"),
            utils.strfmt(lang.get("version0"), CTGP7Updater.displayProgramVersion()),
            "<a href='{}'>{}</a>".format(self.HELP_DISCORD_LINK, lang.get("discordURLName"))
            ).replace("\n","<br>")+
            "<br><br>2021-2023 CyberYoshi64, PabloMK7"
        )
        msg.exec_()

    def aboutQt(self):
        QMessageBox.aboutQt(self)

    def openBrowserGitHub(self):
        QDesktopServices.openUrl(QUrl(self.HELP_GITHUB_LINK))

    def openBrowserGameBanana(self):
        QDesktopServices.openUrl(QUrl(self.HELP_GAMEBANANA_LINK))

    def openDiscord(self):
        QDesktopServices.openUrl(QUrl(self.HELP_DISCORD_LINK))

    def quitApp(self):
        self.close()

    def featureNotImplemented(self):
        QMessageBox.warning(self, lang.get("featureNotImpl"), lang.get("featureNotImplText"))

    def connectSignalsSlots(self):
        self.sdBrowseButton.clicked.connect(self.selectSDDirectory)
        self.sdDetectButton.clicked.connect(self.scanForNintendo3DSSD)
        self.sdRootText.textChanged.connect(lambda s: self.applySDFolder(s))
        self.actionAboutThisApp.triggered.connect(self.showHelpDialog)
        self.installButton.clicked.connect(self.installButtonPress)
        self.updateButton.clicked.connect(self.updateButtonPress)
        self.actionInstallMod.triggered.connect(self.installButtonPress)
        self.actionUpdateMod.triggered.connect(self.updateButtonPress)
        self.actionUninstall.triggered.connect(self.removeButtonPress)
        self.actionExit.triggered.connect(self.quitApp)
        self.actionAboutQt.triggered.connect(self.aboutQt)
        self.actionHelpDiscord.triggered.connect(self.openDiscord)
        self.actionHelpGamebanana.triggered.connect(self.openBrowserGameBanana)
        self.actionHelpGitHub.triggered.connect(self.openBrowserGitHub)

        self.actionShowChangelog.triggered.connect(self.changeLogViewer)
        self.actionIntegChk.triggered.connect(self.performIntegrityCheck)

    def closeEvent(self, event: QCloseEvent) -> None:
        i = 0
        
        if self.installerworker and not self.installerworker.finished:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle(lang.get("warning"))
            msg.addButton(QMessageBox.Ok)
            msg.setText(lang.get("cantExitWorkerActive"))
            msg.exec_()
            event.ignore()
            return

        while (
            (not self.threadPool.waitForDone(100)) or 
            len(self.windowPool)
        ):
            for j in self.windowPool:
                if j and hasattr(j,"close"):
                    j.close()
                else:
                    self.windowPool.remove(j)
            i+=1
            if not (i % 50):
                msg = QMessageBox(self)
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle(lang.get("warning"))
                msg.addButton(QMessageBox.Yes)
                msg.addButton(QMessageBox.No)
                msg.addButton(QMessageBox.Retry)
                msg.setDefaultButton(QMessageBox.No)
                msg.setText(lang.get("cantExitAskForce"))
                btn = msg.exec_()
                if (btn == QMessageBox.No):
                    event.ignore()
                    return
                elif (btn == QMessageBox.Yes):
                    break
        event.accept()
def startUpdaterApp():
    app = QApplication(sys.argv)
    win = Window()
    try:
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(u"ctgp7.ctgp7.installer.1_1") # So that the taskbar shows the window icon on windows
    except:
        pass
    win.show()
    sys.exit(app.exec_())