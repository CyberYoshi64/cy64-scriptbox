# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editMiiVeqAUK.ui'
##
## Created by: Qt User Interface Compiler version 5.15.11
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(576, 468)
        Dialog.setMinimumSize(QSize(576, 0))
        Dialog.setMaximumSize(QSize(800, 640))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(36, 44, 63, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(54, 66, 94, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(45, 55, 78, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(18, 22, 31, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(24, 29, 42, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        brush7 = QBrush(QColor(175, 88, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush7)
        palette.setBrush(QPalette.Active, QPalette.HighlightedText, brush)
        brush8 = QBrush(QColor(0, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(85, 170, 0, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush10 = QBrush(QColor(255, 255, 255, 128))
        brush10.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush7)
        brush11 = QBrush(QColor(251, 251, 250, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush11)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        brush12 = QBrush(QColor(255, 255, 255, 160))
        brush12.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush12)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush12)
        brush13 = QBrush(QColor(255, 255, 255, 192))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush12)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        brush14 = QBrush(QColor(91, 66, 22, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush14)
        palette.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush12)
        brush15 = QBrush(QColor(0, 170, 255, 160))
        brush15.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush15)
        brush16 = QBrush(QColor(85, 170, 0, 160))
        brush16.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush16)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        brush17 = QBrush(QColor(161, 161, 161, 255))
        brush17.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush17)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        Dialog.setPalette(palette)
        font = QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.editMiiAuthor = QLineEdit(Dialog)
        self.editMiiAuthor.setObjectName(u"editMiiAuthor")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editMiiAuthor.sizePolicy().hasHeightForWidth())
        self.editMiiAuthor.setSizePolicy(sizePolicy)
        self.editMiiAuthor.setMaxLength(10)

        self.gridLayout.addWidget(self.editMiiAuthor, 10, 1, 1, 2)

        self.line_4 = QFrame(Dialog)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_4, 11, 1, 1, 2)

        self.lblMiiDate = QLabel(Dialog)
        self.lblMiiDate.setObjectName(u"lblMiiDate")

        self.gridLayout.addWidget(self.lblMiiDate, 7, 0, 2, 1)

        self.miscSharable = QCheckBox(Dialog)
        self.miscSharable.setObjectName(u"miscSharable")

        self.gridLayout.addWidget(self.miscSharable, 13, 1, 1, 1)

        self.lblRegionLock = QLabel(Dialog)
        self.lblRegionLock.setObjectName(u"lblRegionLock")

        self.gridLayout.addWidget(self.lblRegionLock, 21, 0, 1, 1)

        self.horizontalWidget = QWidget(Dialog)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 4, 0, 4)
        self.btnImport = QPushButton(self.horizontalWidget)
        self.btnImport.setObjectName(u"btnImport")

        self.horizontalLayout.addWidget(self.btnImport)

        self.btnExport = QPushButton(self.horizontalWidget)
        self.btnExport.setObjectName(u"btnExport")

        self.horizontalLayout.addWidget(self.btnExport)


        self.gridLayout.addWidget(self.horizontalWidget, 26, 0, 1, 3)

        self.lblCharset = QLabel(Dialog)
        self.lblCharset.setObjectName(u"lblCharset")

        self.gridLayout.addWidget(self.lblCharset, 18, 0, 1, 1)

        self.lblMiiAuthor = QLabel(Dialog)
        self.lblMiiAuthor.setObjectName(u"lblMiiAuthor")

        self.gridLayout.addWidget(self.lblMiiAuthor, 10, 0, 1, 1)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 12))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 24, 0, 1, 3)

        self.editMiiName = QLineEdit(Dialog)
        self.editMiiName.setObjectName(u"editMiiName")
        sizePolicy.setHeightForWidth(self.editMiiName.sizePolicy().hasHeightForWidth())
        self.editMiiName.setSizePolicy(sizePolicy)
        self.editMiiName.setMaxLength(10)

        self.gridLayout.addWidget(self.editMiiName, 3, 1, 1, 2)

        self.line_3 = QFrame(Dialog)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_3, 9, 1, 1, 2)

        self.lblMiiDateHR = QLabel(Dialog)
        self.lblMiiDateHR.setObjectName(u"lblMiiDateHR")
        self.lblMiiDateHR.setMinimumSize(QSize(0, 16))
        self.lblMiiDateHR.setMaximumSize(QSize(16777215, 24))
        font1 = QFont()
        font1.setPointSize(8)
        self.lblMiiDateHR.setFont(font1)

        self.gridLayout.addWidget(self.lblMiiDateHR, 8, 1, 1, 2)

        self.lblMiiName = QLabel(Dialog)
        self.lblMiiName.setObjectName(u"lblMiiName")

        self.gridLayout.addWidget(self.lblMiiName, 3, 0, 1, 1)

        self.boxCharset = QComboBox(Dialog)
        self.boxCharset.addItem("")
        self.boxCharset.addItem("")
        self.boxCharset.addItem("")
        self.boxCharset.addItem("")
        self.boxCharset.setObjectName(u"boxCharset")

        self.gridLayout.addWidget(self.boxCharset, 18, 1, 1, 2)

        self.warnFrame = QFrame(Dialog)
        self.warnFrame.setObjectName(u"warnFrame")
        sizePolicy.setHeightForWidth(self.warnFrame.sizePolicy().hasHeightForWidth())
        self.warnFrame.setSizePolicy(sizePolicy)
        self.warnFrame.setMinimumSize(QSize(0, 48))
        self.warnFrame.setMaximumSize(QSize(16777215, 48))
        self.warnFrame.setStyleSheet(u"background: #630; border-radius: 12px; color: white")
        self.verticalLayout = QVBoxLayout(self.warnFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(8, 4, 8, 4)
        self.warning = QLabel(self.warnFrame)
        self.warning.setObjectName(u"warning")
        self.warning.setWordWrap(True)
        self.warning.setIndent(0)

        self.verticalLayout.addWidget(self.warning)


        self.gridLayout.addWidget(self.warnFrame, 1, 0, 1, 3)

        self.line_5 = QFrame(Dialog)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_5, 17, 1, 1, 2)

        self.boxRegionLock = QComboBox(Dialog)
        self.boxRegionLock.addItem("")
        self.boxRegionLock.addItem("")
        self.boxRegionLock.addItem("")
        self.boxRegionLock.addItem("")
        self.boxRegionLock.setObjectName(u"boxRegionLock")

        self.gridLayout.addWidget(self.boxRegionLock, 21, 1, 1, 2)

        self.line_6 = QFrame(Dialog)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_6, 19, 1, 1, 2)

        self.lblMisc = QLabel(Dialog)
        self.lblMisc.setObjectName(u"lblMisc")

        self.gridLayout.addWidget(self.lblMisc, 13, 0, 2, 1)

        self.miscCopyable = QCheckBox(Dialog)
        self.miscCopyable.setObjectName(u"miscCopyable")

        self.gridLayout.addWidget(self.miscCopyable, 13, 2, 1, 1)

        self.line_2 = QFrame(Dialog)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 5, 1, 1, 2)

        self.miscSpecial = QCheckBox(Dialog)
        self.miscSpecial.setObjectName(u"miscSpecial")

        self.gridLayout.addWidget(self.miscSpecial, 14, 1, 1, 1)

        self.horizontalWidget_2 = QWidget(Dialog)
        self.horizontalWidget_2.setObjectName(u"horizontalWidget_2")
        sizePolicy1.setHeightForWidth(self.horizontalWidget_2.sizePolicy().hasHeightForWidth())
        self.horizontalWidget_2.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 4, 0, 4)
        self.btnApply = QPushButton(self.horizontalWidget_2)
        self.btnApply.setObjectName(u"btnApply")

        self.horizontalLayout_2.addWidget(self.btnApply)

        self.btnDiscard = QPushButton(self.horizontalWidget_2)
        self.btnDiscard.setObjectName(u"btnDiscard")

        self.horizontalLayout_2.addWidget(self.btnDiscard)

        self.btnDiscard.raise_()
        self.btnApply.raise_()

        self.gridLayout.addWidget(self.horizontalWidget_2, 27, 0, 1, 3)

        self.editMiiDate = QSpinBox(Dialog)
        self.editMiiDate.setObjectName(u"editMiiDate")
        self.editMiiDate.setMaximum(268435455)

        self.gridLayout.addWidget(self.editMiiDate, 7, 1, 1, 2)

