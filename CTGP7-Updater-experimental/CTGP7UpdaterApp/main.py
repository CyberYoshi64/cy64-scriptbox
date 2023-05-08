import sys
import os
import shutil

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from CTGP7UpdaterApp.ui_main import Ui_MainWindow
from CTGP7UpdaterApp.ui_dialog01 import Ui_Dialog as Ui_Dialog1
from CTGP7UpdaterApp.ui_chglogvwr import Ui_Dialog as Ui_ChglogVwr

from CTGP7UpdaterApp.dialogTemplate1 import ThreadedDialog

from CTGP7UpdaterApp.CTGP7Updater import CTGP7Updater
import ctypes

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
        self.signals.title.emit("Changelog Viewer")
        self.signals.text.emit("Downloading changelog...")
        self.signals.progress.emit(0)
        try:
            baseURL = CTGP7Updater.getDefaultCdnUrlAsString()
            self.signals.progress.emit(33)
            hdr, text = [], []
            changelogData = CTGP7Updater._downloadString(baseURL + CTGP7Updater._UPDATER_CHGLOG_FILE).split(";")
            self.signals.progress.emit(66)
            self.signals.text.emit("Parsing data...")
            for index in range(len(changelogData)):
                tex1 = changelogData[index]
                hdr.insert(0, tex1[:tex1.find(":")])
                tex1 = (tex1+":").replace(":","\n").replace("`","'")
                text.insert(0, tex1[tex1.find("\n")+1:].strip())
        except Exception as e:
            self.signals.minsize.emit(QSize(440, 200))
            self.signals.text.emit(Qt.MarkdownText)
            self.signals.text.emit(
                "## An error has occured\n\n"+
                "Could not display changelog. See the below error details.\n\n"+
                "Ask for help in the [CTGP-7 Discord Server]({}) ".format(Window.HELP_DISCORD_LINK)+
                "if this error keeps occuring."
            )
            self.signals.progress.emit(False)
            self.signals.detailedText.emit(False, str(e))
            return
        
        self.signals.text.emit("")
        self.signals.progress.emit(False)
        self.signals.minsize.emit(QSize(480, 300))
        
        tex1 = ""
        for i in range(len(hdr)):
            tex1 += "### Ver. {}\n\n```\n{}\n```\n\n".format(hdr[i], text[i])
        self.signals.detailedText.emit(False, tex1)
        self.signals.detailedText.emit(False, Qt.MarkdownText)

class WorkerSignals(QObject):
    progress = Signal(dict)
    error = Signal(str)
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
            self.logData({"m": "Initializing..."})
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
            self.signals.error.emit(str(e))
        else:
            self.signals.success.emit(self.updater.latestVersion)
        self.finished = True

