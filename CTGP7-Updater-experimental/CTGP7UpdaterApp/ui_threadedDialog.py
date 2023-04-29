# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog1zmYdmS.ui'
##
## Created by: Qt User Interface Compiler version 5.15.9
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
        Dialog.setMinimumSize(QSize(400, 0))
        Dialog.setMaximumSize(QSize(1000, 600))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.text = QLabel(Dialog)
        self.text.setObjectName(u"text")
        self.text.setMargin(4)
        self.text.setWordWrap(True)

        self.verticalLayout.addWidget(self.text)

        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 304, 71))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.detailedText = QLabel(self.scrollAreaWidgetContents)
        self.detailedText.setObjectName(u"detailedText")
        self.detailedText.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.detailedText.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.detailedText)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.progBar = QProgressBar(Dialog)
        self.progBar.setObjectName(u"progBar")
        self.progBar.setValue(0)
        self.progBar.setTextVisible(False)

        self.verticalLayout.addWidget(self.progBar)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.text.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.detailedText.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
    # retranslateUi

