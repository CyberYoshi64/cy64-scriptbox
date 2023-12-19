# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowYELlQY.ui'
##
## Created by: Qt User Interface Compiler version 5.15.11
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(982, 532)
        MainWindow.setMaximumSize(QSize(1172, 800))
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
        MainWindow.setPalette(palette)
        font = QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QFont.PreferAntialias)
        MainWindow.setFont(font)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSaveAs = QAction(MainWindow)
        self.actionSaveAs.setObjectName(u"actionSaveAs")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionDummy1 = QAction(MainWindow)
        self.actionDummy1.setObjectName(u"actionDummy1")
        self.actionAboutThisApp = QAction(MainWindow)
        self.actionAboutThisApp.setObjectName(u"actionAboutThisApp")
        self.actionAboutQt = QAction(MainWindow)
        self.actionAboutQt.setObjectName(u"actionAboutQt")
        self.actionHelpGitHub = QAction(MainWindow)
        self.actionHelpGitHub.setObjectName(u"actionHelpGitHub")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setFont(font)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setFont(font)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_4 = QGridLayout(self.tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.genMisc = QLabel(self.tab)
        self.genMisc.setObjectName(u"genMisc")

        self.gridLayout_4.addWidget(self.genMisc, 9, 1, 1, 1)

        self.line_2 = QFrame(self.tab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(0, 12))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_2, 8, 1, 1, 2)

        self.genCecMeets = QLabel(self.tab)
        self.genCecMeets.setObjectName(u"genCecMeets")

        self.gridLayout_4.addWidget(self.genCecMeets, 4, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 0, 0, 1, 1)

        self.genCoins = QLabel(self.tab)
        self.genCoins.setObjectName(u"genCoins")

        self.gridLayout_4.addWidget(self.genCoins, 3, 1, 1, 1)

        self.genVR = QLabel(self.tab)
        self.genVR.setObjectName(u"genVR")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.genVR.sizePolicy().hasHeightForWidth())
        self.genVR.setSizePolicy(sizePolicy)
        self.genVR.setMinimumSize(QSize(312, 0))
        self.genVR.setMaximumSize(QSize(312, 16777215))

        self.gridLayout_4.addWidget(self.genVR, 0, 1, 1, 1)

        self.genCecComment = QLabel(self.tab)
        self.genCecComment.setObjectName(u"genCecComment")

        self.gridLayout_4.addWidget(self.genCecComment, 5, 1, 1, 1)

        self.genLosses = QLabel(self.tab)
        self.genLosses.setObjectName(u"genLosses")

        self.gridLayout_4.addWidget(self.genLosses, 2, 1, 1, 1)

        self.genWins = QLabel(self.tab)
        self.genWins.setObjectName(u"genWins")

        self.gridLayout_4.addWidget(self.genWins, 1, 1, 1, 1)

        self.genMiiData = QLabel(self.tab)
        self.genMiiData.setObjectName(u"genMiiData")

        self.gridLayout_4.addWidget(self.genMiiData, 6, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_7, 0, 4, 1, 1)

        self.genVRVal = QSpinBox(self.tab)
        self.genVRVal.setObjectName(u"genVRVal")
        self.genVRVal.setMinimumSize(QSize(412, 0))
        self.genVRVal.setMinimum(1)
        self.genVRVal.setMaximum(99999)
        self.genVRVal.setValue(1000)

        self.gridLayout_4.addWidget(self.genVRVal, 0, 2, 1, 1)

        self.genWinsVal = QSpinBox(self.tab)
        self.genWinsVal.setObjectName(u"genWinsVal")
        self.genWinsVal.setMaximum(99999)

        self.gridLayout_4.addWidget(self.genWinsVal, 1, 2, 1, 1)

        self.genLossesVal = QSpinBox(self.tab)
        self.genLossesVal.setObjectName(u"genLossesVal")
        self.genLossesVal.setMaximum(99999)

        self.gridLayout_4.addWidget(self.genLossesVal, 2, 2, 1, 1)

        self.genCoinsVal = QSpinBox(self.tab)
        self.genCoinsVal.setObjectName(u"genCoinsVal")
        self.genCoinsVal.setMaximum(2147483647)

        self.gridLayout_4.addWidget(self.genCoinsVal, 3, 2, 1, 1)

        self.genCecMeetsVal = QSpinBox(self.tab)
        self.genCecMeetsVal.setObjectName(u"genCecMeetsVal")
        self.genCecMeetsVal.setMaximum(2147483647)

        self.gridLayout_4.addWidget(self.genCecMeetsVal, 4, 2, 1, 1)

        self.genCecCommentVal = QLineEdit(self.tab)
        self.genCecCommentVal.setObjectName(u"genCecCommentVal")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.genCecCommentVal.sizePolicy().hasHeightForWidth())
        self.genCecCommentVal.setSizePolicy(sizePolicy1)
        self.genCecCommentVal.setMaxLength(16)

        self.gridLayout_4.addWidget(self.genCecCommentVal, 5, 2, 1, 1)

        self.genMiiDataEdit = QPushButton(self.tab)
        self.genMiiDataEdit.setObjectName(u"genMiiDataEdit")

        self.gridLayout_4.addWidget(self.genMiiDataEdit, 6, 2, 1, 1)

        self.genMaxValueBtn = QCommandLinkButton(self.tab)
        self.genMaxValueBtn.setObjectName(u"genMaxValueBtn")
        self.genMaxValueBtn.setMinimumSize(QSize(0, 40))
        self.genMaxValueBtn.setMaximumSize(QSize(16777215, 48))

        self.gridLayout_4.addWidget(self.genMaxValueBtn, 9, 2, 1, 1)

        self.genResetSaveBtn = QCommandLinkButton(self.tab)
        self.genResetSaveBtn.setObjectName(u"genResetSaveBtn")
        self.genResetSaveBtn.setMinimumSize(QSize(0, 40))
        self.genResetSaveBtn.setMaximumSize(QSize(16777215, 48))

        self.gridLayout_4.addWidget(self.genResetSaveBtn, 10, 2, 1, 1)

        self.genRandomSaveBtn = QCommandLinkButton(self.tab)
        self.genRandomSaveBtn.setObjectName(u"genRandomSaveBtn")
        self.genRandomSaveBtn.setMinimumSize(QSize(0, 40))
        self.genRandomSaveBtn.setMaximumSize(QSize(16777215, 48))

        self.gridLayout_4.addWidget(self.genRandomSaveBtn, 11, 2, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tabUnlocks = QWidget()
        self.tabUnlocks.setObjectName(u"tabUnlocks")
        self.gridLayout_6 = QGridLayout(self.tabUnlocks)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.unlChar = QVBoxLayout()
        self.unlChar.setSpacing(0)
        self.unlChar.setObjectName(u"unlChar")
        self.unlCharLabel = QLabel(self.tabUnlocks)
        self.unlCharLabel.setObjectName(u"unlCharLabel")
        self.unlCharLabel.setMinimumSize(QSize(0, 32))
        font1 = QFont()
        font1.setFamily(u"RodinNTLG2")
        font1.setPointSize(13)
        font1.setBold(False)
        font1.setWeight(50)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.unlCharLabel.setFont(font1)

        self.unlChar.addWidget(self.unlCharLabel)

        self.unlCharList = QListWidget(self.tabUnlocks)
        __qlistwidgetitem = QListWidgetItem(self.unlCharList)
        __qlistwidgetitem.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsEnabled);
        __qlistwidgetitem1 = QListWidgetItem(self.unlCharList)
        __qlistwidgetitem1.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem1.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsEnabled);
        __qlistwidgetitem2 = QListWidgetItem(self.unlCharList)
        __qlistwidgetitem2.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem2.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsEnabled);
        __qlistwidgetitem3 = QListWidgetItem(self.unlCharList)
        __qlistwidgetitem3.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem3.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsEnabled);
        __qlistwidgetitem4 = QListWidgetItem(self.unlCharList)
        __qlistwidgetitem4.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem4.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsEnabled);
        __qlistwidgetitem5 = QListWidgetItem(self.unlCharList)
        __qlistwidgetitem5.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem5.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsEnabled);
        __qlistwidgetitem6 = QListWidgetItem(self.unlCharList)
        __qlistwidgetitem6.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem6.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsEnabled);
        __qlistwidgetitem7 = QListWidgetItem(self.unlCharList)
        __qlistwidgetitem7.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem7.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsEnabled);
        __qlistwidgetitem8 = QListWidgetItem(self.unlCharList)
        __qlistwidgetitem8.setCheckState(Qt.Unchecked);
        __qlistwidgetitem9 = QListWidgetItem(self.unlCharList)
        __qlistwidgetitem9.setCheckState(Qt.Unchecked);
        __qlistwidgetitem10 = QListWidgetItem(self.unlCharList)
        __qlistwidgetitem10.setCheckState(Qt.Unchecked);
        __qlistwidgetitem11 = QListWidgetItem(self.unlCharList)
        __qlistwidgetitem11.setCheckState(Qt.Unchecked);
        __qlistwidgetitem12 = QListWidgetItem(self.unlCharList)
        __qlistwidgetitem12.setCheckState(Qt.Unchecked);
        __qlistwidgetitem13 = QListWidgetItem(self.unlCharList)
        __qlistwidgetitem13.setCheckState(Qt.Unchecked);
        __qlistwidgetitem14 = QListWidgetItem(self.unlCharList)
        __qlistwidgetitem14.setCheckState(Qt.Unchecked);
        __qlistwidgetitem15 = QListWidgetItem(self.unlCharList)
        __qlistwidgetitem15.setCheckState(Qt.Unchecked);
        __qlistwidgetitem16 = QListWidgetItem(self.unlCharList)
        __qlistwidgetitem16.setCheckState(Qt.Unchecked);
        self.unlCharList.setObjectName(u"unlCharList")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.unlCharList.sizePolicy().hasHeightForWidth())
        self.unlCharList.setSizePolicy(sizePolicy2)
        self.unlCharList.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.unlChar.addWidget(self.unlCharList)


        self.gridLayout_6.addLayout(self.unlChar, 1, 0, 1, 1)

        self.unlBody = QVBoxLayout()
        self.unlBody.setSpacing(0)
        self.unlBody.setObjectName(u"unlBody")
        self.unlBodyLabel = QLabel(self.tabUnlocks)
        self.unlBodyLabel.setObjectName(u"unlBodyLabel")
        self.unlBodyLabel.setMinimumSize(QSize(0, 32))
        self.unlBodyLabel.setFont(font1)

        self.unlBody.addWidget(self.unlBodyLabel)

        self.unlBodyList = QListWidget(self.tabUnlocks)
        __qlistwidgetitem17 = QListWidgetItem(self.unlBodyList)
        __qlistwidgetitem17.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem17.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsEnabled);
        __qlistwidgetitem18 = QListWidgetItem(self.unlBodyList)
        __qlistwidgetitem18.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem18.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsEnabled);
        __qlistwidgetitem19 = QListWidgetItem(self.unlBodyList)
        __qlistwidgetitem19.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem19.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsEnabled);
        __qlistwidgetitem20 = QListWidgetItem(self.unlBodyList)
        __qlistwidgetitem20.setCheckState(Qt.Unchecked);
        __qlistwidgetitem21 = QListWidgetItem(self.unlBodyList)
        __qlistwidgetitem21.setCheckState(Qt.Unchecked);
        __qlistwidgetitem22 = QListWidgetItem(self.unlBodyList)
        __qlistwidgetitem22.setCheckState(Qt.Unchecked);
        __qlistwidgetitem23 = QListWidgetItem(self.unlBodyList)
        __qlistwidgetitem23.setCheckState(Qt.Unchecked);
        __qlistwidgetitem24 = QListWidgetItem(self.unlBodyList)
        __qlistwidgetitem24.setCheckState(Qt.Unchecked);
        __qlistwidgetitem25 = QListWidgetItem(self.unlBodyList)
        __qlistwidgetitem25.setCheckState(Qt.Unchecked);
        __qlistwidgetitem26 = QListWidgetItem(self.unlBodyList)
        __qlistwidgetitem26.setCheckState(Qt.Unchecked);
        __qlistwidgetitem27 = QListWidgetItem(self.unlBodyList)
        __qlistwidgetitem27.setCheckState(Qt.Unchecked);
        __qlistwidgetitem28 = QListWidgetItem(self.unlBodyList)
        __qlistwidgetitem28.setCheckState(Qt.Unchecked);
        __qlistwidgetitem29 = QListWidgetItem(self.unlBodyList)
        __qlistwidgetitem29.setCheckState(Qt.Unchecked);
        __qlistwidgetitem30 = QListWidgetItem(self.unlBodyList)
        __qlistwidgetitem30.setCheckState(Qt.Unchecked);
        __qlistwidgetitem31 = QListWidgetItem(self.unlBodyList)
        __qlistwidgetitem31.setCheckState(Qt.Unchecked);
        __qlistwidgetitem32 = QListWidgetItem(self.unlBodyList)
        __qlistwidgetitem32.setCheckState(Qt.Unchecked);
        __qlistwidgetitem33 = QListWidgetItem(self.unlBodyList)
        __qlistwidgetitem33.setCheckState(Qt.Unchecked);
        self.unlBodyList.setObjectName(u"unlBodyList")
        sizePolicy2.setHeightForWidth(self.unlBodyList.sizePolicy().hasHeightForWidth())
        self.unlBodyList.setSizePolicy(sizePolicy2)
        self.unlBodyList.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.unlBody.addWidget(self.unlBodyList)


        self.gridLayout_6.addLayout(self.unlBody, 1, 1, 1, 1)

        self.unlTire = QVBoxLayout()
        self.unlTire.setSpacing(0)
        self.unlTire.setObjectName(u"unlTire")
        self.unlTireLabel = QLabel(self.tabUnlocks)
        self.unlTireLabel.setObjectName(u"unlTireLabel")
        self.unlTireLabel.setMinimumSize(QSize(0, 32))
        self.unlTireLabel.setFont(font1)

        self.unlTire.addWidget(self.unlTireLabel)

        self.unlTireList = QListWidget(self.tabUnlocks)
        __qlistwidgetitem34 = QListWidgetItem(self.unlTireList)
        __qlistwidgetitem34.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem34.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsEnabled);
        __qlistwidgetitem35 = QListWidgetItem(self.unlTireList)
        __qlistwidgetitem35.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem35.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsEnabled);
        __qlistwidgetitem36 = QListWidgetItem(self.unlTireList)
        __qlistwidgetitem36.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem36.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsEnabled);
        __qlistwidgetitem37 = QListWidgetItem(self.unlTireList)
        __qlistwidgetitem37.setCheckState(Qt.Unchecked);
        __qlistwidgetitem38 = QListWidgetItem(self.unlTireList)
        __qlistwidgetitem38.setCheckState(Qt.Unchecked);
        __qlistwidgetitem39 = QListWidgetItem(self.unlTireList)
        __qlistwidgetitem39.setCheckState(Qt.Unchecked);
        __qlistwidgetitem40 = QListWidgetItem(self.unlTireList)
        __qlistwidgetitem40.setCheckState(Qt.Unchecked);
        __qlistwidgetitem41 = QListWidgetItem(self.unlTireList)
        __qlistwidgetitem41.setCheckState(Qt.Unchecked);
        __qlistwidgetitem42 = QListWidgetItem(self.unlTireList)
        __qlistwidgetitem42.setCheckState(Qt.Unchecked);
        __qlistwidgetitem43 = QListWidgetItem(self.unlTireList)
        __qlistwidgetitem43.setCheckState(Qt.Unchecked);
        self.unlTireList.setObjectName(u"unlTireList")
        sizePolicy2.setHeightForWidth(self.unlTireList.sizePolicy().hasHeightForWidth())
        self.unlTireList.setSizePolicy(sizePolicy2)
        self.unlTireList.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.unlTire.addWidget(self.unlTireList)


        self.gridLayout_6.addLayout(self.unlTire, 1, 2, 1, 1)

        self.unlGlider = QVBoxLayout()
        self.unlGlider.setSpacing(0)
        self.unlGlider.setObjectName(u"unlGlider")
        self.unlGliderLabel = QLabel(self.tabUnlocks)
        self.unlGliderLabel.setObjectName(u"unlGliderLabel")
        self.unlGliderLabel.setMinimumSize(QSize(0, 32))
        self.unlGliderLabel.setFont(font1)

        self.unlGlider.addWidget(self.unlGliderLabel)

        self.unlGliderList = QListWidget(self.tabUnlocks)
        __qlistwidgetitem44 = QListWidgetItem(self.unlGliderList)
        __qlistwidgetitem44.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem44.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsEnabled);
        __qlistwidgetitem45 = QListWidgetItem(self.unlGliderList)
        __qlistwidgetitem45.setCheckState(Qt.Unchecked);
        __qlistwidgetitem46 = QListWidgetItem(self.unlGliderList)
        __qlistwidgetitem46.setCheckState(Qt.Unchecked);
        __qlistwidgetitem47 = QListWidgetItem(self.unlGliderList)
        __qlistwidgetitem47.setCheckState(Qt.Unchecked);
        __qlistwidgetitem48 = QListWidgetItem(self.unlGliderList)
        __qlistwidgetitem48.setCheckState(Qt.Unchecked);
        __qlistwidgetitem49 = QListWidgetItem(self.unlGliderList)
        __qlistwidgetitem49.setCheckState(Qt.Unchecked);
        __qlistwidgetitem50 = QListWidgetItem(self.unlGliderList)
        __qlistwidgetitem50.setCheckState(Qt.Unchecked);
        self.unlGliderList.setObjectName(u"unlGliderList")
        sizePolicy2.setHeightForWidth(self.unlGliderList.sizePolicy().hasHeightForWidth())
        self.unlGliderList.setSizePolicy(sizePolicy2)
        self.unlGliderList.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.unlGlider.addWidget(self.unlGliderList)


        self.gridLayout_6.addLayout(self.unlGlider, 1, 3, 1, 1)

        self.label_8 = QLabel(self.tabUnlocks)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 32))
        self.label_8.setMargin(4)

        self.gridLayout_6.addWidget(self.label_8, 0, 0, 1, 4)

        self.tabWidget.addTab(self.tabUnlocks, "")
        self.tabGP = QWidget()
        self.tabGP.setObjectName(u"tabGP")
        self.gridLayout = QGridLayout(self.tabGP)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget = QWidget(self.tabGP)
        self.widget.setObjectName(u"widget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy3)
        self.cupHdr = QHBoxLayout(self.widget)
        self.cupHdr.setObjectName(u"cupHdr")
        self.cupHdr.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(64, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.cupHdr.addItem(self.horizontalSpacer)

        self.cupHdrEngineLbl = QLabel(self.widget)
        self.cupHdrEngineLbl.setObjectName(u"cupHdrEngineLbl")
        sizePolicy.setHeightForWidth(self.cupHdrEngineLbl.sizePolicy().hasHeightForWidth())
        self.cupHdrEngineLbl.setSizePolicy(sizePolicy)

        self.cupHdr.addWidget(self.cupHdrEngineLbl)

        self.cupHdrEngineSel = QComboBox(self.widget)
        self.cupHdrEngineSel.addItem("")
        self.cupHdrEngineSel.addItem("")
        self.cupHdrEngineSel.addItem("")
        self.cupHdrEngineSel.addItem("")
        self.cupHdrEngineSel.setObjectName(u"cupHdrEngineSel")
        self.cupHdrEngineSel.setMinimumSize(QSize(96, 0))
        self.cupHdrEngineSel.setMaximumSize(QSize(256, 16777215))

        self.cupHdr.addWidget(self.cupHdrEngineSel)

        self.cupHdrApplyCupAll = QPushButton(self.widget)
        self.cupHdrApplyCupAll.setObjectName(u"cupHdrApplyCupAll")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.cupHdrApplyCupAll.sizePolicy().hasHeightForWidth())
        self.cupHdrApplyCupAll.setSizePolicy(sizePolicy4)

        self.cupHdr.addWidget(self.cupHdrApplyCupAll)

        self.horizontalSpacer_2 = QSpacerItem(64, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.cupHdr.addItem(self.horizontalSpacer_2)


        self.gridLayout_2.addWidget(self.widget, 1, 1, 1, 4)

        self.verticalSpacer_3 = QSpacerItem(20, 16, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 3, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 7, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 12, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 5, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_10, 4, 0, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_11, 4, 5, 1, 1)

        self.cup1 = QWidget(self.tabGP)
        self.cup1.setObjectName(u"cup1")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.cup1.sizePolicy().hasHeightForWidth())
        self.cup1.setSizePolicy(sizePolicy5)
        self.cup1.setMinimumSize(QSize(240, 172))
        self.cup1.setMaximumSize(QSize(240, 172))
        self.cup1Icon = QLabel(self.cup1)
        self.cup1Icon.setObjectName(u"cup1Icon")
        self.cup1Icon.setGeometry(QRect(88, 20, 64, 64))
        self.cup1Icon.setAlignment(Qt.AlignCenter)
        self.cup1Label = QLabel(self.cup1)
        self.cup1Label.setObjectName(u"cup1Label")
        self.cup1Label.setGeometry(QRect(20, 88, 200, 24))
        self.cup1Label.setAlignment(Qt.AlignCenter)
        self.cup1Rank = QComboBox(self.cup1)
        self.cup1Rank.addItem("")
        self.cup1Rank.addItem("")
        self.cup1Rank.addItem("")
        self.cup1Rank.addItem("")
        self.cup1Rank.addItem("")
        self.cup1Rank.addItem("")
        self.cup1Rank.addItem("")
        self.cup1Rank.setObjectName(u"cup1Rank")
        self.cup1Rank.setGeometry(QRect(10, 120, 112, 40))
        self.cup1Tro = QComboBox(self.cup1)
        self.cup1Tro.addItem("")
        self.cup1Tro.addItem("")
        self.cup1Tro.addItem("")
        self.cup1Tro.addItem("")
        self.cup1Tro.setObjectName(u"cup1Tro")
        self.cup1Tro.setGeometry(QRect(118, 120, 112, 40))
        self.cup1Active = QCheckBox(self.cup1)
        self.cup1Active.setObjectName(u"cup1Active")
        self.cup1Active.setEnabled(False)
        self.cup1Active.setGeometry(QRect(8, 8, 24, 24))
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.cup1Active.sizePolicy().hasHeightForWidth())
        self.cup1Active.setSizePolicy(sizePolicy6)
        self.cup1Active.setChecked(True)

        self.gridLayout_2.addWidget(self.cup1, 4, 1, 1, 1)

        self.cup2 = QWidget(self.tabGP)
        self.cup2.setObjectName(u"cup2")
        sizePolicy5.setHeightForWidth(self.cup2.sizePolicy().hasHeightForWidth())
        self.cup2.setSizePolicy(sizePolicy5)
        self.cup2.setMinimumSize(QSize(240, 172))
        self.cup2.setMaximumSize(QSize(240, 172))
        self.cup2Icon = QLabel(self.cup2)
        self.cup2Icon.setObjectName(u"cup2Icon")
        self.cup2Icon.setGeometry(QRect(88, 20, 64, 64))
        self.cup2Icon.setAlignment(Qt.AlignCenter)
        self.cup2Label = QLabel(self.cup2)
        self.cup2Label.setObjectName(u"cup2Label")
        self.cup2Label.setGeometry(QRect(20, 88, 200, 24))
        self.cup2Label.setAlignment(Qt.AlignCenter)
        self.cup2Rank = QComboBox(self.cup2)
        self.cup2Rank.addItem("")
        self.cup2Rank.addItem("")
        self.cup2Rank.addItem("")
        self.cup2Rank.addItem("")
        self.cup2Rank.addItem("")
        self.cup2Rank.addItem("")
        self.cup2Rank.addItem("")
        self.cup2Rank.setObjectName(u"cup2Rank")
        self.cup2Rank.setGeometry(QRect(10, 120, 112, 40))
        self.cup2Tro = QComboBox(self.cup2)
        self.cup2Tro.addItem("")
        self.cup2Tro.addItem("")
        self.cup2Tro.addItem("")
        self.cup2Tro.addItem("")
        self.cup2Tro.setObjectName(u"cup2Tro")
        self.cup2Tro.setGeometry(QRect(118, 120, 112, 40))
        self.cup2Active = QCheckBox(self.cup2)
        self.cup2Active.setObjectName(u"cup2Active")
        self.cup2Active.setGeometry(QRect(10, 10, 24, 24))
        sizePolicy6.setHeightForWidth(self.cup2Active.sizePolicy().hasHeightForWidth())
        self.cup2Active.setSizePolicy(sizePolicy6)

        self.gridLayout_2.addWidget(self.cup2, 4, 2, 1, 1)

        self.cup3 = QWidget(self.tabGP)
        self.cup3.setObjectName(u"cup3")
        sizePolicy5.setHeightForWidth(self.cup3.sizePolicy().hasHeightForWidth())
        self.cup3.setSizePolicy(sizePolicy5)
        self.cup3.setMinimumSize(QSize(240, 172))
        self.cup3.setMaximumSize(QSize(240, 172))
        self.cup3Icon = QLabel(self.cup3)
        self.cup3Icon.setObjectName(u"cup3Icon")
        self.cup3Icon.setGeometry(QRect(88, 20, 64, 64))
        self.cup3Icon.setAlignment(Qt.AlignCenter)
        self.cup3Label = QLabel(self.cup3)
        self.cup3Label.setObjectName(u"cup3Label")
        self.cup3Label.setGeometry(QRect(20, 88, 200, 24))
        self.cup3Label.setAlignment(Qt.AlignCenter)
        self.cup3Rank = QComboBox(self.cup3)
        self.cup3Rank.addItem("")
        self.cup3Rank.addItem("")
        self.cup3Rank.addItem("")
        self.cup3Rank.addItem("")
        self.cup3Rank.addItem("")
        self.cup3Rank.addItem("")
        self.cup3Rank.addItem("")
        self.cup3Rank.setObjectName(u"cup3Rank")
        self.cup3Rank.setGeometry(QRect(10, 120, 112, 40))
        self.cup3Tro = QComboBox(self.cup3)
        self.cup3Tro.addItem("")
        self.cup3Tro.addItem("")
        self.cup3Tro.addItem("")
        self.cup3Tro.addItem("")
        self.cup3Tro.setObjectName(u"cup3Tro")
        self.cup3Tro.setGeometry(QRect(118, 120, 112, 40))
        self.cup3Active = QCheckBox(self.cup3)
        self.cup3Active.setObjectName(u"cup3Active")
        self.cup3Active.setGeometry(QRect(10, 10, 24, 24))
        sizePolicy6.setHeightForWidth(self.cup3Active.sizePolicy().hasHeightForWidth())
        self.cup3Active.setSizePolicy(sizePolicy6)

        self.gridLayout_2.addWidget(self.cup3, 4, 3, 1, 1)

        self.cup4 = QWidget(self.tabGP)
        self.cup4.setObjectName(u"cup4")
        sizePolicy5.setHeightForWidth(self.cup4.sizePolicy().hasHeightForWidth())
        self.cup4.setSizePolicy(sizePolicy5)
        self.cup4.setMinimumSize(QSize(240, 172))
        self.cup4.setMaximumSize(QSize(240, 172))
        self.cup4Icon = QLabel(self.cup4)
        self.cup4Icon.setObjectName(u"cup4Icon")
        self.cup4Icon.setGeometry(QRect(88, 20, 64, 64))
        self.cup4Icon.setAlignment(Qt.AlignCenter)
        self.cup4Label = QLabel(self.cup4)
        self.cup4Label.setObjectName(u"cup4Label")
        self.cup4Label.setGeometry(QRect(20, 88, 200, 24))
        self.cup4Label.setAlignment(Qt.AlignCenter)
        self.cup4Rank = QComboBox(self.cup4)
        self.cup4Rank.addItem("")
        self.cup4Rank.addItem("")
        self.cup4Rank.addItem("")
        self.cup4Rank.addItem("")
        self.cup4Rank.addItem("")
        self.cup4Rank.addItem("")
        self.cup4Rank.addItem("")
        self.cup4Rank.setObjectName(u"cup4Rank")
        self.cup4Rank.setGeometry(QRect(10, 120, 112, 40))
        self.cup4Tro = QComboBox(self.cup4)
        self.cup4Tro.addItem("")
        self.cup4Tro.addItem("")
        self.cup4Tro.addItem("")
        self.cup4Tro.addItem("")
        self.cup4Tro.setObjectName(u"cup4Tro")
        self.cup4Tro.setGeometry(QRect(118, 120, 112, 40))
        self.cup4Active = QCheckBox(self.cup4)
        self.cup4Active.setObjectName(u"cup4Active")
        self.cup4Active.setGeometry(QRect(10, 10, 24, 24))
        sizePolicy6.setHeightForWidth(self.cup4Active.sizePolicy().hasHeightForWidth())
        self.cup4Active.setSizePolicy(sizePolicy6)

        self.gridLayout_2.addWidget(self.cup4, 4, 4, 1, 1)

        self.cup5 = QWidget(self.tabGP)
        self.cup5.setObjectName(u"cup5")
        sizePolicy5.setHeightForWidth(self.cup5.sizePolicy().hasHeightForWidth())
        self.cup5.setSizePolicy(sizePolicy5)
        self.cup5.setMinimumSize(QSize(240, 172))
        self.cup5.setMaximumSize(QSize(240, 172))
        self.cup5Active = QCheckBox(self.cup5)
        self.cup5Active.setObjectName(u"cup5Active")
        self.cup5Active.setEnabled(False)
        self.cup5Active.setGeometry(QRect(8, 8, 24, 24))
        sizePolicy6.setHeightForWidth(self.cup5Active.sizePolicy().hasHeightForWidth())
        self.cup5Active.setSizePolicy(sizePolicy6)
        self.cup5Active.setChecked(True)
        self.cup5Icon = QLabel(self.cup5)
        self.cup5Icon.setObjectName(u"cup5Icon")
        self.cup5Icon.setGeometry(QRect(88, 20, 64, 64))
        self.cup5Icon.setAlignment(Qt.AlignCenter)
        self.cup5Label = QLabel(self.cup5)
        self.cup5Label.setObjectName(u"cup5Label")
        self.cup5Label.setGeometry(QRect(20, 88, 200, 24))
        self.cup5Label.setAlignment(Qt.AlignCenter)
        self.cup5Rank = QComboBox(self.cup5)
        self.cup5Rank.addItem("")
        self.cup5Rank.addItem("")
        self.cup5Rank.addItem("")
        self.cup5Rank.addItem("")
        self.cup5Rank.addItem("")
        self.cup5Rank.addItem("")
        self.cup5Rank.addItem("")
        self.cup5Rank.setObjectName(u"cup5Rank")
        self.cup5Rank.setGeometry(QRect(10, 120, 112, 40))
        self.cup5Tro = QComboBox(self.cup5)
        self.cup5Tro.addItem("")
        self.cup5Tro.addItem("")
        self.cup5Tro.addItem("")
        self.cup5Tro.addItem("")
        self.cup5Tro.setObjectName(u"cup5Tro")
        self.cup5Tro.setGeometry(QRect(118, 120, 112, 40))

        self.gridLayout_2.addWidget(self.cup5, 6, 1, 1, 1)

        self.cup6 = QWidget(self.tabGP)
        self.cup6.setObjectName(u"cup6")
        sizePolicy5.setHeightForWidth(self.cup6.sizePolicy().hasHeightForWidth())
        self.cup6.setSizePolicy(sizePolicy5)
        self.cup6.setMinimumSize(QSize(240, 172))
        self.cup6.setMaximumSize(QSize(240, 172))
        self.cup6Icon = QLabel(self.cup6)
        self.cup6Icon.setObjectName(u"cup6Icon")
        self.cup6Icon.setGeometry(QRect(88, 20, 64, 64))
        self.cup6Icon.setAlignment(Qt.AlignCenter)
        self.cup6Label = QLabel(self.cup6)
        self.cup6Label.setObjectName(u"cup6Label")
        self.cup6Label.setGeometry(QRect(20, 88, 200, 24))
        self.cup6Label.setAlignment(Qt.AlignCenter)
        self.cup6Rank = QComboBox(self.cup6)
        self.cup6Rank.addItem("")
        self.cup6Rank.addItem("")
        self.cup6Rank.addItem("")
        self.cup6Rank.addItem("")
        self.cup6Rank.addItem("")
        self.cup6Rank.addItem("")
        self.cup6Rank.addItem("")
        self.cup6Rank.setObjectName(u"cup6Rank")
        self.cup6Rank.setGeometry(QRect(10, 120, 112, 40))
        self.cup6Tro = QComboBox(self.cup6)
        self.cup6Tro.addItem("")
        self.cup6Tro.addItem("")
        self.cup6Tro.addItem("")
        self.cup6Tro.addItem("")
        self.cup6Tro.setObjectName(u"cup6Tro")
        self.cup6Tro.setGeometry(QRect(118, 120, 112, 40))
        self.cup6Active = QCheckBox(self.cup6)
        self.cup6Active.setObjectName(u"cup6Active")
        self.cup6Active.setGeometry(QRect(10, 10, 24, 24))
        sizePolicy6.setHeightForWidth(self.cup6Active.sizePolicy().hasHeightForWidth())
        self.cup6Active.setSizePolicy(sizePolicy6)

        self.gridLayout_2.addWidget(self.cup6, 6, 2, 1, 1)

        self.cup7 = QWidget(self.tabGP)
        self.cup7.setObjectName(u"cup7")
        sizePolicy5.setHeightForWidth(self.cup7.sizePolicy().hasHeightForWidth())
        self.cup7.setSizePolicy(sizePolicy5)
        self.cup7.setMinimumSize(QSize(240, 172))
        self.cup7.setMaximumSize(QSize(240, 172))
        self.cup7Icon = QLabel(self.cup7)
        self.cup7Icon.setObjectName(u"cup7Icon")
        self.cup7Icon.setGeometry(QRect(88, 20, 64, 64))
        self.cup7Icon.setAlignment(Qt.AlignCenter)
        self.cup7Label = QLabel(self.cup7)
        self.cup7Label.setObjectName(u"cup7Label")
        self.cup7Label.setGeometry(QRect(20, 88, 200, 24))
        self.cup7Label.setAlignment(Qt.AlignCenter)
        self.cup7Rank = QComboBox(self.cup7)
        self.cup7Rank.addItem("")
        self.cup7Rank.addItem("")
        self.cup7Rank.addItem("")
        self.cup7Rank.addItem("")
        self.cup7Rank.addItem("")
        self.cup7Rank.addItem("")
        self.cup7Rank.addItem("")
        self.cup7Rank.setObjectName(u"cup7Rank")
        self.cup7Rank.setGeometry(QRect(10, 120, 112, 40))
        self.cup7Tro = QComboBox(self.cup7)
        self.cup7Tro.addItem("")
        self.cup7Tro.addItem("")
        self.cup7Tro.addItem("")
        self.cup7Tro.addItem("")
        self.cup7Tro.setObjectName(u"cup7Tro")
        self.cup7Tro.setGeometry(QRect(118, 120, 112, 40))
        self.cup7Active = QCheckBox(self.cup7)
        self.cup7Active.setObjectName(u"cup7Active")
        self.cup7Active.setGeometry(QRect(10, 10, 24, 24))
        sizePolicy6.setHeightForWidth(self.cup7Active.sizePolicy().hasHeightForWidth())
        self.cup7Active.setSizePolicy(sizePolicy6)

        self.gridLayout_2.addWidget(self.cup7, 6, 3, 1, 1)

        self.cup8 = QWidget(self.tabGP)
        self.cup8.setObjectName(u"cup8")
        sizePolicy5.setHeightForWidth(self.cup8.sizePolicy().hasHeightForWidth())
        self.cup8.setSizePolicy(sizePolicy5)
        self.cup8.setMinimumSize(QSize(240, 172))
        self.cup8.setMaximumSize(QSize(240, 172))
        self.cup8Icon = QLabel(self.cup8)
        self.cup8Icon.setObjectName(u"cup8Icon")
        self.cup8Icon.setGeometry(QRect(88, 20, 64, 64))
        self.cup8Icon.setAlignment(Qt.AlignCenter)
        self.cup8Label = QLabel(self.cup8)
        self.cup8Label.setObjectName(u"cup8Label")
        self.cup8Label.setGeometry(QRect(20, 88, 200, 24))
        self.cup8Label.setAlignment(Qt.AlignCenter)
        self.cup8Rank = QComboBox(self.cup8)
        self.cup8Rank.addItem("")
        self.cup8Rank.addItem("")
        self.cup8Rank.addItem("")
        self.cup8Rank.addItem("")
        self.cup8Rank.addItem("")
        self.cup8Rank.addItem("")
        self.cup8Rank.addItem("")
        self.cup8Rank.setObjectName(u"cup8Rank")
        self.cup8Rank.setGeometry(QRect(10, 120, 112, 40))
        self.cup8Tro = QComboBox(self.cup8)
        self.cup8Tro.addItem("")
        self.cup8Tro.addItem("")
        self.cup8Tro.addItem("")
        self.cup8Tro.addItem("")
        self.cup8Tro.setObjectName(u"cup8Tro")
        self.cup8Tro.setGeometry(QRect(118, 120, 112, 40))
        self.cup8Active = QCheckBox(self.cup8)
        self.cup8Active.setObjectName(u"cup8Active")
        self.cup8Active.setGeometry(QRect(10, 10, 24, 24))
        sizePolicy6.setHeightForWidth(self.cup8Active.sizePolicy().hasHeightForWidth())
        self.cup8Active.setSizePolicy(sizePolicy6)

        self.gridLayout_2.addWidget(self.cup8, 6, 4, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 2)

        self.tabWidget.addTab(self.tabGP, "")
        self.tabOpponent = QWidget()
        self.tabOpponent.setObjectName(u"tabOpponent")
        self.horizontalLayout_3 = QHBoxLayout(self.tabOpponent)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)

        self.oppPicker = QWidget(self.tabOpponent)
        self.oppPicker.setObjectName(u"oppPicker")
        self.oppPicker.setMinimumSize(QSize(160, 0))
        self.verticalLayout_3 = QVBoxLayout(self.oppPicker)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.opponents = QListWidget(self.oppPicker)
        self.opponents.setObjectName(u"opponents")
        self.opponents.setMinimumSize(QSize(0, 300))
        self.opponents.setMaximumSize(QSize(300, 16777215))
        self.opponents.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_5.addWidget(self.opponents, 8, 0, 1, 3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.oppPickToTop = QPushButton(self.oppPicker)
        self.oppPickToTop.setObjectName(u"oppPickToTop")
        self.oppPickToTop.setMaximumSize(QSize(48, 16777215))

        self.horizontalLayout.addWidget(self.oppPickToTop)

        self.oppPickToBot = QPushButton(self.oppPicker)
        self.oppPickToBot.setObjectName(u"oppPickToBot")
        self.oppPickToBot.setMaximumSize(QSize(48, 16777215))

        self.horizontalLayout.addWidget(self.oppPickToBot)

        self.oppPickDown = QPushButton(self.oppPicker)
        self.oppPickDown.setObjectName(u"oppPickDown")
        self.oppPickDown.setMaximumSize(QSize(48, 16777215))

        self.horizontalLayout.addWidget(self.oppPickDown)

        self.oppPickUp = QPushButton(self.oppPicker)
        self.oppPickUp.setObjectName(u"oppPickUp")
        self.oppPickUp.setMaximumSize(QSize(48, 16777215))

        self.horizontalLayout.addWidget(self.oppPickUp)


        self.gridLayout_5.addLayout(self.horizontalLayout, 10, 0, 1, 3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.oppCurrent = QLabel(self.oppPicker)
        self.oppCurrent.setObjectName(u"oppCurrent")
        self.oppCurrent.setMinimumSize(QSize(64, 32))
        self.oppCurrent.setMaximumSize(QSize(64, 16777215))
        font2 = QFont()
        font2.setFamily(u"RodinNTLG2")
        font2.setPointSize(16)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.oppCurrent.setFont(font2)
        self.oppCurrent.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.oppCurrent)

        self.oppLblSlash = QLabel(self.oppPicker)
        self.oppLblSlash.setObjectName(u"oppLblSlash")
        self.oppLblSlash.setMaximumSize(QSize(64, 16777215))
        font3 = QFont()
        font3.setFamily(u"RodinNTLG2")
        font3.setPointSize(13)
        font3.setStyleStrategy(QFont.PreferAntialias)
        self.oppLblSlash.setFont(font3)
        self.oppLblSlash.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.oppLblSlash)

        self.oppTotal = QLabel(self.oppPicker)
        self.oppTotal.setObjectName(u"oppTotal")
        self.oppTotal.setMinimumSize(QSize(64, 0))
        self.oppTotal.setMaximumSize(QSize(64, 16777215))
        font4 = QFont()
        font4.setFamily(u"RodinNTLG2")
        font4.setPointSize(10)
        font4.setStyleStrategy(QFont.PreferAntialias)
        self.oppTotal.setFont(font4)
        self.oppTotal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.oppTotal)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.gridLayout_5.addLayout(self.horizontalLayout_2, 0, 0, 1, 3)

        self.oppExport = QPushButton(self.oppPicker)
        self.oppExport.setObjectName(u"oppExport")
        sizePolicy1.setHeightForWidth(self.oppExport.sizePolicy().hasHeightForWidth())
        self.oppExport.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.oppExport, 11, 0, 1, 1)

        self.oppImport = QPushButton(self.oppPicker)
        self.oppImport.setObjectName(u"oppImport")

        self.gridLayout_5.addWidget(self.oppImport, 11, 1, 1, 1)

        self.oppRemove = QPushButton(self.oppPicker)
        self.oppRemove.setObjectName(u"oppRemove")
        sizePolicy1.setHeightForWidth(self.oppRemove.sizePolicy().hasHeightForWidth())
        self.oppRemove.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.oppRemove, 11, 2, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_5)


        self.horizontalLayout_3.addWidget(self.oppPicker)

        self.horizontalSpacer_5 = QSpacerItem(8, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.oppFrame = QFrame(self.tabOpponent)
        self.oppFrame.setObjectName(u"oppFrame")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.oppFrame.sizePolicy().hasHeightForWidth())
        self.oppFrame.setSizePolicy(sizePolicy7)
        self.oppFrame.setFrameShadow(QFrame.Plain)
        self.gridLayout_3 = QGridLayout(self.oppFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.oppCountryView = QWidget(self.oppFrame)
        self.oppCountryView.setObjectName(u"oppCountryView")
        self.oppCountryView.setMinimumSize(QSize(320, 44))
        self.oppCountryView.setMaximumSize(QSize(512, 80))
        self.oppCountryView.setStyleSheet(u"color: white; background-color: #112; border-radius: 8px")
        self.verticalLayout_4 = QVBoxLayout(self.oppCountryView)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(8, 2, 8, 2)
        self.oppCountyLabel = QLabel(self.oppCountryView)
        self.oppCountyLabel.setObjectName(u"oppCountyLabel")
        self.oppCountyLabel.setMinimumSize(QSize(0, 32))
        font5 = QFont()
        font5.setPointSize(9)
        self.oppCountyLabel.setFont(font5)
        self.oppCountyLabel.setTextFormat(Qt.PlainText)
        self.oppCountyLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.oppCountyLabel)


        self.gridLayout_3.addWidget(self.oppCountryView, 8, 2, 1, 1)

        self.oppUnlock = QLabel(self.oppFrame)
        self.oppUnlock.setObjectName(u"oppUnlock")

        self.gridLayout_3.addWidget(self.oppUnlock, 18, 1, 1, 1)

        self.oppOwnWin = QLabel(self.oppFrame)
        self.oppOwnWin.setObjectName(u"oppOwnWin")
        sizePolicy.setHeightForWidth(self.oppOwnWin.sizePolicy().hasHeightForWidth())
        self.oppOwnWin.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.oppOwnWin, 15, 1, 1, 1)

        self.oppCountry = QLabel(self.oppFrame)
        self.oppCountry.setObjectName(u"oppCountry")
        sizePolicy.setHeightForWidth(self.oppCountry.sizePolicy().hasHeightForWidth())
        self.oppCountry.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.oppCountry, 7, 1, 2, 1)

        self.oppLosses = QLabel(self.oppFrame)
        self.oppLosses.setObjectName(u"oppLosses")
        sizePolicy.setHeightForWidth(self.oppLosses.sizePolicy().hasHeightForWidth())
        self.oppLosses.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.oppLosses, 3, 1, 1, 1)

        self.oppHdr2 = QLabel(self.oppFrame)
        self.oppHdr2.setObjectName(u"oppHdr2")
        sizePolicy3.setHeightForWidth(self.oppHdr2.sizePolicy().hasHeightForWidth())
        self.oppHdr2.setSizePolicy(sizePolicy3)
        self.oppHdr2.setMinimumSize(QSize(0, 28))
        font6 = QFont()
        font6.setFamily(u"RodinNTLG2")
        font6.setPointSize(14)
        font6.setBold(True)
        font6.setWeight(75)
        font6.setStyleStrategy(QFont.PreferAntialias)
        self.oppHdr2.setFont(font6)

        self.gridLayout_3.addWidget(self.oppHdr2, 11, 1, 1, 2)

        self.oppWins = QLabel(self.oppFrame)
        self.oppWins.setObjectName(u"oppWins")
        sizePolicy.setHeightForWidth(self.oppWins.sizePolicy().hasHeightForWidth())
        self.oppWins.setSizePolicy(sizePolicy)
        self.oppWins.setMinimumSize(QSize(232, 0))

        self.gridLayout_3.addWidget(self.oppWins, 1, 1, 1, 1)

        self.oppOwnLoss = QLabel(self.oppFrame)
        self.oppOwnLoss.setObjectName(u"oppOwnLoss")
        sizePolicy.setHeightForWidth(self.oppOwnLoss.sizePolicy().hasHeightForWidth())
        self.oppOwnLoss.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.oppOwnLoss, 16, 1, 1, 1)

        self.oppHdr1 = QLabel(self.oppFrame)
        self.oppHdr1.setObjectName(u"oppHdr1")
        sizePolicy3.setHeightForWidth(self.oppHdr1.sizePolicy().hasHeightForWidth())
        self.oppHdr1.setSizePolicy(sizePolicy3)
        self.oppHdr1.setMinimumSize(QSize(0, 28))
        self.oppHdr1.setFont(font6)

        self.gridLayout_3.addWidget(self.oppHdr1, 0, 1, 1, 2)

        self.line = QFrame(self.oppFrame)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 12))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line, 10, 1, 1, 2)

        self.oppMiiData = QLabel(self.oppFrame)
        self.oppMiiData.setObjectName(u"oppMiiData")
        sizePolicy.setHeightForWidth(self.oppMiiData.sizePolicy().hasHeightForWidth())
        self.oppMiiData.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.oppMiiData, 5, 1, 1, 1)

        self.oppVR = QLabel(self.oppFrame)
        self.oppVR.setObjectName(u"oppVR")
        sizePolicy.setHeightForWidth(self.oppVR.sizePolicy().hasHeightForWidth())
        self.oppVR.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.oppVR, 13, 1, 1, 1)

        self.oppWinsVal = QSpinBox(self.oppFrame)
        self.oppWinsVal.setObjectName(u"oppWinsVal")
        self.oppWinsVal.setMinimum(-999)
        self.oppWinsVal.setMaximum(999)

        self.gridLayout_3.addWidget(self.oppWinsVal, 1, 2, 1, 1)

        self.oppLossesVal = QSpinBox(self.oppFrame)
        self.oppLossesVal.setObjectName(u"oppLossesVal")
        self.oppLossesVal.setMinimum(-999)
        self.oppLossesVal.setMaximum(999)

        self.gridLayout_3.addWidget(self.oppLossesVal, 3, 2, 1, 1)

        self.oppEditMii = QPushButton(self.oppFrame)
        self.oppEditMii.setObjectName(u"oppEditMii")

        self.gridLayout_3.addWidget(self.oppEditMii, 5, 2, 1, 1)

        self.oppCountyFrm = QWidget(self.oppFrame)
        self.oppCountyFrm.setObjectName(u"oppCountyFrm")
        sizePolicy3.setHeightForWidth(self.oppCountyFrm.sizePolicy().hasHeightForWidth())
        self.oppCountyFrm.setSizePolicy(sizePolicy3)
        self.horizontalLayout_4 = QHBoxLayout(self.oppCountyFrm)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(6, 0, 6, 0)
        self.oppCountryVal = QSpinBox(self.oppCountyFrm)
        self.oppCountryVal.setObjectName(u"oppCountryVal")
        self.oppCountryVal.setMinimum(0)
        self.oppCountryVal.setMaximum(255)

        self.horizontalLayout_4.addWidget(self.oppCountryVal)

        self.oppAreaVal = QSpinBox(self.oppCountyFrm)
        self.oppAreaVal.setObjectName(u"oppAreaVal")
        self.oppAreaVal.setMaximum(255)

        self.horizontalLayout_4.addWidget(self.oppAreaVal)


        self.gridLayout_3.addWidget(self.oppCountyFrm, 7, 2, 1, 1)

        self.oppVRVal = QSpinBox(self.oppFrame)
        self.oppVRVal.setObjectName(u"oppVRVal")
        self.oppVRVal.setMinimum(1)
        self.oppVRVal.setMaximum(99999)
        self.oppVRVal.setValue(1000)

        self.gridLayout_3.addWidget(self.oppVRVal, 13, 2, 1, 1)

        self.oppOwnWinVal = QSpinBox(self.oppFrame)
        self.oppOwnWinVal.setObjectName(u"oppOwnWinVal")
        self.oppOwnWinVal.setMaximum(99999)

        self.gridLayout_3.addWidget(self.oppOwnWinVal, 15, 2, 1, 1)

        self.oppOwnLossVal = QSpinBox(self.oppFrame)
        self.oppOwnLossVal.setObjectName(u"oppOwnLossVal")
        self.oppOwnLossVal.setMaximum(99999)

        self.gridLayout_3.addWidget(self.oppOwnLossVal, 16, 2, 1, 1)

        self.oppUnlockMng = QPushButton(self.oppFrame)
        self.oppUnlockMng.setObjectName(u"oppUnlockMng")

        self.gridLayout_3.addWidget(self.oppUnlockMng, 18, 2, 1, 1)


        self.horizontalLayout_3.addWidget(self.oppFrame)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_9)

        self.tabWidget.addTab(self.tabOpponent, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 982, 27))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuContact = QMenu(self.menuHelp)
        self.menuContact.setObjectName(u"menuContact")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.tabWidget, self.genVRVal)
        QWidget.setTabOrder(self.genVRVal, self.genWinsVal)
        QWidget.setTabOrder(self.genWinsVal, self.genLossesVal)
        QWidget.setTabOrder(self.genLossesVal, self.genCoinsVal)
        QWidget.setTabOrder(self.genCoinsVal, self.genCecMeetsVal)
        QWidget.setTabOrder(self.genCecMeetsVal, self.genCecCommentVal)
        QWidget.setTabOrder(self.genCecCommentVal, self.genMiiDataEdit)
        QWidget.setTabOrder(self.genMiiDataEdit, self.genMaxValueBtn)
        QWidget.setTabOrder(self.genMaxValueBtn, self.genResetSaveBtn)
        QWidget.setTabOrder(self.genResetSaveBtn, self.genRandomSaveBtn)
        QWidget.setTabOrder(self.genRandomSaveBtn, self.unlCharList)
        QWidget.setTabOrder(self.unlCharList, self.unlBodyList)
        QWidget.setTabOrder(self.unlBodyList, self.unlTireList)
        QWidget.setTabOrder(self.unlTireList, self.unlGliderList)
        QWidget.setTabOrder(self.unlGliderList, self.cupHdrEngineSel)
        QWidget.setTabOrder(self.cupHdrEngineSel, self.cupHdrApplyCupAll)
        QWidget.setTabOrder(self.cupHdrApplyCupAll, self.cup1Rank)
        QWidget.setTabOrder(self.cup1Rank, self.cup1Tro)
        QWidget.setTabOrder(self.cup1Tro, self.cup2Rank)
        QWidget.setTabOrder(self.cup2Rank, self.cup2Tro)
        QWidget.setTabOrder(self.cup2Tro, self.cup3Rank)
        QWidget.setTabOrder(self.cup3Rank, self.cup3Tro)
        QWidget.setTabOrder(self.cup3Tro, self.cup4Rank)
        QWidget.setTabOrder(self.cup4Rank, self.cup4Tro)
        QWidget.setTabOrder(self.cup4Tro, self.cup5Rank)
        QWidget.setTabOrder(self.cup5Rank, self.cup5Tro)
        QWidget.setTabOrder(self.cup5Tro, self.cup6Rank)
        QWidget.setTabOrder(self.cup6Rank, self.cup6Tro)
        QWidget.setTabOrder(self.cup6Tro, self.cup7Rank)
        QWidget.setTabOrder(self.cup7Rank, self.cup7Tro)
        QWidget.setTabOrder(self.cup7Tro, self.cup8Rank)
        QWidget.setTabOrder(self.cup8Rank, self.cup8Tro)
        QWidget.setTabOrder(self.cup8Tro, self.cup1Active)
        QWidget.setTabOrder(self.cup1Active, self.cup2Active)
        QWidget.setTabOrder(self.cup2Active, self.cup3Active)
        QWidget.setTabOrder(self.cup3Active, self.cup4Active)
        QWidget.setTabOrder(self.cup4Active, self.cup5Active)
        QWidget.setTabOrder(self.cup5Active, self.cup6Active)
        QWidget.setTabOrder(self.cup6Active, self.cup7Active)
        QWidget.setTabOrder(self.cup7Active, self.cup8Active)
        QWidget.setTabOrder(self.cup8Active, self.opponents)
        QWidget.setTabOrder(self.opponents, self.oppPickToTop)
        QWidget.setTabOrder(self.oppPickToTop, self.oppPickToBot)
        QWidget.setTabOrder(self.oppPickToBot, self.oppPickDown)
        QWidget.setTabOrder(self.oppPickDown, self.oppPickUp)
        QWidget.setTabOrder(self.oppPickUp, self.oppExport)
        QWidget.setTabOrder(self.oppExport, self.oppImport)
        QWidget.setTabOrder(self.oppImport, self.oppRemove)
        QWidget.setTabOrder(self.oppRemove, self.oppWinsVal)
        QWidget.setTabOrder(self.oppWinsVal, self.oppLossesVal)
        QWidget.setTabOrder(self.oppLossesVal, self.oppEditMii)
        QWidget.setTabOrder(self.oppEditMii, self.oppCountryVal)
        QWidget.setTabOrder(self.oppCountryVal, self.oppAreaVal)
        QWidget.setTabOrder(self.oppAreaVal, self.oppVRVal)
        QWidget.setTabOrder(self.oppVRVal, self.oppOwnWinVal)
        QWidget.setTabOrder(self.oppOwnWinVal, self.oppOwnLossVal)
        QWidget.setTabOrder(self.oppOwnLossVal, self.oppUnlockMng)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionDummy1)
        self.menuHelp.addAction(self.actionAboutThisApp)
        self.menuHelp.addAction(self.actionAboutQt)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.menuContact.menuAction())
        self.menuContact.addAction(self.actionHelpGitHub)

        self.retranslateUi(MainWindow)
        self.actionQuit.triggered.connect(MainWindow.close)

        self.tabWidget.setCurrentIndex(0)
        self.unlCharList.setCurrentRow(0)
        self.unlBodyList.setCurrentRow(0)
        self.unlTireList.setCurrentRow(0)
        self.unlGliderList.setCurrentRow(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"&Open...", None))
