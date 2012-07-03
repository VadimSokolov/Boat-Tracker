# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Jun 29 00:01:47 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 640)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridlayout = QtGui.QGridLayout(self.centralwidget)
        self.gridlayout.setMargin(9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.frameMap = QtGui.QFrame(self.centralwidget)
        self.frameMap.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameMap.setFrameShadow(QtGui.QFrame.Raised)
        self.frameMap.setObjectName(_fromUtf8("frameMap"))
        self.gridlayout.addWidget(self.frameMap, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMap = QtGui.QMenu(self.menubar)
        self.menuMap.setObjectName(_fromUtf8("menuMap"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.mpActionZoomIn = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/mActionZoomIn.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mpActionZoomIn.setIcon(icon1)
        self.mpActionZoomIn.setObjectName(_fromUtf8("mpActionZoomIn"))
        self.mpActionZoomOut = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/mActionZoomOut.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mpActionZoomOut.setIcon(icon2)
        self.mpActionZoomOut.setObjectName(_fromUtf8("mpActionZoomOut"))
        self.mpActionPan = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/mActionPan.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mpActionPan.setIcon(icon3)
        self.mpActionPan.setObjectName(_fromUtf8("mpActionPan"))
        self.mpActionAddLayer = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/mActionAddLayer.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mpActionAddLayer.setIcon(icon4)
        self.mpActionAddLayer.setObjectName(_fromUtf8("mpActionAddLayer"))
        self.menuMap.addAction(self.mpActionZoomIn)
        self.menuMap.addAction(self.mpActionZoomOut)
        self.menuMap.addAction(self.mpActionPan)
        self.menuMap.addAction(self.mpActionAddLayer)
        self.menubar.addAction(self.menuMap.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "BoatTracker", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMap.setTitle(QtGui.QApplication.translate("MainWindow", "Map", None, QtGui.QApplication.UnicodeUTF8))
        self.mpActionZoomIn.setText(QtGui.QApplication.translate("MainWindow", "Zoom In", None, QtGui.QApplication.UnicodeUTF8))
        self.mpActionZoomOut.setText(QtGui.QApplication.translate("MainWindow", "Zoom Out", None, QtGui.QApplication.UnicodeUTF8))
        self.mpActionPan.setText(QtGui.QApplication.translate("MainWindow", "Pan", None, QtGui.QApplication.UnicodeUTF8))
        self.mpActionAddLayer.setText(QtGui.QApplication.translate("MainWindow", "Add Layer", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