class Window(QMainWindow, Ui_MainWindow):
    
    HELP_DISCORD_LINK = "https://discord.com/invite/0uTPwYv3SPQww54l"
    
    def __init__(self, parent=None):
        self.isInit = True
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("CTGP-7 Installer v{}".format(CTGP7Updater.VERSION_NUMBER))
        self.connectSignalsSlots()
        self.workerMode = CTGP7Updater._MODE_INSTALL
        self.isCitraPath = None
        self.hasPending = False
        self.didSaveBackup = False
        self.installerworker = None
        self.checkOwnVersion()
        self.scanForNintendo3DSSD()
        self.reSetup()
        self.threadPool = QThreadPool()
        self.windowPool = []
        self.isInit = False

    def checkOwnVersion(self):
        try:
            if CTGP7Updater.checkProgramVersion():
                QMessageBox.information(self, "Update Check",
                    "There's a new update available for the PC installer.<br><br>"+
                    "It is recommended to visit the <a href='https://gamebanana.com/mods/50221'>Gamebanana page</a> "+
                    "to download the latest version to ensure that the PC installer can work smoothly."
                )
        except Exception as e:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)
            msg.setText(
                "An error has occurred while checking for updates.<br>"+
                "Ensure your device is connected to the internet.<br><br>"+
                "If this error keeps happening, ask for help in the "+
                "<a href='https://discord.com/invite/0uTPwYv3SPQww54l'>"+
                "CTGP-7 Discord Server</a>."
            )
            msg.setDetailedText("{}\n\nInstaller version: {}".format(str(e), CTGP7Updater.VERSION_NUMBER))
            msg.setWindowTitle("Update Check")
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
 
    def reSetup(self):
        self.progressBar.setEnabled(False)
        self.sdBrowseButton.setEnabled(True)
        self.sdDetectButton.setEnabled(True)
        self.sdRootText.setEnabled(True)
        self.progressInfoLabel.setText("")
        self.applySDFolder(self.sdRootText.text())
        self.menuFile.setEnabled(True)
        self.menuExperimental.setEnabled(True)

    def prepareForWorker(self):
        self.progressBar.setEnabled(True)
        self.sdBrowseButton.setEnabled(False)
        self.sdDetectButton.setEnabled(False)
        self.sdRootText.setEnabled(False)
        self.menuFile.setEnabled(False)
        self.menuExperimental.setEnabled(False)
        self.miscInfoLabel.setText("")
        self.setInstallBtnState(4)
    
    def installOnError(self, err:str):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Critical)
        msg.setText(
            "An error has occurred.<br>"+
            "See the error information below.<br><br>"+
            "Ask for help in the <a href='"+self.HELP_DISCORD_LINK+
            "'>CTGP-7 Discord Server</a>, if this error keeps happening."
        )
        msg.setDetailedText("{}\n\nInstaller version: {}".format(str(err), CTGP7Updater.VERSION_NUMBER))
        msg.setWindowTitle("Error")
        for b in msg.buttons():
            if (msg.buttonRole(b) == QMessageBox.ActionRole):
                b.click()
                break
        msg.exec_()
        self.reSetup()#self.close()
    
    def installOnSuccess(self, ver:str):
        QMessageBox.information(self, "Operation successful", "Installation finished successfully! (v{})<br>Make sure to install the CIA file in the CTGP-7 -> cia folder on the SD card.".format(ver))
        if (self.didSaveBackup):
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Question)
            msg.addButton(QMessageBox.Yes)
            msg.addButton(QMessageBox.No)
            msg.setDefaultButton(QMessageBox.No)
            msg.setWindowTitle("Save backup")
            msg.setText("Would you like to restore the save backup done previously?")
            if (msg.exec_() == QMessageBox.Yes):
                savefolder = os.path.join(self.sdRootText.text(), "CTGP-7", "savefs")
                backupfolder = os.path.join(self.sdRootText.text(), "CTGP-7savebak")
                try:
                    shutil.copytree(backupfolder, savefolder)
                except Exception as e:
                    self.installOnError("Failed to restore save backup, please restore it manually: {}".format(e))
                    return
        self.reSetup()#self.close()

    def doSaveBackup(self):
        try:
            savefolder = os.path.join(self.sdRootText.text(), "CTGP-7", "savefs")
            backupfolder = os.path.join(self.sdRootText.text(), "CTGP-7savebak")
            if (os.path.exists(savefolder)):
                self.reportProgress({"m": "Creating save backup..."})
                if (os.path.exists(backupfolder)):
                    shutil.rmtree(backupfolder)
                os.rename(savefolder, backupfolder)
                self.didSaveBackup = True
                QMessageBox.information(self, "Save backup", "Save data backup of the previous CTGP-7 installation has been made in {}".format(backupfolder))
            elif (os.path.exists(backupfolder)):
                msg = QMessageBox(self)
                msg.setIcon(QMessageBox.Question)
                msg.addButton(QMessageBox.Yes)
                msg.addButton(QMessageBox.No)
                msg.setDefaultButton(QMessageBox.No)
                msg.setWindowTitle("Detected save data backup")
                msg.setText(
                    "While no save data could be detected for CTGP-7, "+
                    "a backup was detected.\n\nDo you want to use it?"
                )
                self.didSaveBackup = msg.exec_() == QMessageBox.Yes
            return True
        except Exception as e:
            self.installOnError("Failed to create save backup: {}".format(e))
            return False

    def selectSDFromList(self, l:list)->str:
        dlg = QDialog(self)
        Ui_Dialog1.setupUi(dlg)
        dlg.setWindowTitle("Select SD Card")
        dlg.label.setText(
            "Detected SD Card count: {}\n\n".format(len(l)) +
            "Please select the one you want to manage installations on."
        )
        for i in l: dlg.sdList.addItem(i)
        dlg.sdList.setCurrentRow(0)
        if dlg.exec_():
            return dlg.sdList.selectedItems()[0].text()
        return None

    def scanForNintendo3DSSD(self):
        fol = CTGP7Updater.findNintendo3DSRoot()
        citraDir = CTGP7Updater.getCitraDir()
        doesCitraExist = os.path.exists(citraDir)
        if (doesCitraExist): fol.append(citraDir)
        if self.isInit and (len(fol)==1):
            if (fol[0] == citraDir):
                QMessageBox.information(self, "Warning", "Couldn't detect an SD Card but a Citra build was found.\n\nIf you want to install/update CTGP-7 for a 3DS console, use the \"Browse\" button to navigate to the SD Card of your console.")
            self.sdRootText.setText(fol[0])
        elif (len(fol)<1):
            QMessageBox.information(self, "Warning", "No SD Card could be detected.\n\nMake sure the SD Card is inserted into your device and mounted.")
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
            msg.setIcon(QMessageBox.Warning)
            msg.addButton(QMessageBox.Yes)
            msg.addButton(QMessageBox.No)
            msg.setDefaultButton(QMessageBox.No)
            msg.setWindowTitle("Pending update")
            msg.setText("A pending update was detected. You must finish it first, before updating again. Do you want to continue this update?")
            if msg.exec_() == QMessageBox.No: return
        
        self.workerMode = CTGP7Updater._MODE_UPDATE
        self.miscInfoLabel.setText("")
        self.installerworker = CTGP7InstallerWorker(self.sdRootText.text(), self.workerMode, self.isCitraPath)
        self.installerworker.signals.progress.connect(self.reportProgress)
        self.installerworker.signals.success.connect(self.installOnSuccess)
        self.installerworker.signals.error.connect(self.installOnError)
        self.prepareForWorker()
        self.threadPool.start(self.installerworker)
    
    def performIntegrityCheck(self):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Warning)
        msg.addButton(QMessageBox.Yes)
        msg.addButton(QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        msg.setWindowTitle("Warning")
        msg.setText(
            "Integrity Check is a W.I.P. feature.\n"+
            "It can currently only redownload missing files."+
            
            #"\n\nAny modifications that are done outside of MyStuff "+
            #"will be replaced."
            "\n\nDo you want to continue?"
        )
        if msg.exec_() == QMessageBox.No: return

        self.workerMode = CTGP7Updater._MODE_INTCHECK
        self.miscInfoLabel.setText("")
        self.installerworker = CTGP7InstallerWorker(self.sdRootText.text(), self.workerMode, self.isCitraPath)
        self.installerworker.signals.progress.connect(self.reportProgress)
        self.installerworker.signals.success.connect(self.installOnSuccess)
        self.installerworker.signals.error.connect(self.installOnError)
        self.prepareForWorker()
        self.threadPool.start(self.installerworker)
    
    def installButtonPress(self):
        if (self.startButtonState > 0 and self.startButtonState < 4):
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.addButton(QMessageBox.Yes)
            msg.addButton(QMessageBox.No)
            msg.setDefaultButton(QMessageBox.No)
            
            if (self.startButtonState == 2):
                msg.setWindowTitle("Confirm re-installation")
                msg.setText("You are about to re-install CTGP-7.<br>Any modifications via MyStuff will be deleted.<br><br>Do you want to continue?<br>(Your save data will be backed up, if possible.)")
                if msg.exec_() == QMessageBox.No: return
            
            if (self.startButtonState == 3):
                msg.setWindowTitle("Broken CTGP-7 installation")
                msg.setText("This installation is either corrupted or was flagged for removal. Proceeding will wipe this installation and create a new one.<br><br>Do you want to proceed anyway?<br>(Your save data will be backed up, if possible.)")
                if msg.exec_() == QMessageBox.No: return
            
            if self.workerMode and (self.isCitraPath == None):
                msg = QMessageBox(self)
                msg.setWindowTitle("Question")
                msg.setIcon(QMessageBox.Question)
                msg.setText("Unable to determine, whether this installation is meant for a 3DS or Citra.<br><br>Please select which platform you want to install CTGP-7 for.")
                dlgIs3DS = msg.addButton("3DS", QMessageBox.NoRole)
                dlgisCitra = msg.addButton("Citra", QMessageBox.NoRole)
                dlgCancel = msg.addButton("Cancel", QMessageBox.NoRole)
                msg.setDefaultButton(dlgCancel)
                msg.exec_()
                if msg.clickedButton() == dlgCancel: return
                self.isCitraPath = (msg.clickedButton() == dlgisCitra)

            if not self.doSaveBackup(): return
            self.workerMode = CTGP7Updater._MODE_INSTALL
            self.installerworker = CTGP7InstallerWorker(self.sdRootText.text(), self.workerMode, self.isCitraPath)
            self.installerworker.signals.progress.connect(self.reportProgress)
            self.installerworker.signals.success.connect(self.installOnSuccess)
            self.installerworker.signals.error.connect(self.installOnError)
            self.prepareForWorker()
            self.threadPool.start(self.installerworker)
        elif (self.startButtonState == 4):
            if (self.installerworker):
                self.installerworker.signals.stop.emit()
            self.setInstallBtnState(0)

    def setInstallBtnState(self, state):
        self.startButtonState = state
        self.installButton.setEnabled(state != 0)
        self.updateButton.setText("Continue update" if self.hasPending else "Update")
        self.updateButton.setEnabled(True)
        self.updateButton.setHidden(True)
        if (state == 0):
            self.installButton.setText("")
            self.installButton.clearFocus()
            self.updateButton.setText("")
            self.updateButton.clearFocus()
        elif (state == 1):
            self.installButton.setText("Install")
        elif (state == 2):
            self.installButton.setText("Re-install")
            self.updateButton.setHidden(False)
        elif (state == 3):
            self.installButton.setText("Re-install")
        elif (state == 4):
            self.installButton.setText("Cancel")
        self.updateButton.setEnabled(not self.updateButton.isHidden())
        self.actionInstallMod.setEnabled(self.installButton.isEnabled())
        self.actionUpdateMod.setEnabled(self.updateButton.isEnabled())

    def applySDFolder(self, folder: str):
        if (folder == "" or folder[-1]==" "):
            self.miscInfoLabel.setText("")
            self.setInstallBtnState(0)
            return
        self.isCitraPath = CTGP7Updater.isCitraDirectory(folder)
        if (os.path.exists(folder)):
            if not CTGP7Updater._isValidNintendo3DSSDCard(folder):
                self.miscInfoLabel.setText("This path appears to not be of a 3DS SD Card.")
                self.miscInfoLabel.setStyleSheet("color: #c60")
            if not CTGP7Updater.doesInstallExist(folder):
                self.miscInfoLabel.setText("Ready to install CTGP-7.")
                self.miscInfoLabel.setStyleSheet("color: #084")
                self.setInstallBtnState(1)
            elif not CTGP7Updater.isVersionValid(folder):
                self.miscInfoLabel.setText("Corrupted CTGP-7 installation detected.")
                self.miscInfoLabel.setStyleSheet("color: #f40")
                self.setInstallBtnState(3)
            elif CTGP7Updater.hasBrokenFlag(folder):
                self.miscInfoLabel.setText("Broken CTGP-7 installation detected.")
                self.miscInfoLabel.setStyleSheet("color: #f24")
                self.setInstallBtnState(3)
            else:
                self.hasPending = CTGP7Updater.hasPendingInstall(folder)
                self.miscInfoLabel.setText("Valid CTGP-7 installation detected.")
                self.miscInfoLabel.setStyleSheet("color: #480")
                self.setInstallBtnState(2)
        else:
            self.miscInfoLabel.setText("Folder does not exist")
            self.miscInfoLabel.setStyleSheet("color: red")
            self.setInstallBtnState(0)

    # You never know when people don't know what "root" is
    # in terms of directories
    def tryCorrectSDPath(self, f:str) -> str:
        p = ['3ds', 'Nintendo 3DS', 'cias', 'CTGP-7', 'luma', 'gm9', 'private']
        c = ["AppData",".local","Roaming" ,"share", "Citra", "citra-emu", "sdmc"]
        ff = f.split(os.sep)
        if os.name!="nt": ff[0]="/" # Linux needs this for absolute path
        run = True; l = len(ff)
        while run:
            for i in p:
                if len(ff)<2: run = False; break
                for j in range(-3,0):
                    if ff[j]==i: ff.pop()
            if len(ff) == l: break
            l = len(ff)
        for i in c:
            try: assert os.path.exists(os.path.join(*ff, i))
            except: pass
            else: ff.append(i)
        newf = ""
        for i in ff:
            if i=="/": newf="/"
            else: newf += "%s%s" % (i, os.sep)
        return newf

    def selectSDDirectory(self):
        dialog = QFileDialog()
        folder_path = dialog.getExistingDirectory(self, "Select destination", self.sdRootText.text())
        if (folder_path != ""):
            folder_path = folder_path.replace("/", os.path.sep).replace("\\", os.path.sep)
            folder_path = self.tryCorrectSDPath(folder_path)
            self.sdRootText.setText(folder_path)
    
    def dialogClose(self, dlg):
        try:
            self.windowPool.remove(dlg)
            dlg.close()
        except:
            pass

    def spawnThreadedDialog(self, thread, modality):
        try:
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
        except Exception as e:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)
            msg.setText(
                "An error has occurred while opening a dialog box.<br>"+
                "This is probably a bug and should be reported.<br><br>"+
                "File an issue on the GitHub repository with the below error."
            )
            msg.setDetailedText(e)
            msg.exec_()
        else:
            dlg.open()
            self.threadPool.start(thread)
        
    def changeLogViewer(self):
        self.spawnThreadedDialog(ChangeLogViewerRun(), Qt.WindowModality.NonModal)

    def showHelpDialog(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("About this application")
        msg.setIcon(QMessageBox.Information)
        msg.setText(
            "CTGP-7 Installer v"+CTGP7Updater.VERSION_NUMBER+"<br><br>"+
            "Having issues? Ask for help in the "+
            "<a href='https://discord.com/invite/0uTPwYv3SPQww54l'>"+
            "Discord server</a>.<br><br>"+
            "2021-2023 CyberYoshi64, PabloMK7"
        )
        msg.exec_()

    def aboutQt(self):
        QMessageBox.aboutQt(self)

    def openBrowserGitHub(self):
        QDesktopServices.openUrl(QUrl("https://github.com/CyberYoshi64/CTGP7-UpdateTool/issues"))

    def openBrowserGameBanana(self):
        QDesktopServices.openUrl(QUrl("https://gamebanana.com/mods/50221"))

    def openDiscord(self):
        QDesktopServices.openUrl(QUrl(self.HELP_DISCORD_LINK))

    def quitApp(self):
        self.close()

    def featureNotImplemented(self):
        QMessageBox.warning(self, "Feature not implemented","This feature is not available at the moment. Check again later.")

    def connectSignalsSlots(self):
        self.sdBrowseButton.clicked.connect(self.selectSDDirectory)
        self.sdDetectButton.clicked.connect(self.scanForNintendo3DSSD)
        self.sdRootText.textChanged.connect(lambda s: self.applySDFolder(s))
        self.actionAboutThisApp.triggered.connect(self.showHelpDialog)
        self.installButton.clicked.connect(self.installButtonPress)
        self.updateButton.clicked.connect(self.updateButtonPress)
        self.actionInstallMod.triggered.connect(self.installButtonPress)
        self.actionUpdateMod.triggered.connect(self.updateButtonPress)
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
            msg.setWindowTitle("Warning")
            msg.addButton(QMessageBox.Ok)
            msg.setText("The installer worker is currently running. Please stop the worker by pressing the 'Cancel' button before closing this window.")
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
                msg.setWindowTitle("Warning")
                msg.addButton(QMessageBox.Yes)
                msg.addButton(QMessageBox.No)
                msg.addButton(QMessageBox.Retry)
                msg.setDefaultButton(QMessageBox.No)
                msg.setText("Could not deinitialize in time.\n\nDo you want to quit the app?")
                msg.setInformativeText("This may result in unsaved changes if you quit now.")
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