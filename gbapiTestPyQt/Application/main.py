import sys, os, shutil, ctypes

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from Application.constants import CONSTANT as const
import Application.utils as utils

from UI.ui_main import Ui_MainWindow
from Application.dialogTemplate1 import ThreadedDialog
from Application.mainLogic import CTGP7Updater

class Window(QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):
        self.isInit = True
        super().__init__(parent)
        self.setupUi(self)
        self.threadPool = QThreadPool()
        self.isInit = False

    def closeEvent(self, event: QCloseEvent) -> None:
        i = 0
        
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
                msg.setText("Some background tasks are not responding. Are you sure to exit the app?")
                btn = msg.exec_()
                if (btn == QMessageBox.No):
                    event.ignore()
                    return
                elif (btn == QMessageBox.Yes):
                    break
        event.accept()
def startApp():
    app = QApplication(sys.argv)
    win = Window()
    try:
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(u"ctgp7.ctgp7.installer.1_1") # So that the taskbar shows the window icon on windows
    except:
        pass
    win.show()
    sys.exit(app.exec_())