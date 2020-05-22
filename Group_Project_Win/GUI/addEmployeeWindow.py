import storage
import GUI.Forms.addEmployeeWindowForm
from PyQt5 import QtWidgets


class AddEmployeeWindow(QtWidgets.QDialog, GUI.Forms.addEmployeeWindowForm.Ui_Dialog):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.setModal(True)
        self.setWindowTitle('База данных аптеки')
        self.parent = parent

        self.button_ok.clicked.connect(self.button_ok_action)
        self.line_edit_login.textChanged.connect(self.check_line_edit)
        self.line_edit_password.textChanged.connect(self.check_line_edit)
        self.line_edit_name.textChanged.connect(self.check_line_edit)
        self.line_edit_position.textChanged.connect(self.check_line_edit)
        self.check_line_edit()

    def check_line_edit(self):
        def check_error():
            check = True
            if len(self.line_edit_login.text()) <= 0:
                check = False
            elif len(self.line_edit_login.text()) > 30:
                self.label_error.setText('ЛОГИН СЛИШКОМ ДЛИННЫЙ')
                return False
            if len(self.line_edit_password.text()) <= 0:
                check = False
            elif len(self.line_edit_password.text()) > 30:
                self.label_error.setText('ПАРОЛЬ СЛИШКОМ ДЛИННЫЙ')
                return False
            if len(self.line_edit_name.text()) <= 0:
                check = False
            elif len(self.line_edit_name.text()) > 90:
                self.label_error.setText('ФИО СЛИШКОМ ДЛИННОЕ')
                return False
            if len(self.line_edit_position.text()) <= 0:
                check = False
            elif len(self.line_edit_position.text()) > 30:
                self.label_error.setText('ДОЖНОСТЬ СЛИШКОМ ДЛИННАЯ')
                return False
            self.label_error.setText('')
            return check

        self.button_ok.setEnabled(check_error())

    def button_ok_action(self):
        login = self.line_edit_login.text()
        password = self.line_edit_password.text()
        name = self.line_edit_name.text()
        position = self.line_edit_position.text()

        storage.employee.add(login, password, name, position)

        self.parent.update_tables()
        self.close()
