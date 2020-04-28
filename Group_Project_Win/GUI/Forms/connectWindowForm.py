# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\connectWindowForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(330, 137)
        Dialog.setMinimumSize(QtCore.QSize(330, 137))
        Dialog.setMaximumSize(QtCore.QSize(330, 137))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_head = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(18)
        self.label_head.setFont(font)
        self.label_head.setObjectName("label_head")
        self.verticalLayout_3.addWidget(self.label_head)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.layout_ip = QtWidgets.QVBoxLayout()
        self.layout_ip.setObjectName("layout_ip")
        self.label_ip = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(10)
        self.label_ip.setFont(font)
        self.label_ip.setObjectName("label_ip")
        self.layout_ip.addWidget(self.label_ip)
        self.line_edit_ip = QtWidgets.QLineEdit(Dialog)
        self.line_edit_ip.setMinimumSize(QtCore.QSize(201, 23))
        self.line_edit_ip.setMaximumSize(QtCore.QSize(201, 23))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(10)
        self.line_edit_ip.setFont(font)
        self.line_edit_ip.setText("")
        self.line_edit_ip.setObjectName("line_edit_ip")
        self.layout_ip.addWidget(self.line_edit_ip)
        self.horizontalLayout.addLayout(self.layout_ip)
        self.layout_port = QtWidgets.QVBoxLayout()
        self.layout_port.setObjectName("layout_port")
        self.label_port = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(10)
        self.label_port.setFont(font)
        self.label_port.setObjectName("label_port")
        self.layout_port.addWidget(self.label_port)
        self.line_edit_port = QtWidgets.QLineEdit(Dialog)
        self.line_edit_port.setMinimumSize(QtCore.QSize(50, 23))
        self.line_edit_port.setMaximumSize(QtCore.QSize(99, 23))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(10)
        self.line_edit_port.setFont(font)
        self.line_edit_port.setText("")
        self.line_edit_port.setObjectName("line_edit_port")
        self.layout_port.addWidget(self.line_edit_port)
        self.horizontalLayout.addLayout(self.layout_port)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.layout_button = QtWidgets.QHBoxLayout()
        self.layout_button.setObjectName("layout_button")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_button.addItem(spacerItem)
        self.button_connect = QtWidgets.QPushButton(Dialog)
        self.button_connect.setMinimumSize(QtCore.QSize(141, 25))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(10)
        self.button_connect.setFont(font)
        self.button_connect.setObjectName("button_connect")
        self.layout_button.addWidget(self.button_connect)
        self.verticalLayout_3.addLayout(self.layout_button)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_head.setText(_translate("Dialog", "ПОДКЛЮЧЕНИЕ"))
        self.label_ip.setText(_translate("Dialog", "IP АДРЕС"))
        self.label_port.setText(_translate("Dialog", "ПОРТ"))
        self.button_connect.setText(_translate("Dialog", "ПОДКЛЮЧИТЬСЯ"))
