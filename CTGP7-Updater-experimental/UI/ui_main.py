# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main-experimentFLeXOG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.10
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore

from . import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 200)
        MainWindow.setMinimumSize(QSize(512, 200))
        MainWindow.setMaximumSize(QSize(720, 240))
        icon = QIcon()
        icon.addFile(u":/images/window_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QSize(24, 24))
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionIntegChk = QAction(MainWindow)
        self.actionIntegChk.setObjectName(u"actionIntegChk")
        self.actionInstallMod = QAction(MainWindow)
        self.actionInstallMod.setObjectName(u"actionInstallMod")
        self.actionUpdateMod = QAction(MainWindow)
        self.actionUpdateMod.setObjectName(u"actionUpdateMod")
        self.actionAboutThisApp = QAction(MainWindow)
        self.actionAboutThisApp.setObjectName(u"actionAboutThisApp")
        self.actionHelpGamebanana = QAction(MainWindow)
        self.actionHelpGamebanana.setObjectName(u"actionHelpGamebanana")
        self.actionHelpGitHub = QAction(MainWindow)
        self.actionHelpGitHub.setObjectName(u"actionHelpGitHub")
        self.actionShowChangelog = QAction(MainWindow)
        self.actionShowChangelog.setObjectName(u"actionShowChangelog")
        self.actionAboutQt = QAction(MainWindow)
        self.actionAboutQt.setObjectName(u"actionAboutQt")
        self.actionHelpDiscord = QAction(MainWindow)
        self.actionHelpDiscord.setObjectName(u"actionHelpDiscord")
        self.actionUninstall = QAction(MainWindow)
        self.actionUninstall.setObjectName(u"actionUninstall")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(8, 8, 8, 8)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setTextFormat(Qt.AutoText)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.sdRootText = QLineEdit(self.centralwidget)
        self.sdRootText.setObjectName(u"sdRootText")
        self.sdRootText.setMinimumSize(QSize(256, 0))
        self.sdRootText.setMaxLength(512)
        self.sdRootText.setFrame(True)
        self.sdRootText.setClearButtonEnabled(False)

        self.horizontalLayout_2.addWidget(self.sdRootText)

        self.sdBrowseButton = QPushButton(self.centralwidget)
        self.sdBrowseButton.setObjectName(u"sdBrowseButton")

        self.horizontalLayout_2.addWidget(self.sdBrowseButton)

        self.sdDetectButton = QPushButton(self.centralwidget)
        self.sdDetectButton.setObjectName(u"sdDetectButton")

        self.horizontalLayout_2.addWidget(self.sdDetectButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.miscInfoLabel = QLabel(self.centralwidget)
        self.miscInfoLabel.setObjectName(u"miscInfoLabel")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.miscInfoLabel.setFont(font)
        self.miscInfoLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.miscInfoLabel)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer_7 = QSpacerItem(64, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.installButton = QPushButton(self.centralwidget)
        self.installButton.setObjectName(u"installButton")
        self.installButton.setMinimumSize(QSize(0, 40))
        self.installButton.setFont(font)

        self.horizontalLayout_4.addWidget(self.installButton)

        self.updateButton = QPushButton(self.centralwidget)
        self.updateButton.setObjectName(u"updateButton")
        self.updateButton.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.updateButton.sizePolicy().hasHeightForWidth())
        self.updateButton.setSizePolicy(sizePolicy)
        self.updateButton.setMinimumSize(QSize(0, 40))
        self.updateButton.setFont(font)

        self.horizontalLayout_4.addWidget(self.updateButton)

        self.horizontalSpacer_8 = QSpacerItem(64, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.progressInfoLabel = QLabel(self.centralwidget)
        self.progressInfoLabel.setObjectName(u"progressInfoLabel")
        self.progressInfoLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.progressInfoLabel)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 24))
        self.progressBar.setValue(0)

        self.verticalLayout.addWidget(self.progressBar)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 640, 27))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuExperimental = QMenu(self.menuBar)
        self.menuExperimental.setObjectName(u"menuExperimental")
        self.menuAbout = QMenu(self.menuBar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuGetHelp = QMenu(self.menuAbout)
        self.menuGetHelp.setObjectName(u"menuGetHelp")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuExperimental.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionInstallMod)
        self.menuFile.addAction(self.actionUpdateMod)
        self.menuFile.addAction(self.actionUninstall)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuExperimental.addAction(self.actionShowChangelog)
        self.menuExperimental.addAction(self.actionIntegChk)
        self.menuAbout.addAction(self.actionAboutThisApp)
        self.menuAbout.addAction(self.actionAboutQt)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.menuGetHelp.menuAction())
        self.menuGetHelp.addAction(self.actionHelpDiscord)
        self.menuGetHelp.addAction(self.actionHelpGamebanana)
        self.menuGetHelp.addAction(self.actionHelpGitHub)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CTGP-7 Installer", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionIntegChk.setText(QCoreApplication.translate("MainWindow", u"Integrity Check", None))
        self.actionInstallMod.setText(QCoreApplication.translate("MainWindow", u"Install", None))
        self.actionUpdateMod.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.actionAboutThisApp.setText(QCoreApplication.translate("MainWindow", u"About this app...", None))
        self.actionHelpGamebanana.setText(QCoreApplication.translate("MainWindow", u"Gamebanana", None))
        self.actionHelpGitHub.setText(QCoreApplication.translate("MainWindow", u"GitHub", None))
        self.actionShowChangelog.setText(QCoreApplication.translate("MainWindow", u"View Changelog", None))
        self.actionAboutQt.setText(QCoreApplication.translate("MainWindow", u"About Qt", None))
        self.actionHelpDiscord.setText(QCoreApplication.translate("MainWindow", u"Discord Server", None))
        self.actionUninstall.setText(QCoreApplication.translate("MainWindow", u"Uninstall", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Target:", None))
        self.sdRootText.setInputMask("")
        self.sdRootText.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Path to 3DS/Citra SD Card", None))
        self.sdBrowseButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.sdDetectButton.setText(QCoreApplication.translate("MainWindow", u"Detect", None))
        self.miscInfoLabel.setText(QCoreApplication.translate("MainWindow", u"[Some information here]", None))
        self.installButton.setText(QCoreApplication.translate("MainWindow", u"Install", None))
        self.updateButton.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.progressInfoLabel.setText(QCoreApplication.translate("MainWindow", u"Progress Info", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuExperimental.setTitle(QCoreApplication.translate("MainWindow", u"Experiments", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuGetHelp.setTitle(QCoreApplication.translate("MainWindow", u"Get help...", None))
    # retranslateUi

