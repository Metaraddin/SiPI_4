# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\editEmployeeWindowForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(506, 230)
        Dialog.setMinimumSize(QtCore.QSize(506, 230))
        Dialog.setMaximumSize(QtCore.QSize(16777215, 230))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_head = QtWidgets.QLabel(Dialog)
        self.label_head.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(18)
        self.label_head.setFont(font)
        self.label_head.setObjectName("label_head")
        self.verticalLayout.addWidget(self.label_head)
        spacerItem = QtWidgets.QSpacerItem(20, 21, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_discipline = QtWidgets.QLabel(Dialog)
        self.label_discipline.setMinimumSize(QtCore.QSize(149, 23))
        self.label_discipline.setMaximumSize(QtCore.QSize(149, 23))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(10)
        self.label_discipline.setFont(font)
        self.label_discipline.setObjectName("label_discipline")
        self.horizontalLayout.addWidget(self.label_discipline)
        self.line_edit_login = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(10)
        self.line_edit_login.setFont(font)
        self.line_edit_login.setObjectName("line_edit_login")
        self.horizontalLayout.addWidget(self.line_edit_login)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_discipline_2 = QtWidgets.QLabel(Dialog)
        self.label_discipline_2.setMinimumSize(QtCore.QSize(149, 23))
        self.label_discipline_2.setMaximumSize(QtCore.QSize(149, 23))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(10)
        self.label_discipline_2.setFont(font)
        self.label_discipline_2.setObjectName("label_discipline_2")
        self.horizontalLayout_2.addWidget(self.label_discipline_2)
        self.line_edit_name = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(10)
        self.line_edit_name.setFont(font)
        self.line_edit_name.setObjectName("line_edit_name")
        self.horizontalLayout_2.addWidget(self.line_edit_name)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_discipline_3 = QtWidgets.QLabel(Dialog)
        self.label_discipline_3.setMinimumSize(QtCore.QSize(149, 23))
        self.label_discipline_3.setMaximumSize(QtCore.QSize(149, 23))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(10)
        self.label_discipline_3.setFont(font)
        self.label_discipline_3.setObjectName("label_discipline_3")
        self.horizontalLayout_3.addWidget(self.label_discipline_3)
        self.line_edit_position = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(10)
        self.line_edit_position.setFont(font)
        self.line_edit_position.setObjectName("line_edit_position")
        self.horizontalLayout_3.addWidget(self.line_edit_position)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.label_error = QtWidgets.QLabel(Dialog)
        self.label_error.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(9)
        self.label_error.setFont(font)
        self.label_error.setObjectName("label_error")
        self.horizontalLayout_6.addWidget(self.label_error)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.button_ok = QtWidgets.QPushButton(Dialog)
        self.button_ok.setMinimumSize(QtCore.QSize(101, 23))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(10)
        self.button_ok.setFont(font)
        self.button_ok.setObjectName("button_ok")
        self.horizontalLayout_5.addWidget(self.button_ok)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_head.setText(_translate("Dialog", "ИЗМЕНИТЬ СОТРУДНИКА"))
        self.label_discipline.setText(_translate("Dialog", "ЛОГИН"))
        self.label_discipline_2.setText(_translate("Dialog", "ФИО"))
        self.label_discipline_3.setText(_translate("Dialog", "ДОЛЖНОСТЬ"))
        self.label_error.setText(_translate("Dialog", "ОШИБКА"))
        self.button_ok.setText(_translate("Dialog", "ГОТОВО"))
