# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/jesus/OneDrive/Masaüstü/PyQt5/PROJELER/DERS PRO/QmesageBox/untitled.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(525, 342)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/İcosn/IMG_20200704_171826.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(20, 20))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 501, 281))
        self.groupBox.setObjectName("groupBox")
        self.splitter = QtWidgets.QSplitter(self.groupBox)
        self.splitter.setGeometry(QtCore.QRect(0, 20, 71, 81))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.pbt_critical = QtWidgets.QPushButton(self.splitter)
        self.pbt_critical.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/İcosn/error.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbt_critical.setIcon(icon1)
        self.pbt_critical.setIconSize(QtCore.QSize(40, 60))
        self.pbt_critical.setObjectName("pbt_critical")
        self.label = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.splitter_2 = QtWidgets.QSplitter(self.groupBox)
        self.splitter_2.setGeometry(QtCore.QRect(210, 20, 91, 71))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.pbt_information = QtWidgets.QPushButton(self.splitter_2)
        self.pbt_information.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/İcosn/information.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbt_information.setIcon(icon2)
        self.pbt_information.setIconSize(QtCore.QSize(40, 50))
        self.pbt_information.setObjectName("pbt_information")
        self.label_4 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.splitter_3 = QtWidgets.QSplitter(self.groupBox)
        self.splitter_3.setGeometry(QtCore.QRect(410, 20, 71, 71))
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.pbt_qeston = QtWidgets.QPushButton(self.splitter_3)
        self.pbt_qeston.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/İcosn/question.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbt_qeston.setIcon(icon3)
        self.pbt_qeston.setIconSize(QtCore.QSize(20, 50))
        self.pbt_qeston.setObjectName("pbt_qeston")
        self.pbt = QtWidgets.QLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pbt.setFont(font)
        self.pbt.setObjectName("pbt")
        self.splitter_4 = QtWidgets.QSplitter(self.groupBox)
        self.splitter_4.setGeometry(QtCore.QRect(0, 150, 81, 81))
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.pbt_warming = QtWidgets.QPushButton(self.splitter_4)
        self.pbt_warming.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/İcosn/warning (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbt_warming.setIcon(icon4)
        self.pbt_warming.setIconSize(QtCore.QSize(40, 50))
        self.pbt_warming.setObjectName("pbt_warming")
        self.label_6 = QtWidgets.QLabel(self.splitter_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.splitter_5 = QtWidgets.QSplitter(self.groupBox)
        self.splitter_5.setGeometry(QtCore.QRect(200, 150, 71, 81))
        self.splitter_5.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5.setObjectName("splitter_5")
        self.pbt_about = QtWidgets.QPushButton(self.splitter_5)
        self.pbt_about.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/İcosn/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbt_about.setIcon(icon5)
        self.pbt_about.setIconSize(QtCore.QSize(40, 50))
        self.pbt_about.setObjectName("pbt_about")
        self.label_7 = QtWidgets.QLabel(self.splitter_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.splitter_6 = QtWidgets.QSplitter(self.groupBox)
        self.splitter_6.setGeometry(QtCore.QRect(410, 150, 71, 81))
        self.splitter_6.setOrientation(QtCore.Qt.Vertical)
        self.splitter_6.setObjectName("splitter_6")
        self.pbt_ozel = QtWidgets.QPushButton(self.splitter_6)
        self.pbt_ozel.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/İcosn/123.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbt_ozel.setIcon(icon6)
        self.pbt_ozel.setIconSize(QtCore.QSize(40, 50))
        self.pbt_ozel.setObjectName("pbt_ozel")
        self.label_8 = QtWidgets.QLabel(self.splitter_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 525, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QmesageBox"))
        self.groupBox.setTitle(_translate("MainWindow", "QmesageBook"))
        self.label.setText(_translate("MainWindow", "Critical"))
        self.label_4.setText(_translate("MainWindow", "Information"))
        self.pbt.setText(_translate("MainWindow", "Qestion"))
        self.label_6.setText(_translate("MainWindow", "Warming"))
        self.label_7.setText(_translate("MainWindow", "About"))
        self.label_8.setText(_translate("MainWindow", "Özel"))

import icosn_rc