#if QT_CONFIG(shortcut)
        self.lblMiiDate.setBuddy(self.editMiiDate)
        self.lblRegionLock.setBuddy(self.boxRegionLock)
        self.lblCharset.setBuddy(self.boxCharset)
        self.lblMiiAuthor.setBuddy(self.editMiiAuthor)
        self.lblMiiName.setBuddy(self.editMiiName)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.editMiiName, self.editMiiDate)
        QWidget.setTabOrder(self.editMiiDate, self.editMiiAuthor)
        QWidget.setTabOrder(self.editMiiAuthor, self.miscSharable)
        QWidget.setTabOrder(self.miscSharable, self.miscCopyable)
        QWidget.setTabOrder(self.miscCopyable, self.miscSpecial)
        QWidget.setTabOrder(self.miscSpecial, self.boxCharset)
        QWidget.setTabOrder(self.boxCharset, self.boxRegionLock)
        QWidget.setTabOrder(self.boxRegionLock, self.btnImport)
        QWidget.setTabOrder(self.btnImport, self.btnExport)
        QWidget.setTabOrder(self.btnExport, self.btnApply)
        QWidget.setTabOrder(self.btnApply, self.btnDiscard)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Edit Mii Data", None))
        self.editMiiAuthor.setPlaceholderText(QCoreApplication.translate("Dialog", u"The author name is empty\u2026", None))
        self.lblMiiDate.setText(QCoreApplication.translate("Dialog", u"Mii Creation Date", None))
        self.miscSharable.setText(QCoreApplication.translate("Dialog", u"Sharable", None))
