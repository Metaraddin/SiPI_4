# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\studentWindowForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(498, 217)
        Dialog.setMinimumSize(QtCore.QSize(498, 217))
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
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
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
        self.line_edit_fname = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(10)
        self.line_edit_fname.setFont(font)
        self.line_edit_fname.setObjectName("line_edit_fname")
        self.horizontalLayout.addWidget(self.line_edit_fname)
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
        self.line_edit_lname = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(10)
        self.line_edit_lname.setFont(font)
        self.line_edit_lname.setObjectName("line_edit_lname")
        self.horizontalLayout_2.addWidget(self.line_edit_lname)
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
        self.line_edit_llname = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(10)
        self.line_edit_llname.setFont(font)
        self.line_edit_llname.setObjectName("line_edit_llname")
        self.horizontalLayout_3.addWidget(self.line_edit_llname)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_discipline_4 = QtWidgets.QLabel(Dialog)
        self.label_discipline_4.setMinimumSize(QtCore.QSize(149, 23))
        self.label_discipline_4.setMaximumSize(QtCore.QSize(149, 23))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(10)
        self.label_discipline_4.setFont(font)
        self.label_discipline_4.setObjectName("label_discipline_4")
        self.horizontalLayout_4.addWidget(self.label_discipline_4)
        self.combo_box_discioline = QtWidgets.QComboBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(10)
        self.combo_box_discioline.setFont(font)
        self.combo_box_discioline.setObjectName("combo_box_discioline")
        self.horizontalLayout_4.addWidget(self.combo_box_discioline)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
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
        self.label_head.setText(_translate("Dialog", "ДОБАВИТЬ СТУДЕНТА"))
        self.label_discipline.setText(_translate("Dialog", "ИМЯ"))
        self.label_discipline_2.setText(_translate("Dialog", "ФАМИЛИЯ"))
        self.label_discipline_3.setText(_translate("Dialog", "ОТЧЕСТВО"))
        self.label_discipline_4.setText(_translate("Dialog", "ОСНОВА"))
        self.button_ok.setText(_translate("Dialog", "ДОБАВИТЬ"))
