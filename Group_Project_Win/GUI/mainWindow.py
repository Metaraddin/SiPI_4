import storage
import GUI.Forms.mainWindowForm
import copy
import datetime
from generator import Generator
from PyQt5 import QtWidgets, QtCore


def check_select_abstract_table(table):
    if table.currentColumn() != -1:
        return False
    return True


def set_abstract_table(table, labels):
    table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
    table.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
    table.verticalHeader().hide()
    table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
    table.setColumnCount(len(labels))
    table.setHorizontalHeaderLabels(labels)
    table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
    table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)


def sort_abstract_table(table, sort_flag, labels, column):
    local_labels = copy.deepcopy(labels)
    if sort_flag[column] is None or sort_flag[column] is False:
        table.sortItems(column)
        local_labels[column] = local_labels[column][:-1] + '↑'
        for i in range(len(sort_flag)):
            sort_flag[i] = None
        sort_flag[column] = True
    else:
        table.sortItems(column, QtCore.Qt.DescendingOrder)
        local_labels[column] = local_labels[column][:-1] + '↓'
        for i in range(len(sort_flag)):
            sort_flag[i] = None
        sort_flag[column] = False
    table.setHorizontalHeaderLabels(local_labels)


def resort_abstract_table(table, sort_flag):
    try:
        column = sort_flag.index(True)
        table.sortItems(column)
    except ValueError:
        try:
            column = sort_flag.index(False)
            table.sortItems(column, QtCore.Qt.DescendingOrder)
        except ValueError:
            pass


def update_abstract_table(table, data, **kwargs):
    table.clearContents()
    table.setRowCount(0)
    count = 0
    for i in range(len(data)):
        check = False
        for j in range(len(data[i])):
            if kwargs.get('filter', '').lower() in str(data[i][j]).lower():
                check = True
        if check:
            for j in range(len(data[i])):
                table.setRowCount(count + 1)
                item = data[i][j]
                if type(item) is bool:
                    if type:
                        table.setItem(count, j,
                                      QtWidgets.QTableWidgetItem(kwargs.get('boll_labels', ['False', 'True'])[1]))
                    else:
                        table.setItem(count, j,
                                      QtWidgets.QTableWidgetItem(kwargs.get('boll_labels', ['False', 'True'])[0]))
                elif type(item) is int:
                    table_item = QtWidgets.QTableWidgetItem()
                    table_item.setData(QtCore.Qt.EditRole, item)
                    table.setItem(count, j, table_item)
                else:
                    table.setItem(count, j, QtWidgets.QTableWidgetItem(data[i][j]))
            count += 1
    table.resizeColumnsToContents()


def check_sekect_abstract_table(table, *buttons):
    enabled = False
    if table.currentColumn() != -1:
        enabled = True
    for i in buttons:
        i.setEnabled(enabled)


