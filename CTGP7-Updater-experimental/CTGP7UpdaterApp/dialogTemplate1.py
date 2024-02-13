from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from UI.ui_threadedDialog import Ui_Dialog as UiDlg

class ThreadedDialog:
    class RunSignals(QObject):
        progress = Signal(type)
        title = Signal(type)
        text = Signal(type)
        detailedText = Signal(bool, type)
        size = Signal(type)
        minsize = Signal(type)
        buttons = Signal(type)
        closed = Signal()

    class Signals(QObject):
        closed = Signal(type)
        closed2 = Signal()

    class Dialog(QDialog, UiDlg):
        def __init__(self, parent=None):
            super().__init__(parent)
            self.closed = False
            self.setupUi(self)
            self.signals = ThreadedDialog.Signals()

        @Slot()
        def _setTitle(self, s):
            if self.closed: self.signals.closed2.emit()
            self.setWindowTitle(str(s))

        @Slot()
        def _setSize(self, s):
            if self.closed: self.signals.closed2.emit()
            self.setFixedSize(s)

        @Slot()
        def _setMinSize(self, s):
            if self.closed: self.signals.closed2.emit()
            self.setMinimumSize(s)

        @Slot()
        def _setText(self, s):
            if not self.text or self.closed:
                self.signals.closed2.emit()
                return
            if isinstance(s, Qt.TextFormat):
                self.text.setTextFormat(s)
            elif str(s)=="":
                self.text.setText("")
                self.text.setHidden(True)
            else:
                self.text.setHidden(False)
                self.text.setText(str(s))

        @Slot()
        def _setDetailedText(self, append, s):
            if not self.detailedText or self.closed:
                self.signals.closed2.emit()
                return
            if isinstance(s,Qt.TextFormat):
                self.detailedText.setTextFormat(s)
            else:
                self.scrollArea.setHidden(False)
                if append: self.detailedText.setText(self.detailedText.text() + str(s))
                else: self.detailedText.setText(str(s))

        @Slot()
        def _setProgress(self, p):
            if not self.progBar or self.closed:
                self.signals.closed2.emit()
                return
            if type(p)==bool:
                self.progBar.setHidden(not p)
            else:
                self.progBar.setHidden(False)
                self.progBar.setEnabled(p>=0)
                if p >= 0: self.progBar.setValue(p)

        @Slot()
        def _setButtons(self, m):
            if not self.buttonBox or self.closed:
                self.signals.closed2.emit()
                return
            if m == None:
                self.buttonBox.setHidden(True)
            else:
                self.buttonBox.setHidden(False)
                self.buttonBox.setStandardButtons(m)

        def accept(self) -> None: self.onClose()
        def reject(self) -> None: self.onClose()

        def closeEvent(self, arg__1: QCloseEvent) -> None:
            self.onClose()
            arg__1.accept()

        @Slot()
        def onClose(self):
            if self.closed: return
            self.signals.closed.emit(self)
            self.signals.closed2.emit()
            self.closed = True
