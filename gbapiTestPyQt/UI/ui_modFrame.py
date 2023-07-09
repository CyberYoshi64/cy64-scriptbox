# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modFrameBHMCzU.ui'
##
## Created by: Qt User Interface Compiler version 5.15.10
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(440, 84)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Frame.sizePolicy().hasHeightForWidth())
        Frame.setSizePolicy(sizePolicy)
        Frame.setMinimumSize(QSize(440, 84))
        Frame.setFrameShape(QFrame.StyledPanel)
        Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(Frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.vl1 = QVBoxLayout()
        self.vl1.setSpacing(0)
        self.vl1.setObjectName(u"vl1")
        self.modTitle = QLabel(Frame)
        self.modTitle.setObjectName(u"modTitle")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.modTitle.sizePolicy().hasHeightForWidth())
        self.modTitle.setSizePolicy(sizePolicy1)
        self.modTitle.setMinimumSize(QSize(0, 26))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.modTitle.setFont(font)

        self.vl1.addWidget(self.modTitle)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.modDesc2 = QLabel(Frame)
        self.modDesc2.setObjectName(u"modDesc2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.modDesc2.sizePolicy().hasHeightForWidth())
        self.modDesc2.setSizePolicy(sizePolicy2)
        self.modDesc2.setMinimumSize(QSize(100, 0))
        self.modDesc2.setMaximumSize(QSize(100, 16777215))
        font1 = QFont()
        font1.setPointSize(8)
        self.modDesc2.setFont(font1)

        self.gridLayout.addWidget(self.modDesc2, 1, 0, 1, 1)

        self.modDesc1 = QLabel(Frame)
        self.modDesc1.setObjectName(u"modDesc1")
        sizePolicy2.setHeightForWidth(self.modDesc1.sizePolicy().hasHeightForWidth())
        self.modDesc1.setSizePolicy(sizePolicy2)
        self.modDesc1.setMinimumSize(QSize(100, 0))
        self.modDesc1.setMaximumSize(QSize(100, 16777215))
        self.modDesc1.setFont(font1)

        self.gridLayout.addWidget(self.modDesc1, 0, 0, 1, 1)

        self.label_5 = QLabel(Frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)

        self.label_6 = QLabel(Frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.gridLayout.addWidget(self.label_6, 1, 1, 1, 1)

        self.label = QLabel(Frame)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.label_3 = QLabel(Frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)


        self.vl1.addLayout(self.gridLayout)


        self.horizontalLayout.addLayout(self.vl1)

        self.vl2 = QVBoxLayout()
        self.vl2.setSpacing(0)
        self.vl2.setObjectName(u"vl2")
        self.vs1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vl2.addItem(self.vs1)

        self.btnDetails = QPushButton(Frame)
        self.btnDetails.setObjectName(u"btnDetails")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btnDetails.sizePolicy().hasHeightForWidth())
        self.btnDetails.setSizePolicy(sizePolicy3)
        self.btnDetails.setMinimumSize(QSize(144, 0))

        self.vl2.addWidget(self.btnDetails)

        self.btnDownload = QPushButton(Frame)
        self.btnDownload.setObjectName(u"btnDownload")
        sizePolicy3.setHeightForWidth(self.btnDownload.sizePolicy().hasHeightForWidth())
        self.btnDownload.setSizePolicy(sizePolicy3)
        self.btnDownload.setMinimumSize(QSize(144, 0))

        self.vl2.addWidget(self.btnDownload)

        self.vs2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vl2.addItem(self.vs2)


        self.horizontalLayout.addLayout(self.vl2)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.modTitle.setText(QCoreApplication.translate("Frame", u"Unknown Mod", None))
        self.modDesc2.setText(QCoreApplication.translate("Frame", u"Download", None))
        self.modDesc1.setText(QCoreApplication.translate("Frame", u"Creator", None))
        self.label_5.setText(QCoreApplication.translate("Frame", u"Unknown", None))
        self.label_6.setText(QCoreApplication.translate("Frame", u"0", None))
        self.label.setText(QCoreApplication.translate("Frame", u"Likes", None))
        self.label_3.setText(QCoreApplication.translate("Frame", u"0", None))
        self.btnDetails.setText(QCoreApplication.translate("Frame", u"View details", None))
        self.btnDownload.setText(QCoreApplication.translate("Frame", u"Download mod", None))
    # retranslateUi

