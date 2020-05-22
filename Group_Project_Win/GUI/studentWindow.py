import storage
import GUI.Forms.studentWindowForm
from PyQt5 import QtWidgets
from GUI.abstract import check_group, check_student


class StudentWindow(QtWidgets.QDialog, GUI.Forms.studentWindowForm.Ui_Dialog):
    def __init__(self, parent, group, student=None):
        super().__init__()
        self.setupUi(self)
        self.setModal(True)
        self.setWindowTitle('База данных аптеки')
        self.parent = parent
        self.group = group
        self.student = student
        self.combo_box_discioline.addItem('Коммерция')
        self.combo_box_discioline.addItem('Бюджет')
        self.check_line_edit()

        self.line_edit_fname.textChanged.connect(self.check_line_edit)

        if student is not None:
            self.label_head.setText('ИЗМЕНИТЬ СТУДЕНТА')
            self.line_edit_fname.setText(str(self.student[2]))
            if self.student[3]:
                self.combo_box_discioline.setCurrentIndex(0)
            else:
                self.combo_box_discioline.setCurrentIndex(1)

        self.button_ok.clicked.connect(self.button_ok_action)

    def check_line_edit(self):
        def check_error():
            check = True
            if len(self.line_edit_fname.text()) <= 0:
                check = False
            elif len(self.line_edit_fname.text()) > 90:
                self.label_error.setText('ФИО СЛИШКОМ ДЛИННОЕ')
                return False
            self.label_error.setText('')
            return check

        self.button_ok.setEnabled(check_error())

    def button_ok_action(self):
        if check_group(self.group):
            if self.combo_box_discioline.currentIndex() == 0:
                basis = True
            else: basis = False
            full_name = self.line_edit_fname.text()
            if self.student is None:
                storage.student.add(self.group[0], full_name, basis)
            else:
                if check_student(self.student):
                    storage.student.set(self.student[0], full_name, basis)
                else:
                    QtWidgets.QMessageBox.about(self, 'Ошибка', 'Данные более не актуальны.'
                                                                'Повторите попытку.')
        else:
            QtWidgets.QMessageBox.about(self, 'Ошибка', 'Данные более не актуальны.'
                                                        'Повторите попытку.')
        self.parent.update_tables()
        self.close()
