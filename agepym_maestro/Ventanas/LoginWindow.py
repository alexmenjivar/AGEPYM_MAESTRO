# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Chris\Desktop\CICLO VIII\DSI\Windows\LoginWindow.ui'
#
# Created: Sat Aug 24 16:59:07 2013
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from Utils.Constantes import absPath

class Ui_LogInWindow(object):
    def setupUi(self, LogInWindow):
        LogInWindow.setObjectName("LogInWindow")
        LogInWindow.resize(640, 404)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LogInWindow.sizePolicy().hasHeightForWidth())
        LogInWindow.setSizePolicy(sizePolicy)
        LogInWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtGui.QWidget(LogInWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.fotoLbl = QtGui.QLabel(self.widget)
        self.fotoLbl.setText("")
        self.fotoLbl.setPixmap(QtGui.QPixmap(absPath("archivos/imagenes/images.jpg")))
        self.fotoLbl.setObjectName("fotoLbl")
        self.gridLayout.addWidget(self.fotoLbl, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 2, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.widget)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.usuarioTxt = QtGui.QLineEdit(self.centralwidget)
        self.usuarioTxt.setObjectName("usuarioTxt")
        self.verticalLayout_2.addWidget(self.usuarioTxt)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.contraTxt = QtGui.QLineEdit(self.centralwidget)
        self.contraTxt.setObjectName("contraTxt")
        self.verticalLayout_2.addWidget(self.contraTxt)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.widget_2 = QtGui.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.aceptarBtn = QtGui.QPushButton(self.widget_2)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(absPath("archivos/imagenes/ok.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.aceptarBtn.setIcon(icon)
        self.aceptarBtn.setObjectName("aceptarBtn")
        self.horizontalLayout.addWidget(self.aceptarBtn)
        self.cancelarBtn = QtGui.QPushButton(self.widget_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(absPath("archivos/imagenes/cancel.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelarBtn.setIcon(icon1)
        self.cancelarBtn.setObjectName("cancelarBtn")
        self.horizontalLayout.addWidget(self.cancelarBtn)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        LogInWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LogInWindow)
        QtCore.QMetaObject.connectSlotsByName(LogInWindow)

    def retranslateUi(self, LogInWindow):
        LogInWindow.setWindowTitle(QtGui.QApplication.translate("LogInWindow", "MAESTRO - Iniciar Sesión", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("LogInWindow", "Usuario:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("LogInWindow", "Contraseña: ", None, QtGui.QApplication.UnicodeUTF8))
        self.aceptarBtn.setText(QtGui.QApplication.translate("LogInWindow", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelarBtn.setText(QtGui.QApplication.translate("LogInWindow", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

