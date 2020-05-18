import storage
import GUI.Forms.markWindowForm
from PyQt5 import QtWidgets


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
