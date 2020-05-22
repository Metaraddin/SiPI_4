import storage
import GUI.Forms.groupWindowForm
from PyQt5 import QtWidgets
from GUI.abstract import check_group


class GroupWindow(QtWidgets.QDialog, GUI.Forms.groupWindowForm.Ui_Dialog):
    def __init__(self, parent, group=None):
        super().__init__()
        self.setupUi(self)
        self.setModal(True)
        self.setWindowTitle('База данных аптеки')
        self.parent = parent
        self.group = group

        self.spin_box_year.setMinimum(1900)
        self.spin_box_year.setMaximum(2999)

        if self.group is not None:
            self.label_head.setText('ИЗМЕНИТЬ ГРУППУ')
            self.line_edit_faculty.setText(str(self.group[1]))
            self.line_edit_specialty.setText(str(self.group[2]))
            self.spin_box_year.setValue(int(self.group[3]))

        self.button_ok.clicked.connect(self.button_ok_action)
        self.line_edit_specialty.textChanged.connect(self.check_line_edit)
        self.line_edit_faculty.textChanged.connect(self.check_line_edit)
        self.check_line_edit()

    def check_line_edit(self):
        def check_error():
            check = True
            if len(self.line_edit_faculty.text()) <= 0:
                check = False
            elif len(self.line_edit_faculty.text()) > 60:
                self.label_error.setText('НАПРАВЛЕНИЕ СЛИШКОМ ДЛИННОЕ')
                return False
            if len(self.line_edit_specialty.text()) <= 0:
                check = False
            elif len(self.line_edit_specialty.text()) > 60:
                self.label_error.setText('СПЕЦИАЛЬНОСТЬ СЛИШКОМ ДЛИННАЯ')
                return False
            self.label_error.setText('')
            return check

        self.button_ok.setEnabled(check_error())

    def button_ok_action(self):
        faculty = self.line_edit_faculty.text()
        specialty = self.line_edit_specialty.text()
        year = self.spin_box_year.value()

        if self.group is None:
            storage.groups.add(faculty, specialty, year)
        else:
            if check_group(self.group):
                id = self.group[0]
                storage.groups.set(id, faculty, specialty, year)
            else:
                QtWidgets.QMessageBox.about(self, 'Ошибка', 'Данные более не актуальны.\n'
                                                            'Повторите попытку.')
        self.parent.update_tables()
        self.close()