#if QT_CONFIG(statustip)
        self.actionOpen.setStatusTip(QCoreApplication.translate("MainWindow", u"Open an existing save file", None))
#endif // QT_CONFIG(statustip)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"&Save", None))
#if QT_CONFIG(statustip)
        self.actionSave.setStatusTip(QCoreApplication.translate("MainWindow", u"Save changes to the file", None))
#endif // QT_CONFIG(statustip)
        self.actionSaveAs.setText(QCoreApplication.translate("MainWindow", u"S&ave As...", None))
#if QT_CONFIG(statustip)
        self.actionSaveAs.setStatusTip(QCoreApplication.translate("MainWindow", u"Save as a different format or another file", None))
#endif // QT_CONFIG(statustip)
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"&Quit", None))
#if QT_CONFIG(statustip)
        self.actionQuit.setStatusTip(QCoreApplication.translate("MainWindow", u"Exit the application (unsaved changes will be lost)", None))
#endif // QT_CONFIG(statustip)
        self.actionDummy1.setText(QCoreApplication.translate("MainWindow", u"Dummy1", None))
#if QT_CONFIG(statustip)
        self.actionDummy1.setStatusTip(QCoreApplication.translate("MainWindow", u"This action does nothing. IDK what to put here honestly", None))
#endif // QT_CONFIG(statustip)
        self.actionAboutThisApp.setText(QCoreApplication.translate("MainWindow", u"&About This App", None))