#if QT_CONFIG(shortcut)
        self.miscSharable.setShortcut(QCoreApplication.translate("Dialog", u"Alt+1", None))
#endif // QT_CONFIG(shortcut)
        self.lblRegionLock.setText(QCoreApplication.translate("Dialog", u"Region lock", None))
        self.btnImport.setText(QCoreApplication.translate("Dialog", u"&Import Mii ...", None))
        self.btnExport.setText(QCoreApplication.translate("Dialog", u"E&xport Mii ...", None))
        self.lblCharset.setText(QCoreApplication.translate("Dialog", u"Character set", None))
        self.lblMiiAuthor.setText(QCoreApplication.translate("Dialog", u"Mii Author Name", None))
        self.editMiiName.setPlaceholderText(QCoreApplication.translate("Dialog", u"The Mii must have a name!", None))
        self.lblMiiDateHR.setText(QCoreApplication.translate("Dialog", u"Human-readable: 2010/1/1, 0:00:00", None))
        self.lblMiiName.setText(QCoreApplication.translate("Dialog", u"Mii Name", None))
        self.boxCharset.setItemText(0, QCoreApplication.translate("Dialog", u"JPN + USA + EUR", None))
        self.boxCharset.setItemText(1, QCoreApplication.translate("Dialog", u"CHN", None))
        self.boxCharset.setItemText(2, QCoreApplication.translate("Dialog", u"KOR", None))
        self.boxCharset.setItemText(3, QCoreApplication.translate("Dialog", u"TWN", None))

        self.warning.setText(QCoreApplication.translate("Dialog", u"<b>Warning: </b>Properties, like Mii facial data cannot be modified and thus have been excluded.", None))
        self.boxRegionLock.setItemText(0, QCoreApplication.translate("Dialog", u"Region-free", None))
        self.boxRegionLock.setItemText(1, QCoreApplication.translate("Dialog", u"Japan only", None))
        self.boxRegionLock.setItemText(2, QCoreApplication.translate("Dialog", u"America only", None))
        self.boxRegionLock.setItemText(3, QCoreApplication.translate("Dialog", u"Europe only", None))

        self.lblMisc.setText(QCoreApplication.translate("Dialog", u"Miscellaneous flags", None))
        self.miscCopyable.setText(QCoreApplication.translate("Dialog", u"Copyable", None))
#if QT_CONFIG(shortcut)
        self.miscCopyable.setShortcut(QCoreApplication.translate("Dialog", u"Alt+2", None))
#endif // QT_CONFIG(shortcut)
        self.miscSpecial.setText(QCoreApplication.translate("Dialog", u"Special", None))
#if QT_CONFIG(shortcut)
        self.miscSpecial.setShortcut(QCoreApplication.translate("Dialog", u"Alt+3", None))
#endif // QT_CONFIG(shortcut)
        self.btnApply.setText(QCoreApplication.translate("Dialog", u"&Apply changes", None))
        self.btnDiscard.setText(QCoreApplication.translate("Dialog", u"&Close && Discard", None))
    # retranslateUi

