# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\addDisciplineWindowForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(410, 151)
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
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_discipline = QtWidgets.QLabel(Dialog)
        self.label_discipline.setMinimumSize(QtCore.QSize(149, 23))
        self.label_discipline.setMaximumSize(QtCore.QSize(149, 23))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(10)
        self.label_discipline.setFont(font)
        self.label_discipline.setObjectName("label_discipline")
        self.horizontalLayout_2.addWidget(self.label_discipline)
        self.combo_box_discioline = QtWidgets.QComboBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(10)
        self.combo_box_discioline.setFont(font)
        self.combo_box_discioline.setObjectName("combo_box_discioline")
        self.horizontalLayout_2.addWidget(self.combo_box_discioline)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_mark = QtWidgets.QLabel(Dialog)
        self.label_mark.setMinimumSize(QtCore.QSize(149, 23))
        self.label_mark.setMaximumSize(QtCore.QSize(149, 23))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(10)
        self.label_mark.setFont(font)
        self.label_mark.setObjectName("label_mark")
        self.horizontalLayout.addWidget(self.label_mark)
        self.combo_box_mark = QtWidgets.QComboBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(10)
        self.combo_box_mark.setFont(font)
        self.combo_box_mark.setObjectName("combo_box_mark")
        self.combo_box_mark.addItem("")
        self.combo_box_mark.addItem("")
        self.horizontalLayout.addWidget(self.combo_box_mark)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.button_ok = QtWidgets.QPushButton(Dialog)
        self.button_ok.setMinimumSize(QtCore.QSize(101, 23))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(10)
        self.button_ok.setFont(font)
        self.button_ok.setObjectName("button_ok")
        self.horizontalLayout_3.addWidget(self.button_ok)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_head.setText(_translate("Dialog", "ДОБАВИТЬ ДИСЦИПЛИНУ"))
        self.label_discipline.setText(_translate("Dialog", "ДИСЦИПЛИНА"))
        self.label_mark.setText(_translate("Dialog", "ТИП ПРОВЕРКИ"))
        self.combo_box_mark.setItemText(0, _translate("Dialog", "Экзамен"))
        self.combo_box_mark.setItemText(1, _translate("Dialog", "Зачёт"))
        self.button_ok.setText(_translate("Dialog", "ДОБАВИТЬ"))
