import storage
import GUI.Forms.disciplineWindowForm
from PyQt5 import QtWidgets
from GUI.abstract import check_discipline


class DisciplineWindow(QtWidgets.QDialog, GUI.Forms.disciplineWindowForm.Ui_Dialog):
    def __init__(self, parent, discipline=None):
        super().__init__()
        self.setupUi(self)
        self.setModal(True)
        self.setWindowTitle('База данных аптеки')
        self.parent = parent
        self.discipline = discipline

        self.spin_box_semester.setMinimum(1)
        self.spin_box_semester.setMaximum(8)

        if self.discipline is not None:
            self.label_head.setText('ИЗМЕНИТЬ ДИСЦИПЛИНУ')
            self.line_edit_name.setText(str(self.discipline[1]))
            self.spin_box_semester.setValue(int(self.discipline[2]))

        self.button_ok.clicked.connect(self.button_ok_action)
        self.line_edit_name.textChanged.connect(self.check_line_edit)
        self.check_line_edit()

    def check_line_edit(self):
        def check_error():
            check = True
            if len(self.line_edit_name.text()) <= 0:
                check = False
            elif len(self.line_edit_name.text()) > 60:
                self.label_error.setText('НАЗВАНИЕ СЛИШКОМ ДЛИННОЕ')
                return False
            self.label_error.setText('')
            return check

        self.button_ok.setEnabled(check_error())

    def button_ok_action(self):
        name = self.line_edit_name.text()
        semester = self.spin_box_semester.value()

        if self.discipline is None:
            storage.discipline.add(name, semester)
        else:
            if check_discipline(self.discipline):
                id = self.discipline[0]
                storage.discipline.set(id, name, semester)
            else:
                QtWidgets.QMessageBox.about(self, 'Ошибка', 'Данные более не актуальны.\n'
                                                            'Повторите попытку.')
        self.parent.update_tables()
        self.close()
