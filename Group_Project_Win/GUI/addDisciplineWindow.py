import storage
import GUI.Forms.addDisciplineWindowForm
from PyQt5 import QtWidgets
from GUI.abstract import check_student


class AddDisciplineWindow(QtWidgets.QDialog, GUI.Forms.addDisciplineWindowForm.Ui_Dialog):
    def __init__(self, parent, student):
        super().__init__()
        self.setupUi(self)
        self.setModal(True)
        self.setWindowTitle('База данных аптеки')
        self.parent = parent
        self.student = student
        self.disciplines = None
        self.update()
        self.button_ok.clicked.connect(self.add)

    def update(self):
        self.combo_box_discioline.clear()
        self.disciplines = storage.discipline.get_all()
        id_list = (storage.statement_exam.get_student(self.student[0])
                   + storage.statement_test.get_student(self.student[0]))
        for i in range(len(id_list)): id_list[i] = id_list[i][0]
        i = 0
        while i < len(self.disciplines):
            if self.disciplines[i][0] in id_list:
                self.disciplines.pop(i)
            else:
                self.combo_box_discioline.addItem('ID %s, %s, %s семестр' % (self.disciplines[i][0],
                                                                             self.disciplines[i][1],
                                                                             self.disciplines[i][2]))
                i += 1

    def add(self):
        if check_student(self.student):
            discipline_id = self.disciplines[self.combo_box_discioline.currentIndex()][0]
            if self.combo_box_mark.currentIndex() == 0:
                storage.statement_exam.add(self.student[0], discipline_id, 'Null')
            else:
                storage.statement_test.add(self.student[0], discipline_id, 'Null')
            self.parent.update_tables()
            self.close()