#if QT_CONFIG(statustip)
        self.actionAboutThisApp.setStatusTip(QCoreApplication.translate("MainWindow", u"Show application version and credits", None))
#endif // QT_CONFIG(statustip)
        self.actionAboutQt.setText(QCoreApplication.translate("MainWindow", u"About &Qt", None))
#if QT_CONFIG(statustip)
        self.actionAboutQt.setStatusTip(QCoreApplication.translate("MainWindow", u"Show active Qt version used by this application", None))
#endif // QT_CONFIG(statustip)
        self.actionHelpGitHub.setText(QCoreApplication.translate("MainWindow", u"File a &GitHub issue...", None))
#if QT_CONFIG(tooltip)
        self.actionHelpGitHub.setToolTip(QCoreApplication.translate("MainWindow", u"GitHub", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.actionHelpGitHub.setStatusTip(QCoreApplication.translate("MainWindow", u"Visit the GitHub repository to submit an issue", None))
#endif // QT_CONFIG(statustip)
        self.genMisc.setText(QCoreApplication.translate("MainWindow", u"Miscellaneous Options", None))
        self.genCecMeets.setText(QCoreApplication.translate("MainWindow", u"StreetPass Encounters", None))
        self.genCoins.setText(QCoreApplication.translate("MainWindow", u"Coin Count", None))
        self.genVR.setText(QCoreApplication.translate("MainWindow", u"Versus Rating", None))
        self.genCecComment.setText(QCoreApplication.translate("MainWindow", u"StreetPass Comment", None))
        self.genLosses.setText(QCoreApplication.translate("MainWindow", u"Losses", None))
        self.genWins.setText(QCoreApplication.translate("MainWindow", u"Wins", None))
        self.genMiiData.setText(QCoreApplication.translate("MainWindow", u"Mii Data", None))
        self.genVRVal.setSuffix(QCoreApplication.translate("MainWindow", u" VR", None))
        self.genWinsVal.setSuffix(QCoreApplication.translate("MainWindow", u" win(s)", None))
        self.genLossesVal.setSuffix(QCoreApplication.translate("MainWindow", u" loss(es)", None))
        self.genCoinsVal.setSuffix(QCoreApplication.translate("MainWindow", u" coin(s)", None))
        self.genCecMeetsVal.setSuffix(QCoreApplication.translate("MainWindow", u" encounter(s)", None))
#if QT_CONFIG(tooltip)
        self.genCecCommentVal.setToolTip(QCoreApplication.translate("MainWindow", u"<p>This is the comment displayed in a speech bubble in the Mario Kart Channel.</p><p>If left empty, the speech bubble is not displayed.</p><p>This field is limited to 16 characters.</p><p><b>Recommendation: </b>Have some moral decency and don't use inappropriate words, such as slurs.</p>", None))
#endif // QT_CONFIG(tooltip)
        self.genCecCommentVal.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[Speech bubble will not appear]", None))
#if QT_CONFIG(tooltip)
        self.genMiiDataEdit.setToolTip(QCoreApplication.translate("MainWindow", u"<p>View and edit a handful of values of your Mii.</p><p>Such include exporting the Mii or editing the Mii name.</p>", None))
#endif // QT_CONFIG(tooltip)
        self.genMiiDataEdit.setText(QCoreApplication.translate("MainWindow", u"Edit Mii data...", None))
#if QT_CONFIG(statustip)
        self.genMaxValueBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"This option unlocks all characters and kart parts, as well as set the stats to their maximum.", None))
