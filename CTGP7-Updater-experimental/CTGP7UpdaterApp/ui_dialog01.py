# -*- coding: utf-8 -*-

################################################################################
## Created by: Qt User Interface Compiler version 5.15.9
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore

class Ui_Dialog(object):
    @staticmethod
    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"Dialog")
        self.resize(512, 280)
        self.setMinimumSize(QSize(512, 280))
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setMargin(8)
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sdList = QListWidget(self)
        self.sdList.setObjectName(u"sdList")
        self.horizontalLayout.addWidget(self.sdList)
        self.buttons = QDialogButtonBox(self)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setOrientation(Qt.Vertical)
        self.buttons.setStandardButtons(QDialogButtonBox.Close|QDialogButtonBox.Open)
        self.buttons.setCenterButtons(True)
        self.horizontalLayout.addWidget(self.buttons)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)

        QMetaObject.connectSlotsByName(self)
    # setupUi
