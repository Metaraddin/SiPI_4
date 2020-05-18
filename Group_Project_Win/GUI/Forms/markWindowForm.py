# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\MarkWindowForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(351, 143)
        Dialog.setMinimumSize(QtCore.QSize(351, 143))
        Dialog.setMaximumSize(QtCore.QSize(16777215, 143))
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
        self.label_discipline = QtWidgets.QLabel(Dialog)
        self.label_discipline.setMinimumSize(QtCore.QSize(149, 23))
        self.label_discipline.setMaximumSize(QtCore.QSize(149, 23))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(10)
        self.label_discipline.setFont(font)
        self.label_discipline.setObjectName("label_discipline")
        self.verticalLayout.addWidget(self.label_discipline)
        self.combo_box_mark = QtWidgets.QComboBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(10)
        self.combo_box_mark.setFont(font)
        self.combo_box_mark.setObjectName("combo_box_mark")
        self.verticalLayout.addWidget(self.combo_box_mark)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.button_ok = QtWidgets.QPushButton(Dialog)
        self.button_ok.setMinimumSize(QtCore.QSize(101, 23))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(10)
        self.button_ok.setFont(font)
        self.button_ok.setObjectName("button_ok")
        self.horizontalLayout.addWidget(self.button_ok)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_head.setText(_translate("Dialog", "*ОЦЕНКА/ЗАЧЁТ*"))
        self.label_discipline.setText(_translate("Dialog", "*ДИСЦИПЛИНА*"))
        self.button_ok.setText(_translate("Dialog", "ВЫСТАВИТЬ"))
