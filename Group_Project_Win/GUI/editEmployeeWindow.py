import storage
import GUI.Forms.editEmployeeWindowForm
from PyQt5 import QtWidgets
from GUI.abstract import check_employee


class EditEmployeeWindow(QtWidgets.QDialog, GUI.Forms.editEmployeeWindowForm.Ui_Dialog):
    def __init__(self, parent, employee):
        super().__init__()
        self.setupUi(self)
        self.setModal(True)
        self.setWindowTitle('База данных аптеки')
        self.parent = parent
        self.employee = employee

        self.line_edit_login.setText(self.employee[0])
        self.line_edit_name.setText(self.employee[1])
        self.line_edit_position.setText(self.employee[2])

        self.button_ok.clicked.connect(self.button_ok_action)

        self.line_edit_login.textChanged.connect(self.check_line_edit)
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
        if check_employee(self.employee):
            last_login = self.employee[0]
            login = self.line_edit_login.text()
            name = self.line_edit_name.text()
            position = self.line_edit_position.text()

            storage.employee.set(last_login, login, name, position)
        else:
            QtWidgets.QMessageBox.about(self, 'Ошибка', 'Данные более не актуальны.\n'
                                                        'Повторите попытку.')

        self.parent.update_tables()
        self.close()
