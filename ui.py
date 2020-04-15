# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz_retimbre.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(694, 405)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.rutas = QtWidgets.QGroupBox(self.centralwidget)
        self.rutas.setGeometry(QtCore.QRect(10, 10, 671, 101))
        self.rutas.setTitle("")
        self.rutas.setObjectName("rutas")
        self.lbl_archivos_trab = QtWidgets.QLabel(self.rutas)
        self.lbl_archivos_trab.setGeometry(QtCore.QRect(10, 10, 131, 21))
        self.lbl_archivos_trab.setObjectName("lbl_archivos_trab")
        self.archivos_trab_ruta = QtWidgets.QLineEdit(self.rutas)
        self.archivos_trab_ruta.setGeometry(QtCore.QRect(150, 10, 481, 20))
        self.archivos_trab_ruta.setObjectName("archivos_trab_ruta")
        self.lbl_archivos = QtWidgets.QLabel(self.rutas)
        self.lbl_archivos.setGeometry(QtCore.QRect(10, 40, 131, 16))
        self.lbl_archivos.setObjectName("lbl_archivos")
        self.rutas_archivos = QtWidgets.QLineEdit(self.rutas)
        self.rutas_archivos.setGeometry(QtCore.QRect(150, 40, 481, 20))
        self.rutas_archivos.setObjectName("rutas_archivos")
        self.lbl_nombre_excel = QtWidgets.QLabel(self.rutas)
        self.lbl_nombre_excel.setGeometry(QtCore.QRect(10, 70, 131, 16))
        self.lbl_nombre_excel.setObjectName("lbl_nombre_excel")
        self.ruta_archivo_excel = QtWidgets.QLineEdit(self.rutas)
        self.ruta_archivo_excel.setGeometry(QtCore.QRect(150, 70, 431, 20))
        self.ruta_archivo_excel.setObjectName("ruta_archivo_excel")
        self.extencion_archivo = QtWidgets.QLineEdit(self.rutas)
        self.extencion_archivo.setEnabled(False)
        self.extencion_archivo.setGeometry(QtCore.QRect(590, 70, 41, 20))
        self.extencion_archivo.setObjectName("extencion_archivo")
        self.btn_comenzar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_comenzar.setGeometry(QtCore.QRect(280, 170, 151, 61))
        self.btn_comenzar.setObjectName("btn_comenzar")
        self.check_nom_comple = QtWidgets.QCheckBox(self.centralwidget)
        self.check_nom_comple.setGeometry(QtCore.QRect(10, 130, 171, 18))
        self.check_nom_comple.setObjectName("check_nom_comple")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Copy  Recibos - Timbres"))
        self.lbl_archivos_trab.setText(_translate("MainWindow", "ARCHIVOS EXCEL"))
        self.lbl_archivos.setText(_translate("MainWindow", "ARCHIVOS TXT Y XML"))
        self.lbl_nombre_excel.setText(_translate("MainWindow", "GUARDAR COMO(LAYOUT)"))
        self.extencion_archivo.setText(_translate("MainWindow", ".xlsx"))
        self.btn_comenzar.setText(_translate("MainWindow", "COMENZAR"))
        self.check_nom_comple.setText(_translate("MainWindow", "COMPLEMENTARIA"))
