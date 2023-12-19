# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewOppUnlocksyjSsMl.ui'
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
        Dialog.resize(576, 400)
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
        self.warnFrame = QFrame(Dialog)
        self.warnFrame.setObjectName(u"warnFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
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


        self.gridLayout.addWidget(self.warnFrame, 1, 0, 1, 2)

        self.unlGlider = QVBoxLayout()
        self.unlGlider.setSpacing(0)
        self.unlGlider.setObjectName(u"unlGlider")
        self.unlGliderLabel = QLabel(Dialog)
        self.unlGliderLabel.setObjectName(u"unlGliderLabel")
        self.unlGliderLabel.setMinimumSize(QSize(0, 32))
        font1 = QFont()
        font1.setFamily(u"RodinNTLG2")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.unlGliderLabel.setFont(font1)

        self.unlGlider.addWidget(self.unlGliderLabel)

        self.unlGliderList = QListWidget(Dialog)
        __qlistwidgetitem = QListWidgetItem(self.unlGliderList)
        __qlistwidgetitem.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsEnabled);
        __qlistwidgetitem1 = QListWidgetItem(self.unlGliderList)
        __qlistwidgetitem1.setCheckState(Qt.Unchecked);
        __qlistwidgetitem2 = QListWidgetItem(self.unlGliderList)
        __qlistwidgetitem2.setCheckState(Qt.Unchecked);
        __qlistwidgetitem3 = QListWidgetItem(self.unlGliderList)
        __qlistwidgetitem3.setCheckState(Qt.Unchecked);
        __qlistwidgetitem4 = QListWidgetItem(self.unlGliderList)
        __qlistwidgetitem4.setCheckState(Qt.Unchecked);
        __qlistwidgetitem5 = QListWidgetItem(self.unlGliderList)
        __qlistwidgetitem5.setCheckState(Qt.Unchecked);
        __qlistwidgetitem6 = QListWidgetItem(self.unlGliderList)
        __qlistwidgetitem6.setCheckState(Qt.Unchecked);
        self.unlGliderList.setObjectName(u"unlGliderList")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.unlGliderList.sizePolicy().hasHeightForWidth())
        self.unlGliderList.setSizePolicy(sizePolicy1)
        self.unlGliderList.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.unlGlider.addWidget(self.unlGliderList)


        self.gridLayout.addLayout(self.unlGlider, 4, 0, 1, 1)

        self.unlChar = QVBoxLayout()
        self.unlChar.setSpacing(0)
        self.unlChar.setObjectName(u"unlChar")
        self.unlCharLabel = QLabel(Dialog)
        self.unlCharLabel.setObjectName(u"unlCharLabel")
        self.unlCharLabel.setMinimumSize(QSize(0, 32))
        self.unlCharLabel.setFont(font1)

        self.unlChar.addWidget(self.unlCharLabel)

        self.unlCharList = QListWidget(Dialog)
        __qlistwidgetitem7 = QListWidgetItem(self.unlCharList)
        __qlistwidgetitem7.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem7.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsEnabled);
        __qlistwidgetitem8 = QListWidgetItem(self.unlCharList)
        __qlistwidgetitem8.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem8.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsEnabled);
        __qlistwidgetitem9 = QListWidgetItem(self.unlCharList)
        __qlistwidgetitem9.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem9.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsEnabled);
        __qlistwidgetitem10 = QListWidgetItem(self.unlCharList)
        __qlistwidgetitem10.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem10.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsEnabled);
        __qlistwidgetitem11 = QListWidgetItem(self.unlCharList)
        __qlistwidgetitem11.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem11.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsEnabled);
        __qlistwidgetitem12 = QListWidgetItem(self.unlCharList)
        __qlistwidgetitem12.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem12.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsEnabled);
        __qlistwidgetitem13 = QListWidgetItem(self.unlCharList)
        __qlistwidgetitem13.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem13.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsEnabled);
        __qlistwidgetitem14 = QListWidgetItem(self.unlCharList)
        __qlistwidgetitem14.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem14.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsEnabled);
        __qlistwidgetitem15 = QListWidgetItem(self.unlCharList)
        __qlistwidgetitem15.setCheckState(Qt.Unchecked);
        __qlistwidgetitem16 = QListWidgetItem(self.unlCharList)
        __qlistwidgetitem16.setCheckState(Qt.Unchecked);
        __qlistwidgetitem17 = QListWidgetItem(self.unlCharList)
        __qlistwidgetitem17.setCheckState(Qt.Unchecked);
        __qlistwidgetitem18 = QListWidgetItem(self.unlCharList)
        __qlistwidgetitem18.setCheckState(Qt.Unchecked);
        __qlistwidgetitem19 = QListWidgetItem(self.unlCharList)
        __qlistwidgetitem19.setCheckState(Qt.Unchecked);
        __qlistwidgetitem20 = QListWidgetItem(self.unlCharList)
        __qlistwidgetitem20.setCheckState(Qt.Unchecked);
        __qlistwidgetitem21 = QListWidgetItem(self.unlCharList)
        __qlistwidgetitem21.setCheckState(Qt.Unchecked);
        __qlistwidgetitem22 = QListWidgetItem(self.unlCharList)
        __qlistwidgetitem22.setCheckState(Qt.Unchecked);
        __qlistwidgetitem23 = QListWidgetItem(self.unlCharList)
        __qlistwidgetitem23.setCheckState(Qt.Unchecked);
        self.unlCharList.setObjectName(u"unlCharList")
        sizePolicy1.setHeightForWidth(self.unlCharList.sizePolicy().hasHeightForWidth())
        self.unlCharList.setSizePolicy(sizePolicy1)
        self.unlCharList.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.unlChar.addWidget(self.unlCharList)


        self.gridLayout.addLayout(self.unlChar, 2, 0, 1, 1)

        self.unlTire = QVBoxLayout()
        self.unlTire.setSpacing(0)
        self.unlTire.setObjectName(u"unlTire")
        self.unlTireLabel = QLabel(Dialog)
        self.unlTireLabel.setObjectName(u"unlTireLabel")
        self.unlTireLabel.setMinimumSize(QSize(0, 32))
        self.unlTireLabel.setFont(font1)

        self.unlTire.addWidget(self.unlTireLabel)

        self.unlTireList = QListWidget(Dialog)
        __qlistwidgetitem24 = QListWidgetItem(self.unlTireList)
        __qlistwidgetitem24.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem24.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsEnabled);
        __qlistwidgetitem25 = QListWidgetItem(self.unlTireList)
        __qlistwidgetitem25.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem25.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsEnabled);
        __qlistwidgetitem26 = QListWidgetItem(self.unlTireList)
        __qlistwidgetitem26.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem26.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsEnabled);
        __qlistwidgetitem27 = QListWidgetItem(self.unlTireList)
        __qlistwidgetitem27.setCheckState(Qt.Unchecked);
        __qlistwidgetitem28 = QListWidgetItem(self.unlTireList)
        __qlistwidgetitem28.setCheckState(Qt.Unchecked);
        __qlistwidgetitem29 = QListWidgetItem(self.unlTireList)
        __qlistwidgetitem29.setCheckState(Qt.Unchecked);
        __qlistwidgetitem30 = QListWidgetItem(self.unlTireList)
        __qlistwidgetitem30.setCheckState(Qt.Unchecked);
        __qlistwidgetitem31 = QListWidgetItem(self.unlTireList)
        __qlistwidgetitem31.setCheckState(Qt.Unchecked);
        __qlistwidgetitem32 = QListWidgetItem(self.unlTireList)
        __qlistwidgetitem32.setCheckState(Qt.Unchecked);
        __qlistwidgetitem33 = QListWidgetItem(self.unlTireList)
        __qlistwidgetitem33.setCheckState(Qt.Unchecked);
        self.unlTireList.setObjectName(u"unlTireList")
        sizePolicy1.setHeightForWidth(self.unlTireList.sizePolicy().hasHeightForWidth())
        self.unlTireList.setSizePolicy(sizePolicy1)
        self.unlTireList.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.unlTire.addWidget(self.unlTireList)


        self.gridLayout.addLayout(self.unlTire, 2, 1, 1, 1)

        self.unlBody = QVBoxLayout()
        self.unlBody.setSpacing(0)
        self.unlBody.setObjectName(u"unlBody")
        self.unlBodyLabel = QLabel(Dialog)
        self.unlBodyLabel.setObjectName(u"unlBodyLabel")
        self.unlBodyLabel.setMinimumSize(QSize(0, 32))
        self.unlBodyLabel.setFont(font1)

        self.unlBody.addWidget(self.unlBodyLabel)

        self.unlBodyList = QListWidget(Dialog)
        __qlistwidgetitem34 = QListWidgetItem(self.unlBodyList)
        __qlistwidgetitem34.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem34.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsEnabled);
        __qlistwidgetitem35 = QListWidgetItem(self.unlBodyList)
        __qlistwidgetitem35.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem35.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsEnabled);
        __qlistwidgetitem36 = QListWidgetItem(self.unlBodyList)
        __qlistwidgetitem36.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem36.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsEnabled);
        __qlistwidgetitem37 = QListWidgetItem(self.unlBodyList)
        __qlistwidgetitem37.setCheckState(Qt.Unchecked);
        __qlistwidgetitem38 = QListWidgetItem(self.unlBodyList)
        __qlistwidgetitem38.setCheckState(Qt.Unchecked);
        __qlistwidgetitem39 = QListWidgetItem(self.unlBodyList)
        __qlistwidgetitem39.setCheckState(Qt.Unchecked);
        __qlistwidgetitem40 = QListWidgetItem(self.unlBodyList)
        __qlistwidgetitem40.setCheckState(Qt.Unchecked);
        __qlistwidgetitem41 = QListWidgetItem(self.unlBodyList)
        __qlistwidgetitem41.setCheckState(Qt.Unchecked);
        __qlistwidgetitem42 = QListWidgetItem(self.unlBodyList)
        __qlistwidgetitem42.setCheckState(Qt.Unchecked);
        __qlistwidgetitem43 = QListWidgetItem(self.unlBodyList)
        __qlistwidgetitem43.setCheckState(Qt.Unchecked);
        __qlistwidgetitem44 = QListWidgetItem(self.unlBodyList)
        __qlistwidgetitem44.setCheckState(Qt.Unchecked);
        __qlistwidgetitem45 = QListWidgetItem(self.unlBodyList)
        __qlistwidgetitem45.setCheckState(Qt.Unchecked);
        __qlistwidgetitem46 = QListWidgetItem(self.unlBodyList)
        __qlistwidgetitem46.setCheckState(Qt.Unchecked);
        __qlistwidgetitem47 = QListWidgetItem(self.unlBodyList)
        __qlistwidgetitem47.setCheckState(Qt.Unchecked);
        __qlistwidgetitem48 = QListWidgetItem(self.unlBodyList)
        __qlistwidgetitem48.setCheckState(Qt.Unchecked);
        __qlistwidgetitem49 = QListWidgetItem(self.unlBodyList)
        __qlistwidgetitem49.setCheckState(Qt.Unchecked);
        __qlistwidgetitem50 = QListWidgetItem(self.unlBodyList)
        __qlistwidgetitem50.setCheckState(Qt.Unchecked);
        self.unlBodyList.setObjectName(u"unlBodyList")
        sizePolicy1.setHeightForWidth(self.unlBodyList.sizePolicy().hasHeightForWidth())
        self.unlBodyList.setSizePolicy(sizePolicy1)
        self.unlBodyList.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.unlBody.addWidget(self.unlBodyList)


        self.gridLayout.addLayout(self.unlBody, 4, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)

        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 2)


        self.retranslateUi(Dialog)
        self.buttonBox.clicked.connect(Dialog.close)

        self.unlGliderList.setCurrentRow(0)
        self.unlCharList.setCurrentRow(0)
        self.unlTireList.setCurrentRow(0)
        self.unlBodyList.setCurrentRow(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Edit Mii Data", None))
        self.warning.setText(QCoreApplication.translate("Dialog", u"This data is not editable.", None))
        self.unlGliderLabel.setText(QCoreApplication.translate("Dialog", u"Gliders", None))

        __sortingEnabled = self.unlGliderList.isSortingEnabled()
        self.unlGliderList.setSortingEnabled(False)
        ___qlistwidgetitem = self.unlGliderList.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Dialog", u"Standard", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem.setToolTip(QCoreApplication.translate("Dialog", u"This element cannot be unchecked.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem1 = self.unlGliderList.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Dialog", u"Paraglider / Parafoil", None));
        ___qlistwidgetitem2 = self.unlGliderList.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Dialog", u"Peach Parasol", None));
        ___qlistwidgetitem3 = self.unlGliderList.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Dialog", u"Flower Glider", None));
        ___qlistwidgetitem4 = self.unlGliderList.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("Dialog", u"Swooper / Swoop", None));
        ___qlistwidgetitem5 = self.unlGliderList.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("Dialog", u"Beast Glider / Ghastly Glider", None));
        ___qlistwidgetitem6 = self.unlGliderList.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("Dialog", u"Gold Glider", None));
        self.unlGliderList.setSortingEnabled(__sortingEnabled)

        self.unlCharLabel.setText(QCoreApplication.translate("Dialog", u"Characters", None))

        __sortingEnabled1 = self.unlCharList.isSortingEnabled()
        self.unlCharList.setSortingEnabled(False)
        ___qlistwidgetitem7 = self.unlCharList.item(0)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("Dialog", u"Mario", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem7.setToolTip(QCoreApplication.translate("Dialog", u"This element cannot be unchecked.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem8 = self.unlCharList.item(1)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("Dialog", u"Luigi", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem8.setToolTip(QCoreApplication.translate("Dialog", u"This element cannot be unchecked.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem9 = self.unlCharList.item(2)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("Dialog", u"Peach", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem9.setToolTip(QCoreApplication.translate("Dialog", u"This element cannot be unchecked.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem10 = self.unlCharList.item(3)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("Dialog", u"Yoshi", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem10.setToolTip(QCoreApplication.translate("Dialog", u"This element cannot be unchecked.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem11 = self.unlCharList.item(4)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("Dialog", u"Bowser", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem11.setToolTip(QCoreApplication.translate("Dialog", u"This element cannot be unchecked.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem12 = self.unlCharList.item(5)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("Dialog", u"Donkey Kong", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem12.setToolTip(QCoreApplication.translate("Dialog", u"This element cannot be unchecked.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem13 = self.unlCharList.item(6)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("Dialog", u"Toad", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem13.setToolTip(QCoreApplication.translate("Dialog", u"This element cannot be unchecked.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem14 = self.unlCharList.item(7)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("Dialog", u"Koopa Troopa", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem14.setToolTip(QCoreApplication.translate("Dialog", u"This element cannot be unchecked.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem15 = self.unlCharList.item(8)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("Dialog", u"Daisy", None));
        ___qlistwidgetitem16 = self.unlCharList.item(9)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("Dialog", u"Wario", None));
        ___qlistwidgetitem17 = self.unlCharList.item(10)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("Dialog", u"Rosalina", None));
        ___qlistwidgetitem18 = self.unlCharList.item(11)
        ___qlistwidgetitem18.setText(QCoreApplication.translate("Dialog", u"Metal Mario", None));
        ___qlistwidgetitem19 = self.unlCharList.item(12)
        ___qlistwidgetitem19.setText(QCoreApplication.translate("Dialog", u"Shy Guy", None));
        ___qlistwidgetitem20 = self.unlCharList.item(13)
        ___qlistwidgetitem20.setText(QCoreApplication.translate("Dialog", u"Honey Queen", None));
        ___qlistwidgetitem21 = self.unlCharList.item(14)
        ___qlistwidgetitem21.setText(QCoreApplication.translate("Dialog", u"Wiggler", None));
        ___qlistwidgetitem22 = self.unlCharList.item(15)
        ___qlistwidgetitem22.setText(QCoreApplication.translate("Dialog", u"Lakitu", None));
        ___qlistwidgetitem23 = self.unlCharList.item(16)
        ___qlistwidgetitem23.setText(QCoreApplication.translate("Dialog", u"Mii", None));
        self.unlCharList.setSortingEnabled(__sortingEnabled1)

        self.unlTireLabel.setText(QCoreApplication.translate("Dialog", u"Tires", None))

        __sortingEnabled2 = self.unlTireList.isSortingEnabled()
        self.unlTireList.setSortingEnabled(False)
        ___qlistwidgetitem24 = self.unlTireList.item(0)
        ___qlistwidgetitem24.setText(QCoreApplication.translate("Dialog", u"Standard / Normal", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem24.setToolTip(QCoreApplication.translate("Dialog", u"This element cannot be unchecked.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem25 = self.unlTireList.item(1)
        ___qlistwidgetitem25.setText(QCoreApplication.translate("Dialog", u"Monster", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem25.setToolTip(QCoreApplication.translate("Dialog", u"This element cannot be unchecked.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem26 = self.unlTireList.item(2)
        ___qlistwidgetitem26.setText(QCoreApplication.translate("Dialog", u"Roller", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem26.setToolTip(QCoreApplication.translate("Dialog", u"This element cannot be unchecked.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem27 = self.unlTireList.item(3)
        ___qlistwidgetitem27.setText(QCoreApplication.translate("Dialog", u"Slick", None));
        ___qlistwidgetitem28 = self.unlTireList.item(4)
        ___qlistwidgetitem28.setText(QCoreApplication.translate("Dialog", u"Slim", None));
        ___qlistwidgetitem29 = self.unlTireList.item(5)
        ___qlistwidgetitem29.setText(QCoreApplication.translate("Dialog", u"Sponge", None));
        ___qlistwidgetitem30 = self.unlTireList.item(6)
        ___qlistwidgetitem30.setText(QCoreApplication.translate("Dialog", u"Red Monster", None));
        ___qlistwidgetitem31 = self.unlTireList.item(7)
        ___qlistwidgetitem31.setText(QCoreApplication.translate("Dialog", u"Mushroom", None));
        ___qlistwidgetitem32 = self.unlTireList.item(8)
        ___qlistwidgetitem32.setText(QCoreApplication.translate("Dialog", u"Wood / Wooden", None));
        ___qlistwidgetitem33 = self.unlTireList.item(9)
        ___qlistwidgetitem33.setText(QCoreApplication.translate("Dialog", u"Gold Tires", None));
        self.unlTireList.setSortingEnabled(__sortingEnabled2)

        self.unlBodyLabel.setText(QCoreApplication.translate("Dialog", u"Karts", None))

        __sortingEnabled3 = self.unlBodyList.isSortingEnabled()
        self.unlBodyList.setSortingEnabled(False)
        ___qlistwidgetitem34 = self.unlBodyList.item(0)
        ___qlistwidgetitem34.setText(QCoreApplication.translate("Dialog", u"Standard Kart", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem34.setToolTip(QCoreApplication.translate("Dialog", u"This element cannot be unchecked.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem35 = self.unlBodyList.item(1)
        ___qlistwidgetitem35.setText(QCoreApplication.translate("Dialog", u"Bolt Buggy", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem35.setToolTip(QCoreApplication.translate("Dialog", u"This element cannot be unchecked.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem36 = self.unlBodyList.item(2)
        ___qlistwidgetitem36.setText(QCoreApplication.translate("Dialog", u"Birthday Girl / Royal Ribbon", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem36.setToolTip(QCoreApplication.translate("Dialog", u"This element cannot be unchecked.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem37 = self.unlBodyList.item(3)
        ___qlistwidgetitem37.setText(QCoreApplication.translate("Dialog", u"Egg 1", None));
        ___qlistwidgetitem38 = self.unlBodyList.item(4)
        ___qlistwidgetitem38.setText(QCoreApplication.translate("Dialog", u"Tiny Tug", None));
        ___qlistwidgetitem39 = self.unlBodyList.item(5)
        ___qlistwidgetitem39.setText(QCoreApplication.translate("Dialog", u"Cloud 9", None));
        ___qlistwidgetitem40 = self.unlBodyList.item(6)
        ___qlistwidgetitem40.setText(QCoreApplication.translate("Dialog", u"Zucchini / Gherkin", None));
        ___qlistwidgetitem41 = self.unlBodyList.item(7)
        ___qlistwidgetitem41.setText(QCoreApplication.translate("Dialog", u"B Dasher", None));
        ___qlistwidgetitem42 = self.unlBodyList.item(8)
        ___qlistwidgetitem42.setText(QCoreApplication.translate("Dialog", u"Bruiser / Growlster", None));
        ___qlistwidgetitem43 = self.unlBodyList.item(9)
        ___qlistwidgetitem43.setText(QCoreApplication.translate("Dialog", u"Bumble V", None));
        ___qlistwidgetitem44 = self.unlBodyList.item(10)
        ___qlistwidgetitem44.setText(QCoreApplication.translate("Dialog", u"Koopa Clown", None));
        ___qlistwidgetitem45 = self.unlBodyList.item(11)
        ___qlistwidgetitem45.setText(QCoreApplication.translate("Dialog", u"Pipe Frame", None));
        ___qlistwidgetitem46 = self.unlBodyList.item(12)
        ___qlistwidgetitem46.setText(QCoreApplication.translate("Dialog", u"Blue Seven", None));
        ___qlistwidgetitem47 = self.unlBodyList.item(13)
        ___qlistwidgetitem47.setText(QCoreApplication.translate("Dialog", u"Cact X", None));
        ___qlistwidgetitem48 = self.unlBodyList.item(14)
        ___qlistwidgetitem48.setText(QCoreApplication.translate("Dialog", u"Barrel Train", None));
        ___qlistwidgetitem49 = self.unlBodyList.item(15)
        ___qlistwidgetitem49.setText(QCoreApplication.translate("Dialog", u"Soda Jet", None));
        ___qlistwidgetitem50 = self.unlBodyList.item(16)
        ___qlistwidgetitem50.setText(QCoreApplication.translate("Dialog", u"Gold Standard Kart", None));
        self.unlBodyList.setSortingEnabled(__sortingEnabled3)

    # retranslateUi