#endif // QT_CONFIG(statustip)
        self.genMaxValueBtn.setText(QCoreApplication.translate("MainWindow", u"Maximize all values / Unlock everything", None))
#if QT_CONFIG(tooltip)
        self.genResetSaveBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<p><b>Note: </b>Your Mii will not be removed.</p>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.genResetSaveBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"This option will revert all settings, wipe the opponents list and relock kart parts and characters.", None))
#endif // QT_CONFIG(statustip)
        self.genResetSaveBtn.setText(QCoreApplication.translate("MainWindow", u"Reset save data to defaults", None))
#if QT_CONFIG(tooltip)
        self.genRandomSaveBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<p><b>Note: </b>Your and opponents' Miis will not be affected.</p>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.genRandomSaveBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"This option will try randomize all values safely.", None))
#endif // QT_CONFIG(statustip)
        self.genRandomSaveBtn.setText(QCoreApplication.translate("MainWindow", u"Randomize save data", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"General", None))
        self.unlCharLabel.setText(QCoreApplication.translate("MainWindow", u"Characters", None))

        __sortingEnabled = self.unlCharList.isSortingEnabled()
        self.unlCharList.setSortingEnabled(False)
        ___qlistwidgetitem = self.unlCharList.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Mario", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem.setToolTip(QCoreApplication.translate("MainWindow", u"This element cannot be unchecked.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem1 = self.unlCharList.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Luigi", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem1.setToolTip(QCoreApplication.translate("MainWindow", u"This element cannot be unchecked.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem2 = self.unlCharList.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Peach", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem2.setToolTip(QCoreApplication.translate("MainWindow", u"This element cannot be unchecked.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem3 = self.unlCharList.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Yoshi", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem3.setToolTip(QCoreApplication.translate("MainWindow", u"This element cannot be unchecked.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem4 = self.unlCharList.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Bowser", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem4.setToolTip(QCoreApplication.translate("MainWindow", u"This element cannot be unchecked.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem5 = self.unlCharList.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Donkey Kong", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem5.setToolTip(QCoreApplication.translate("MainWindow", u"This element cannot be unchecked.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem6 = self.unlCharList.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Toad", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem6.setToolTip(QCoreApplication.translate("MainWindow", u"This element cannot be unchecked.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem7 = self.unlCharList.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Koopa Troopa", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem7.setToolTip(QCoreApplication.translate("MainWindow", u"This element cannot be unchecked.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem8 = self.unlCharList.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Daisy", None));
        ___qlistwidgetitem9 = self.unlCharList.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Wario", None));
        ___qlistwidgetitem10 = self.unlCharList.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Rosalina", None));
        ___qlistwidgetitem11 = self.unlCharList.item(11)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Metal Mario", None));
        ___qlistwidgetitem12 = self.unlCharList.item(12)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Shy Guy", None));
        ___qlistwidgetitem13 = self.unlCharList.item(13)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Honey Queen", None));
        ___qlistwidgetitem14 = self.unlCharList.item(14)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Wiggler", None));
        ___qlistwidgetitem15 = self.unlCharList.item(15)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Lakitu", None));
        ___qlistwidgetitem16 = self.unlCharList.item(16)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Mii", None));
        self.unlCharList.setSortingEnabled(__sortingEnabled)

        self.unlBodyLabel.setText(QCoreApplication.translate("MainWindow", u"Karts", None))

        __sortingEnabled1 = self.unlBodyList.isSortingEnabled()
        self.unlBodyList.setSortingEnabled(False)
        ___qlistwidgetitem17 = self.unlBodyList.item(0)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Standard Kart", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem17.setToolTip(QCoreApplication.translate("MainWindow", u"This element cannot be unchecked.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem18 = self.unlBodyList.item(1)
        ___qlistwidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Bolt Buggy", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem18.setToolTip(QCoreApplication.translate("MainWindow", u"This element cannot be unchecked.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem19 = self.unlBodyList.item(2)
        ___qlistwidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Birthday Girl / Royal Ribbon", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem19.setToolTip(QCoreApplication.translate("MainWindow", u"This element cannot be unchecked.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem20 = self.unlBodyList.item(3)
        ___qlistwidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Egg 1", None));
        ___qlistwidgetitem21 = self.unlBodyList.item(4)
        ___qlistwidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Tiny Tug", None));
        ___qlistwidgetitem22 = self.unlBodyList.item(5)
        ___qlistwidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Cloud 9", None));
        ___qlistwidgetitem23 = self.unlBodyList.item(6)
        ___qlistwidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Zucchini / Gherkin", None));
        ___qlistwidgetitem24 = self.unlBodyList.item(7)
        ___qlistwidgetitem24.setText(QCoreApplication.translate("MainWindow", u"B Dasher", None));
        ___qlistwidgetitem25 = self.unlBodyList.item(8)
        ___qlistwidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Bruiser / Growlster", None));
        ___qlistwidgetitem26 = self.unlBodyList.item(9)
        ___qlistwidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Bumble V", None));
        ___qlistwidgetitem27 = self.unlBodyList.item(10)
        ___qlistwidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Koopa Clown", None));
        ___qlistwidgetitem28 = self.unlBodyList.item(11)
        ___qlistwidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Pipe Frame", None));
        ___qlistwidgetitem29 = self.unlBodyList.item(12)
        ___qlistwidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Blue Seven", None));
        ___qlistwidgetitem30 = self.unlBodyList.item(13)
        ___qlistwidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Cact X", None));
        ___qlistwidgetitem31 = self.unlBodyList.item(14)
        ___qlistwidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Barrel Train", None));
        ___qlistwidgetitem32 = self.unlBodyList.item(15)
        ___qlistwidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Soda Jet", None));
        ___qlistwidgetitem33 = self.unlBodyList.item(16)
        ___qlistwidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Gold Standard Kart", None));
        self.unlBodyList.setSortingEnabled(__sortingEnabled1)

        self.unlTireLabel.setText(QCoreApplication.translate("MainWindow", u"Tires", None))

        __sortingEnabled2 = self.unlTireList.isSortingEnabled()
        self.unlTireList.setSortingEnabled(False)
        ___qlistwidgetitem34 = self.unlTireList.item(0)
        ___qlistwidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Standard / Normal", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem34.setToolTip(QCoreApplication.translate("MainWindow", u"This element cannot be unchecked.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem35 = self.unlTireList.item(1)
        ___qlistwidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Monster", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem35.setToolTip(QCoreApplication.translate("MainWindow", u"This element cannot be unchecked.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem36 = self.unlTireList.item(2)
        ___qlistwidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Roller", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem36.setToolTip(QCoreApplication.translate("MainWindow", u"This element cannot be unchecked.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem37 = self.unlTireList.item(3)
        ___qlistwidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Slick", None));
        ___qlistwidgetitem38 = self.unlTireList.item(4)
        ___qlistwidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Slim", None));
        ___qlistwidgetitem39 = self.unlTireList.item(5)
        ___qlistwidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Sponge", None));
        ___qlistwidgetitem40 = self.unlTireList.item(6)
        ___qlistwidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Red Monster", None));
        ___qlistwidgetitem41 = self.unlTireList.item(7)
        ___qlistwidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Mushroom", None));
        ___qlistwidgetitem42 = self.unlTireList.item(8)
        ___qlistwidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Wood / Wooden", None));
        ___qlistwidgetitem43 = self.unlTireList.item(9)
        ___qlistwidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Gold Tires", None));
        self.unlTireList.setSortingEnabled(__sortingEnabled2)

        self.unlGliderLabel.setText(QCoreApplication.translate("MainWindow", u"Gliders", None))

        __sortingEnabled3 = self.unlGliderList.isSortingEnabled()
        self.unlGliderList.setSortingEnabled(False)
        ___qlistwidgetitem44 = self.unlGliderList.item(0)
        ___qlistwidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Standard", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem44.setToolTip(QCoreApplication.translate("MainWindow", u"This element cannot be unchecked.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem45 = self.unlGliderList.item(1)
        ___qlistwidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Paraglider / Parafoil", None));
        ___qlistwidgetitem46 = self.unlGliderList.item(2)
        ___qlistwidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Peach Parasol", None));
        ___qlistwidgetitem47 = self.unlGliderList.item(3)
        ___qlistwidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Flower Glider", None));
        ___qlistwidgetitem48 = self.unlGliderList.item(4)
        ___qlistwidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Swooper / Swoop", None));
        ___qlistwidgetitem49 = self.unlGliderList.item(5)
        ___qlistwidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Beast Glider / Ghastly Glider", None));
        ___qlistwidgetitem50 = self.unlGliderList.item(6)
        ___qlistwidgetitem50.setText(QCoreApplication.translate("MainWindow", u"Gold Glider", None));
        self.unlGliderList.setSortingEnabled(__sortingEnabled3)

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Tick the entries you want to have unlocked. Some entries may not be togglable.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabUnlocks), QCoreApplication.translate("MainWindow", u"Unlocks", None))
        self.cupHdrEngineLbl.setText(QCoreApplication.translate("MainWindow", u"Current engine class", None))
        self.cupHdrEngineSel.setItemText(0, QCoreApplication.translate("MainWindow", u"50 cc", None))
        self.cupHdrEngineSel.setItemText(1, QCoreApplication.translate("MainWindow", u"100 cc", None))
        self.cupHdrEngineSel.setItemText(2, QCoreApplication.translate("MainWindow", u"150 cc", None))
        self.cupHdrEngineSel.setItemText(3, QCoreApplication.translate("MainWindow", u"Mirror", None))

