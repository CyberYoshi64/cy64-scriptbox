# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainlXfomN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.9
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 160)
        MainWindow.setMinimumSize(QSize(400, 160))
        self.actionDummy = QAction(MainWindow)
        self.actionDummy.setObjectName(u"actionDummy")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setTextFormat(Qt.MarkdownText)
        self.label.setMargin(4)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.testBut1 = QCommandLinkButton(self.centralwidget)
        self.testBut1.setObjectName(u"testBut1")
        sizePolicy.setHeightForWidth(self.testBut1.sizePolicy().hasHeightForWidth())
        self.testBut1.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.testBut1)

        self.testBut2 = QCommandLinkButton(self.centralwidget)
        self.testBut2.setObjectName(u"testBut2")
        sizePolicy.setHeightForWidth(self.testBut2.sizePolicy().hasHeightForWidth())
        self.testBut2.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.testBut2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 27))
        self.menuDummy = QMenu(self.menubar)
        self.menuDummy.setObjectName(u"menuDummy")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuDummy.menuAction())
        self.menuDummy.addAction(self.actionDummy)
        self.menuDummy.addSeparator()
        self.menuDummy.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionDummy.setText(QCoreApplication.translate("MainWindow", u"Dummy", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"### This is a sample window\n"
"Here's some buttons, click 'em!", None))
        self.testBut1.setText(QCoreApplication.translate("MainWindow", u"Test Button 1", None))
        self.testBut2.setText(QCoreApplication.translate("MainWindow", u"Test Button 2", None))
        self.menuDummy.setTitle(QCoreApplication.translate("MainWindow", u"Dummy", None))
    # retranslateUi
