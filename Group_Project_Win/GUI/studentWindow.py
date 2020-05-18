import storage
import GUI.Forms.studentWindowForm
from PyQt5 import QtWidgets
from GUI.abstract import check_student


class StudentWindow(QtWidgets.QDialog, GUI.Forms.studentWindowForm.Ui_Dialog):
    def __init__(self, parent, student=None):
        super().__init__()
        self.setupUi(self)
        self.setModal(True)
        self.setWindowTitle('База данных аптеки')
        self.parent = parent
        self.student = student
        self.combo_box_discioline.addItem('Бюджет')
        self.combo_box_discioline.addItem('Коммерция')

        if student is not None:
            self.line_edit_fname.setText(self.student[1])
            self.line_edit_lname.setText(self.student[2])
            self.line_edit_llname.setText(self.student[3])
            if self.student[4]:
                self.combo_box_discioline.setCurrentIndex(0)
            else:
                self.combo_box_discioline.setCurrentIndex(1)

        self.button_ok.clicked.connect(self.button_ok_action)

    def button_ok_action(self):
        return 0
