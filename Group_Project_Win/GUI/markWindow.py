import storage
import GUI.Forms.markWindowForm
from PyQt5 import QtWidgets
from GUI.abstract import check_student, check_discipline, check_statement


class MarkWindow(QtWidgets.QDialog, GUI.Forms.markWindowForm.Ui_Dialog):
    def __init__(self, parent, student, statement, discipline):
        super().__init__()
        self.setupUi(self)
        self.setModal(True)
        self.setWindowTitle('База данных аптеки')
        self.parent = parent
        self.student = student
        self.statement = statement
        self.discipline = discipline
        if self.statement[3] == storage.statement_exam.EXAM_NAME:
            self.label_head.setText(storage.statement_exam.EXAM_NAME.upper())
            for i in range(2, 6):
                self.combo_box_mark.addItem(str(i))
            if self.statement[2] is not None:
                self.combo_box_mark.setCurrentIndex(self.statement[2] - 2)
        else:
            self.label_head.setText(storage.statement_test.TEST_NAME.upper())
            self.combo_box_mark.addItem(storage.statement_test.MARK_TRUE)
            self.combo_box_mark.addItem(storage.statement_test.MARK_FALSE)
            if self.statement[2] is not None:
                if self.statement[2]:
                    self.combo_box_mark.setCurrentIndex(0)
                else:
                    self.combo_box_mark.setCurrentIndex(1)
        self.label_discipline.setText(self.discipline[1])

        self.button_ok.clicked.connect(self.button_ok_action)

    def button_ok_action(self):
        if check_student(self.student) \
                and check_statement(self.statement) \
                and check_discipline(self.discipline):
            if self.statement[3] == storage.statement_exam.EXAM_NAME:
                storage.statement_exam.set_mark(self.student[0],
                                                self.discipline[0],
                                                self.combo_box_mark.itemText(self.combo_box_mark.currentIndex()))
            else:
                if self.combo_box_mark.currentIndex() == 0:
                    storage.statement_test.set_mark(self.student[0], self.discipline[0], True)
                else:
                    storage.statement_test.set_mark(self.student[0], self.discipline[0], False)
        else:
            QtWidgets.QMessageBox.about(self, 'Ошибка', 'Данные более не актуальны.'
                                                        'Повторите попытку.')
        self.parent.update_tables()
        self.close()