#if QT_CONFIG(statustip)
        self.cupHdrEngineSel.setStatusTip(QCoreApplication.translate("MainWindow", u"Select engine class: 50cc, 100cc, 150cc and Mirror", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.cupHdrApplyCupAll.setStatusTip(QCoreApplication.translate("MainWindow", u"Apply the trophies and ranks of this engine class to all engine classes.", None))
#endif // QT_CONFIG(statustip)
        self.cupHdrApplyCupAll.setText(QCoreApplication.translate("MainWindow", u"Apply current engine class to all", None))
        self.cup1Icon.setText(QCoreApplication.translate("MainWindow", u"-----\n"
"cup icon\n"
"------", None))
        self.cup1Label.setText(QCoreApplication.translate("MainWindow", u"Mushroom Cup", None))
        self.cup1Rank.setItemText(0, QCoreApplication.translate("MainWindow", u"No rank", None))
        self.cup1Rank.setItemText(1, QCoreApplication.translate("MainWindow", u"C (unused)", None))
        self.cup1Rank.setItemText(2, QCoreApplication.translate("MainWindow", u"B (unused)", None))
        self.cup1Rank.setItemText(3, QCoreApplication.translate("MainWindow", u"A (unused)", None))
        self.cup1Rank.setItemText(4, QCoreApplication.translate("MainWindow", u"1 Star", None))
        self.cup1Rank.setItemText(5, QCoreApplication.translate("MainWindow", u"2 Stars", None))
        self.cup1Rank.setItemText(6, QCoreApplication.translate("MainWindow", u"3 Stars", None))

        self.cup1Tro.setItemText(0, QCoreApplication.translate("MainWindow", u"No trophy", None))
        self.cup1Tro.setItemText(1, QCoreApplication.translate("MainWindow", u"Bronze", None))
        self.cup1Tro.setItemText(2, QCoreApplication.translate("MainWindow", u"Silver", None))
        self.cup1Tro.setItemText(3, QCoreApplication.translate("MainWindow", u"Gold", None))

#if QT_CONFIG(tooltip)
        self.cup1Active.setToolTip(QCoreApplication.translate("MainWindow", u"<p>This cup cannot be toggled.</p>", None))
#endif // QT_CONFIG(tooltip)
        self.cup1Active.setText("")
        self.cup2Icon.setText(QCoreApplication.translate("MainWindow", u"-----\n"
"cup icon\n"
"------", None))
        self.cup2Label.setText(QCoreApplication.translate("MainWindow", u"Flower Cup", None))
        self.cup2Rank.setItemText(0, QCoreApplication.translate("MainWindow", u"No rank", None))
        self.cup2Rank.setItemText(1, QCoreApplication.translate("MainWindow", u"C (unused)", None))
        self.cup2Rank.setItemText(2, QCoreApplication.translate("MainWindow", u"B (unused)", None))
        self.cup2Rank.setItemText(3, QCoreApplication.translate("MainWindow", u"A (unused)", None))
        self.cup2Rank.setItemText(4, QCoreApplication.translate("MainWindow", u"1 Star", None))
        self.cup2Rank.setItemText(5, QCoreApplication.translate("MainWindow", u"2 Stars", None))
        self.cup2Rank.setItemText(6, QCoreApplication.translate("MainWindow", u"3 Stars", None))

        self.cup2Tro.setItemText(0, QCoreApplication.translate("MainWindow", u"No trophy", None))
        self.cup2Tro.setItemText(1, QCoreApplication.translate("MainWindow", u"Bronze", None))
        self.cup2Tro.setItemText(2, QCoreApplication.translate("MainWindow", u"Silver", None))
        self.cup2Tro.setItemText(3, QCoreApplication.translate("MainWindow", u"Gold", None))

        self.cup2Active.setText("")
        self.cup3Icon.setText(QCoreApplication.translate("MainWindow", u"-----\n"
"cup icon\n"
"------", None))
        self.cup3Label.setText(QCoreApplication.translate("MainWindow", u"Star Cup", None))
        self.cup3Rank.setItemText(0, QCoreApplication.translate("MainWindow", u"No rank", None))
        self.cup3Rank.setItemText(1, QCoreApplication.translate("MainWindow", u"C (unused)", None))
        self.cup3Rank.setItemText(2, QCoreApplication.translate("MainWindow", u"B (unused)", None))
        self.cup3Rank.setItemText(3, QCoreApplication.translate("MainWindow", u"A (unused)", None))
        self.cup3Rank.setItemText(4, QCoreApplication.translate("MainWindow", u"1 Star", None))
        self.cup3Rank.setItemText(5, QCoreApplication.translate("MainWindow", u"2 Stars", None))
        self.cup3Rank.setItemText(6, QCoreApplication.translate("MainWindow", u"3 Stars", None))

        self.cup3Tro.setItemText(0, QCoreApplication.translate("MainWindow", u"No trophy", None))
        self.cup3Tro.setItemText(1, QCoreApplication.translate("MainWindow", u"Bronze", None))
        self.cup3Tro.setItemText(2, QCoreApplication.translate("MainWindow", u"Silver", None))
        self.cup3Tro.setItemText(3, QCoreApplication.translate("MainWindow", u"Gold", None))

        self.cup3Active.setText("")
        self.cup4Icon.setText(QCoreApplication.translate("MainWindow", u"-----\n"
"cup icon\n"
"------", None))
        self.cup4Label.setText(QCoreApplication.translate("MainWindow", u"Special Cup", None))
        self.cup4Rank.setItemText(0, QCoreApplication.translate("MainWindow", u"No rank", None))
        self.cup4Rank.setItemText(1, QCoreApplication.translate("MainWindow", u"C (unused)", None))
        self.cup4Rank.setItemText(2, QCoreApplication.translate("MainWindow", u"B (unused)", None))
        self.cup4Rank.setItemText(3, QCoreApplication.translate("MainWindow", u"A (unused)", None))
        self.cup4Rank.setItemText(4, QCoreApplication.translate("MainWindow", u"1 Star", None))
        self.cup4Rank.setItemText(5, QCoreApplication.translate("MainWindow", u"2 Stars", None))
        self.cup4Rank.setItemText(6, QCoreApplication.translate("MainWindow", u"3 Stars", None))

        self.cup4Tro.setItemText(0, QCoreApplication.translate("MainWindow", u"No trophy", None))
        self.cup4Tro.setItemText(1, QCoreApplication.translate("MainWindow", u"Bronze", None))
        self.cup4Tro.setItemText(2, QCoreApplication.translate("MainWindow", u"Silver", None))
        self.cup4Tro.setItemText(3, QCoreApplication.translate("MainWindow", u"Gold", None))

        self.cup4Active.setText("")
#if QT_CONFIG(tooltip)
        self.cup5Active.setToolTip(QCoreApplication.translate("MainWindow", u"<p>This cup cannot be toggled.</p>", None))
#endif // QT_CONFIG(tooltip)
        self.cup5Active.setText("")
        self.cup5Icon.setText(QCoreApplication.translate("MainWindow", u"-----\n"
"cup icon\n"
"------", None))
        self.cup5Label.setText(QCoreApplication.translate("MainWindow", u"Shell Cup", None))
        self.cup5Rank.setItemText(0, QCoreApplication.translate("MainWindow", u"No rank", None))
        self.cup5Rank.setItemText(1, QCoreApplication.translate("MainWindow", u"C (unused)", None))
        self.cup5Rank.setItemText(2, QCoreApplication.translate("MainWindow", u"B (unused)", None))
        self.cup5Rank.setItemText(3, QCoreApplication.translate("MainWindow", u"A (unused)", None))
        self.cup5Rank.setItemText(4, QCoreApplication.translate("MainWindow", u"1 Star", None))
        self.cup5Rank.setItemText(5, QCoreApplication.translate("MainWindow", u"2 Stars", None))
        self.cup5Rank.setItemText(6, QCoreApplication.translate("MainWindow", u"3 Stars", None))

        self.cup5Tro.setItemText(0, QCoreApplication.translate("MainWindow", u"No trophy", None))
        self.cup5Tro.setItemText(1, QCoreApplication.translate("MainWindow", u"Bronze", None))
        self.cup5Tro.setItemText(2, QCoreApplication.translate("MainWindow", u"Silver", None))
        self.cup5Tro.setItemText(3, QCoreApplication.translate("MainWindow", u"Gold", None))

        self.cup6Icon.setText(QCoreApplication.translate("MainWindow", u"-----\n"
"cup icon\n"
"------", None))
        self.cup6Label.setText(QCoreApplication.translate("MainWindow", u"Banana Cup", None))
        self.cup6Rank.setItemText(0, QCoreApplication.translate("MainWindow", u"No rank", None))
        self.cup6Rank.setItemText(1, QCoreApplication.translate("MainWindow", u"C (unused)", None))
        self.cup6Rank.setItemText(2, QCoreApplication.translate("MainWindow", u"B (unused)", None))
        self.cup6Rank.setItemText(3, QCoreApplication.translate("MainWindow", u"A (unused)", None))
        self.cup6Rank.setItemText(4, QCoreApplication.translate("MainWindow", u"1 Star", None))
        self.cup6Rank.setItemText(5, QCoreApplication.translate("MainWindow", u"2 Stars", None))
        self.cup6Rank.setItemText(6, QCoreApplication.translate("MainWindow", u"3 Stars", None))

        self.cup6Tro.setItemText(0, QCoreApplication.translate("MainWindow", u"No trophy", None))
        self.cup6Tro.setItemText(1, QCoreApplication.translate("MainWindow", u"Bronze", None))
        self.cup6Tro.setItemText(2, QCoreApplication.translate("MainWindow", u"Silver", None))
        self.cup6Tro.setItemText(3, QCoreApplication.translate("MainWindow", u"Gold", None))

        self.cup6Active.setText("")
        self.cup7Icon.setText(QCoreApplication.translate("MainWindow", u"-----\n"
"cup icon\n"
"------", None))
        self.cup7Label.setText(QCoreApplication.translate("MainWindow", u"Leaf Cup", None))
        self.cup7Rank.setItemText(0, QCoreApplication.translate("MainWindow", u"No rank", None))
        self.cup7Rank.setItemText(1, QCoreApplication.translate("MainWindow", u"C (unused)", None))
        self.cup7Rank.setItemText(2, QCoreApplication.translate("MainWindow", u"B (unused)", None))
        self.cup7Rank.setItemText(3, QCoreApplication.translate("MainWindow", u"A (unused)", None))
        self.cup7Rank.setItemText(4, QCoreApplication.translate("MainWindow", u"1 Star", None))
        self.cup7Rank.setItemText(5, QCoreApplication.translate("MainWindow", u"2 Stars", None))
        self.cup7Rank.setItemText(6, QCoreApplication.translate("MainWindow", u"3 Stars", None))

        self.cup7Tro.setItemText(0, QCoreApplication.translate("MainWindow", u"No trophy", None))
        self.cup7Tro.setItemText(1, QCoreApplication.translate("MainWindow", u"Bronze", None))
        self.cup7Tro.setItemText(2, QCoreApplication.translate("MainWindow", u"Silver", None))
        self.cup7Tro.setItemText(3, QCoreApplication.translate("MainWindow", u"Gold", None))

        self.cup7Active.setText("")
        self.cup8Icon.setText(QCoreApplication.translate("MainWindow", u"-----\n"
"cup icon\n"
"------", None))
        self.cup8Label.setText(QCoreApplication.translate("MainWindow", u"Lightning Cup", None))
        self.cup8Rank.setItemText(0, QCoreApplication.translate("MainWindow", u"No rank", None))
        self.cup8Rank.setItemText(1, QCoreApplication.translate("MainWindow", u"C (unused)", None))
        self.cup8Rank.setItemText(2, QCoreApplication.translate("MainWindow", u"B (unused)", None))
        self.cup8Rank.setItemText(3, QCoreApplication.translate("MainWindow", u"A (unused)", None))
        self.cup8Rank.setItemText(4, QCoreApplication.translate("MainWindow", u"1 Star", None))
        self.cup8Rank.setItemText(5, QCoreApplication.translate("MainWindow", u"2 Stars", None))
        self.cup8Rank.setItemText(6, QCoreApplication.translate("MainWindow", u"3 Stars", None))

        self.cup8Tro.setItemText(0, QCoreApplication.translate("MainWindow", u"No trophy", None))
        self.cup8Tro.setItemText(1, QCoreApplication.translate("MainWindow", u"Bronze", None))
        self.cup8Tro.setItemText(2, QCoreApplication.translate("MainWindow", u"Silver", None))
        self.cup8Tro.setItemText(3, QCoreApplication.translate("MainWindow", u"Gold", None))

        self.cup8Active.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGP), QCoreApplication.translate("MainWindow", u"Grand Prix", None))
