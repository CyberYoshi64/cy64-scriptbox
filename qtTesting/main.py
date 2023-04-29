#!/usr/bin/python3

import os, sys
import PySide2.QtGui

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

import random

from ui_main import Ui_MainWindow as UiMain
from ui_dialog1 import Ui_Dialog as UiDialog1

class Dialog1RunSignals(QObject):
    progress = Signal(type)
    title = Signal(type)
    text = Signal(type)
    detailedText = Signal(bool, type)
    buttons = Signal(type)
    closed = Signal()

class Dialog1Signals(QObject):
    closed = Signal(type)
    closed2 = Signal()

class Dialog1Run(QRunnable, QThread):
    def __init__(self) -> None:
        super().__init__()
        self.closed = False
        self.signals = Dialog1RunSignals()
    
    @Slot()
    def setClosed(self):
        self.closed = True

    @Slot()
    def run(self):
        i = 0.0
        while not self.closed:
            s = ""
            for _ in range(256):
                s += chr(random.randint(32,122) if (not _ or _ % 64) else 10)
            self.signals.text.emit(s)
            s = ""
            for _ in range(64):
                s += chr(random.randint(32,122))
            self.signals.title.emit(s)
            i = (i + 2) % 100
            self.signals.progress.emit(i)
            if (i % 10)==10: self.signals.detailedText.emit(False, i)
            self.sleep(1)
        self.signals.closed.emit()
        

class Dialog1(QDialog, UiDialog1):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.closed = False
        self.setupUi(self)
        self.signals = Dialog1Signals()
    
    @Slot()
    def setTitle(self, s):
        self.setWindowTitle(str(s))
    
    @Slot()
    def setText(self, s):
        if not self.text:
            self.signals.closed2.emit()
            return
        if isinstance(s, Qt.TextFormat):
            self.text.setTextFormat(s)
        else:
            self.text.setText(str(s))
    
    @Slot()
    def setDetailedText(self, append, s):
        if not self.detailedText:
            self.signals.closed2.emit()
            return
        if isinstance(s,Qt.TextFormat):
            self.detailedText.setTextFormat(s)
        else:
            self.scrollArea.setHidden(False)
            if append: self.detailedText.setText(self.detailedText.text() + str(s))
            else: self.detailedText.setText(str(s))
    
    @Slot()
    def setProgress(self, p):
        if not self.progBar:
            self.signals.closed2.emit()
            return
        if type(p)==bool:
            self.progBar.setHidden(p)
        else:
            self.progBar.setHidden(False)
            self.progBar.setEnabled(p>=0)
            if p >= 0: self.progBar.setValue(p)
    
    @Slot()
    def setButtons(self, m):
        if not self.buttonBox:
            self.signals.closed2.emit()
            return
        if m == None:
            self.buttonBox.setHidden(True)
        else:
            self.buttonBox.setHidden(False)
            self.buttonBox.setStandardButtons(m)

    def closeEvent(self, arg__1: QCloseEvent) -> None:
        self.onClose()
        arg__1.accept()

    @Slot()
    def onClose(self):
        if self.closed: return
        self.signals.closed.emit(self)
        self.signals.closed2.emit()
        self.closed = True

class MainApplication(QMainWindow, UiMain):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignals()
        self.threadPool = QThreadPool(self)
        self.threadPool.setMaxThreadCount(20)
        self.windowPool = []
    
    def dialogClose(self, dlg):
        try:
            self.windowPool.remove(dlg)
            dlg.close()
        except Exception as e:
            QMessageBox.information(self, "Error", str(e))

    def spawnDialog(self):
        dlg = Dialog1()
        dlg.scrollArea.setHidden(True)
        dlg.progBar.setHidden(True)
        dlg.buttonBox.setHidden(True)
        thread = Dialog1Run()
        thread.signals.progress.connect(dlg.setProgress)
        thread.signals.title.connect(dlg.setTitle)
        thread.signals.text.connect(dlg.setText)
        thread.signals.detailedText.connect(dlg.setDetailedText)
        thread.signals.buttons.connect(dlg.setButtons)
        thread.signals.closed.connect(dlg.onClose)
        dlg.signals.closed.connect(self.dialogClose)
        dlg.signals.closed2.connect(thread.setClosed)
        self.windowPool.append(dlg)
        dlg.open()
        self.threadPool.start(thread)
    
    def connectSignals(self):
        self.actionExit.triggered.connect(self.close)
        self.testBut1.clicked.connect(self.spawnDialog)
        
    def closeEvent(self, event: QCloseEvent) -> None:
        i = 0
        self.statusBar().showMessage("Closing application; please wait...", 10000)
        while not self.threadPool.waitForDone(500):
            for j in self.windowPool:
                if hasattr(j,"close"):
                    j.close()
                else:
                    self.windowPool.remove(j)
            i+=1
            if not (i % 20):
                msg = QMessageBox(self)
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Warning")
                msg.addButton(QMessageBox.Yes)
                msg.addButton(QMessageBox.No)
                msg.addButton(QMessageBox.Retry)
                msg.setDefaultButton(QMessageBox.No)
                msg.setText("Could not deinitialize in time.\n\nDo you want to quit the app?")
                msg.setDetailedText("This may result in unsaved changes if you quit now.")
                btn = msg.exec_()
                if (btn == QMessageBox.No):
                    event.ignore()
                    return
                elif (btn == QMessageBox.Yes):
                    break
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainApplication()
    win.show()
    sys.exit(app.exec_())