class MainWindow(QtWidgets.QMainWindow, GUI.Forms.mainWindowForm.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('База данных института')

        self.current_group = None
        self.current_student = None

        self.tabWidget.currentChanged.connect(self.update_tables)

        self.labels_table_general = ['Номер  ', 'Факультет  ', 'Специальность  ', 'Год поступления  ']
        self.labels_table_disciplines = ['ID  ', 'Название  ', 'Семестр  ']
        self.labels_table_teachers = ['Логин  ', 'ФИО  ', 'Должность  ']
        self.labels_table_groups = ['ID  ', 'ФИО  ', 'Основа  ']
        self.labels_table_student = ['ID  ', 'Название  ', 'Способ оценивания  ', 'Оценка  ', 'Семестр  ']

        self.sort_flag_general = [None] * len(self.labels_table_general)
        self.sort_flag_disciplines = [None] * len(self.labels_table_disciplines)
        self.sort_flag_teachers = [None] * len(self.labels_table_teachers)
        self.sort_flag_groups = [None] * len(self.labels_table_groups)
        self.sort_flag_student = [None] * len(self.labels_table_student)

        self.table_general.horizontalHeader().sectionClicked.connect(self.sort_tables_general)
        self.table_disciplines.horizontalHeader().sectionClicked.connect(self.sort_tables_disciplines)
        self.table_teachers.horizontalHeader().sectionClicked.connect(self.sort_tables_teachers)
        self.table_groups.horizontalHeader().sectionClicked.connect(self.sort_tables_groups)
        self.table_student.horizontalHeader().sectionClicked.connect(self.sort_tables_student)

        self.table_general.itemSelectionChanged.connect(self.check_select_tables)
        self.table_disciplines.itemSelectionChanged.connect(self.check_select_tables)
        self.table_teachers.itemSelectionChanged.connect(self.check_select_tables)
        self.table_groups.itemSelectionChanged.connect(self.check_select_tables)
        self.table_student.itemSelectionChanged.connect(self.check_select_tables)

        self.table_general.cellDoubleClicked.connect(self.open_group)
        self.table_groups.cellDoubleClicked.connect(self.open_student)

        self.line_edit_search_general.textChanged.connect(self.update_tables)
        self.line_edit_search_disciplines.textChanged.connect(self.update_tables)
        self.line_edit_search_teachers.textChanged.connect(self.update_tables)
        self.line_edit_search_groups.textChanged.connect(self.update_tables)
        self.line_edit_search_student.textChanged.connect(self.update_tables)

        self.button_update_general.clicked.connect(self.update_tables)
        self.button_update_disciplines.clicked.connect(self.update_tables)
        self.button_update_teachers.clicked.connect(self.update_tables)
        self.button_update_groups.clicked.connect(self.update_tables)
        self.button_update_student.clicked.connect(self.update_tables)

        self.button_back_groups.clicked.connect(self.back_groups)
        self.button_back_student.clicked.connect(self.back_student)

        self.button_gen_general.clicked.connect(self.gen_tables)
        self.button_gen_disciplines.clicked.connect(self.gen_tables)
        self.button_gen_teachers.clicked.connect(self.gen_tables)
        self.button_gen_groups.clicked.connect(self.gen_tables)
        self.button_gen_student.clicked.connect(self.gen_tables)

        self.button_clear_general.clicked.connect(self.clear_general)
        self.button_clear_disciplines.clicked.connect(self.clear_disciplines)
        self.button_clear_teachers.clicked.connect(self.clear_teachers)

        self.button_delete_general.clicked.connect(self.delete_general)
        self.button_delete_disciplines.clicked.connect(self.delete_discipline)
        self.button_delete_teachers.clicked.connect(self.delete_teacher)
        self.button_delete_groups.clicked.connect(self.delete_group)
        self.button_delete_student.clicked.connect(self.delete_student)

        self.set_tables()

    def set_tables(self):
        set_abstract_table(self.table_general, self.labels_table_general)
        set_abstract_table(self.table_disciplines, self.labels_table_disciplines)
        set_abstract_table(self.table_teachers, self.labels_table_teachers)
        set_abstract_table(self.table_groups, self.labels_table_groups)
        set_abstract_table(self.table_student, self.labels_table_student)
        self.update_tables()
        self.sort_tables_general(2)
        self.sort_tables_disciplines(1)
        self.sort_tables_teachers(1)
        self.sort_tables_groups(1)
        self.sort_tables_student(2)

    def sort_tables_general(self, column):
        self.update_tables()
        sort_abstract_table(self.table_general, self.sort_flag_general, self.labels_table_general, column)

    def sort_tables_disciplines(self, column):
        self.update_tables()
        sort_abstract_table(self.table_disciplines, self.sort_flag_disciplines, self.labels_table_disciplines, column)

    def sort_tables_teachers(self, column):
        self.update_tables()
        sort_abstract_table(self.table_teachers, self.sort_flag_teachers, self.labels_table_teachers, column)

    def sort_tables_groups(self, column):
        self.update_tables()
        sort_abstract_table(self.table_groups, self.sort_flag_groups, self.labels_table_groups, column)

    def sort_tables_student(self, column):
        self.update_tables()
        sort_abstract_table(self.table_student, self.sort_flag_student, self.labels_table_student, column)

    def resort_tables(self):
        resort_abstract_table(self.table_general, self.sort_flag_general)
        resort_abstract_table(self.table_disciplines, self.sort_flag_disciplines)
        resort_abstract_table(self.table_teachers, self.sort_flag_teachers)
        resort_abstract_table(self.table_groups, self.sort_flag_groups)
        resort_abstract_table(self.table_student, self.sort_flag_student)

    def update_tables(self):
        text = datetime.datetime.now().strftime("ПОСЛЕДНЕЕ ОБНОВЛЕНИЕ: <b>%H:%M:%S</b>")
        update_abstract_table(self.table_general, storage.groups.get_all(),
                              filter=self.line_edit_search_general.text())
        self.table_general.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.label_update_general.setText(text)
        update_abstract_table(self.table_disciplines, storage.discipline.get_all(),
                              filter=self.line_edit_search_disciplines.text())
        self.table_disciplines.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.label_update_disciplines.setText(text)
        update_abstract_table(self.table_teachers, storage.employee.get_all(),
                              filter=self.line_edit_search_teachers.text())
        self.table_teachers.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.label_update_teachers.setText(text)
        if self.current_group is not None:
            groups = storage.groups.get_group(self.current_group[0])
            if len(groups) <= 0:
                self.current_group = None
                if self.stackedWidget.currentIndex() != 0:
                    self.stackedWidget.setCurrentIndex(0)
            else:
                self.current_group = groups[0]
                self.label_head_groups.setText('Группа №%s' % self.current_group[0])
                update_abstract_table(self.table_groups, storage.student.get_group(self.current_group[0]),
                                      filter=self.line_edit_search_student.text(), boll_labels=['Коммерция', 'Бюджет'])
                self.table_groups.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
                self.label_update_groups.setText(text)
        if self.current_student is not None:
            students = storage.student.get_student(self.current_student[0])
            if len(students) <= 0:
                self.current_student = None
                if self.stackedWidget.currentIndex() > 1:
                    self.stackedWidget.setCurrentIndex(1)
            else:
                self.current_student = students[0]
                self.label_head_student.setText(str(self.current_student[2]))
                update_abstract_table(self.table_student,
                                      storage.statement_exam.get_student(self.current_student[0]) +
                                      storage.statement_test.get_student(self.current_student[0]),
                                      filter=self.line_edit_search_student.text(),
                                      boll_labels=['Незачет', 'Зачет'])
                self.table_student.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
                self.label_update_student.setText(text)
        self.resort_tables()
        self.check_select_tables()

    def check_select_tables(self):
        check_sekect_abstract_table(self.table_general, self.button_delete_general, self.button_edit_general)
        check_sekect_abstract_table(self.table_disciplines,
                                    self.button_edit_disciplines, self.button_delete_disciplines)
        check_sekect_abstract_table(self.table_teachers, self.button_delete_teachers, self.button_edit_teachers)
        check_sekect_abstract_table(self.table_groups, self.button_edit_groups, self.button_delete_groups)
        check_sekect_abstract_table(self.table_student, self.button_delete_student)

    def open_group(self, cell):
        groups = storage.groups.get_group(self.table_general.item(cell, 0).text())
        if len(groups) > 0:
            self.line_edit_search_general.clear()
            self.current_group = groups[0]
            self.update_tables()
            self.stackedWidget.setCurrentIndex(1)
        else:
            QtWidgets.QMessageBox.about(self, 'Ошибка', 'Данная группа была удалёна'
                                                        'или изменена другим пользователем.')

    def open_student(self, cell):
        students = storage.student.get_student(self.table_groups.item(cell, 0).text())
        if len(students) > 0:
            self.line_edit_search_groups.clear()
            self.current_student = students[0]
            self.update_tables()
            self.stackedWidget.setCurrentIndex(2)
        else:
            QtWidgets.QMessageBox.about(self, 'Ошибка', 'Данный студент был удалён'
                                                        'или изменён другим пользователем.')

    def back_groups(self):
        self.line_edit_search_groups.clear()
        self.current_group = None
        self.update_tables()
        self.stackedWidget.setCurrentIndex(0)

    def back_student(self):
        self.line_edit_search_student.clear()
        self.current_student = None
        self.update_tables()
        self.stackedWidget.setCurrentIndex(1)

    def gen_tables(self):
        self.update_tables()
        message = "Вы хотите заполнить базу данных тестовыми значениями?" \
                  "\nЭто удалит все текущие записи и сбросит индексы."
        button_reply = QtWidgets.QMessageBox.question(self, 'Генерация', message,
                                                      QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if button_reply == QtWidgets.QMessageBox.Yes:
            Generator(30)
        self.update_tables()

    def clear_abstract_table(self, storage_table):
        self.update_tables()
        message = "Вы хотите очистить таблицу базы данных?" \
                  "\nЭто действие нельзя отменить." \
                  "\nИндексы сброшены не будут."
        button_reply = QtWidgets.QMessageBox.question(self, 'Очищение', message,
                                                      QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if button_reply == QtWidgets.QMessageBox.Yes:
            storage_table.clear()
        self.update_tables()

    def clear_general(self):
        self.clear_abstract_table(storage.groups)

    def clear_disciplines(self):
        self.clear_abstract_table(storage.discipline)

    def clear_teachers(self):
        self.clear_abstract_table(storage.employee)

    def delete_abstract(self, storage_table, *keys):
        self.update_tables()
        message = "Вы хотите удалить запись из базы данных?" \
                  "\nЭто действие нельзя отменить."
        button_reply = QtWidgets.QMessageBox.question(self, 'Удаление', message,
                                                      QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if button_reply == QtWidgets.QMessageBox.Yes:
            if len(keys) == 1:
                storage_table.delete(keys[0])
            else:
                storage_table.delete(keys[0], keys[1])
        self.update_tables()

    def delete_discipline(self):
        self.delete_abstract(storage.discipline,
                             self.table_disciplines.item(self.table_disciplines.currentRow(), 0).text())

    def delete_teacher(self):
        self.delete_abstract(storage.employee, self.table_teachers.item(self.table_teachers.currentRow(), 0).text())

    def delete_general(self):
        self.delete_abstract(storage.groups, self.table_general.item(self.table_general.currentRow(), 0).text())

    def delete_group(self):
        self.delete_abstract(storage.student, self.table_groups.item(self.table_groups.currentRow(), 0).text())

    def delete_student(self):
        student_id = self.current_student[0]
        discipline_id = self.table_student.item(self.table_student.currentRow(), 0).text()
        if self.table_student.item(self.table_student.currentRow(), 2).text() == 'Экзамен':
            self.delete_abstract(storage.statement_exam, student_id, discipline_id)
        else:
            self.delete_abstract(storage.statement_test, student_id, discipline_id)