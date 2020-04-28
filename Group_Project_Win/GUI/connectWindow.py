import storage
import re
import GUI.Forms.connectWindowForm
from PyQt5 import QtWidgets, QtCore, QtGui


class ConnectWindow(QtWidgets.QDialog, GUI.Forms.connectWindowForm.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('База данных института')

        self.line_edit_ip.textChanged.connect(self.check_line_edit)
        self.line_edit_port.textChanged.connect(self.check_line_edit)
        self.button_connect.clicked.connect(self.button_connect_action)

        ip_range = "(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"
        self.ip_regex = '^{ip_r}\\.{ip_r}\\.{ip_r}\\.{ip_r}$'.format(ip_r=ip_range)
        self.line_edit_ip.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp(self.ip_regex)))
        self.line_edit_port.setValidator(QtGui.QIntValidator(0, 65535))

        self.check_line_edit()

    def check_line_edit(self):
        if re.fullmatch(self.ip_regex, self.line_edit_ip.text()) and len(self.line_edit_port.text()) > 0:
            self.button_connect.setEnabled(True)
            return
        self.button_connect.setEnabled(False)

    def button_connect_action(self):
        if storage.connect(self.line_edit_ip.text(), self.line_edit_port):
            self.close() ##################
        else:
            QtWidgets.QMessageBox.about(self, 'Ошибка', 'Не удалось подключиться к базе данных.'
                                                        '\nПроверьте данные и попробуйте снова.')