#if QT_CONFIG(statustip)
        self.oppPickToTop.setStatusTip(QCoreApplication.translate("MainWindow", u"Move this opponent to the top of the list", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.oppPickToTop.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+Home", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(statustip)
        self.oppPickToBot.setStatusTip(QCoreApplication.translate("MainWindow", u"Move this opponent up one entry", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.oppPickToBot.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+Up", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(statustip)
        self.oppPickDown.setStatusTip(QCoreApplication.translate("MainWindow", u"Move this opponent down one entry", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.oppPickDown.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+Down", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(statustip)
        self.oppPickUp.setStatusTip(QCoreApplication.translate("MainWindow", u"Move this opponent to the bottom of the list", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.oppPickUp.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+End", None))
#endif // QT_CONFIG(shortcut)
        self.oppCurrent.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.oppLblSlash.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.oppTotal.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(statustip)
        self.oppExport.setStatusTip(QCoreApplication.translate("MainWindow", u"Export this opponent", None))
#endif // QT_CONFIG(statustip)
        self.oppExport.setText(QCoreApplication.translate("MainWindow", u"E&xport", None))
#if QT_CONFIG(statustip)
        self.oppImport.setStatusTip(QCoreApplication.translate("MainWindow", u"Import an opponent", None))
#endif // QT_CONFIG(statustip)
        self.oppImport.setText(QCoreApplication.translate("MainWindow", u"&Import", None))
#if QT_CONFIG(statustip)
        self.oppRemove.setStatusTip(QCoreApplication.translate("MainWindow", u"Remove this opponent from the list", None))
#endif // QT_CONFIG(statustip)
        self.oppRemove.setText(QCoreApplication.translate("MainWindow", u"Remo&ve", None))
#if QT_CONFIG(tooltip)
        self.oppCountryView.setToolTip(QCoreApplication.translate("MainWindow", u"<p>This is a rough demonstration of what Mario Kart 7 would show in the Opponents List.</p>", None))
#endif // QT_CONFIG(tooltip)
        self.oppCountyLabel.setText(QCoreApplication.translate("MainWindow", u"Country (i.e. Deutschland)\n"
"Hier k\u00f6nnte Ihre Werbung stehen.", None))
        self.oppUnlock.setText(QCoreApplication.translate("MainWindow", u"Opponent's Game Unlocks", None))
        self.oppOwnWin.setText(QCoreApplication.translate("MainWindow", u"Opponent's own wins", None))
        self.oppCountry.setText(QCoreApplication.translate("MainWindow", u"Country / Area", None))
        self.oppLosses.setText(QCoreApplication.translate("MainWindow", u"Losses", None))
        self.oppHdr2.setText(QCoreApplication.translate("MainWindow", u"Stats not shown in-game", None))
        self.oppWins.setText(QCoreApplication.translate("MainWindow", u"Wins", None))
        self.oppOwnLoss.setText(QCoreApplication.translate("MainWindow", u"Opponent's own losses", None))
        self.oppHdr1.setText(QCoreApplication.translate("MainWindow", u"In-game properties", None))
        self.oppMiiData.setText(QCoreApplication.translate("MainWindow", u"Mii Data", None))
        self.oppVR.setText(QCoreApplication.translate("MainWindow", u"Versus Rating", None))
        self.oppWinsVal.setSuffix(QCoreApplication.translate("MainWindow", u" win(s)", None))
        self.oppLossesVal.setSuffix(QCoreApplication.translate("MainWindow", u" loss(es)", None))
#if QT_CONFIG(tooltip)
        self.oppEditMii.setToolTip(QCoreApplication.translate("MainWindow", u"<p>View and edit a handful of values of this opponent's Mii.</p><p>Such include exporting the Mii or editing the Mii name.</p>", None))
#endif // QT_CONFIG(tooltip)
        self.oppEditMii.setText(QCoreApplication.translate("MainWindow", u"Edit Mii data...", None))
        self.oppCountryVal.setPrefix(QCoreApplication.translate("MainWindow", u"ID ", None))
        self.oppAreaVal.setPrefix(QCoreApplication.translate("MainWindow", u"Sub ID ", None))
        self.oppVRVal.setSuffix(QCoreApplication.translate("MainWindow", u" VR", None))
        self.oppOwnWinVal.setSuffix(QCoreApplication.translate("MainWindow", u" win(s)", None))
        self.oppOwnLossVal.setSuffix(QCoreApplication.translate("MainWindow", u" loss(es)", None))
#if QT_CONFIG(tooltip)
        self.oppUnlockMng.setToolTip(QCoreApplication.translate("MainWindow", u"Editing them has no impact, but if you want, you can duplicate them for yourself.", None))
#endif // QT_CONFIG(tooltip)
        self.oppUnlockMng.setText(QCoreApplication.translate("MainWindow", u"View Unlocks", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabOpponent), QCoreApplication.translate("MainWindow", u"Opponents", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"&Edit", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"&Help", None))
        self.menuContact.setTitle(QCoreApplication.translate("MainWindow", u"&Contact", None))
        pass
    # retranslateUi

