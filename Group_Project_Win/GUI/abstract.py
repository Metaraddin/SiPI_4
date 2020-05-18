from PyQt5 import QtWidgets, QtCore
import storage
import copy


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
                    if item:
                        table.setItem(count, j,
                                      QtWidgets.QTableWidgetItem(kwargs.get('bool_labels', ['False', 'True'])[1]))
                    else:
                        table.setItem(count, j,
                                      QtWidgets.QTableWidgetItem(kwargs.get('bool_labels', ['False', 'True'])[0]))
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


def check_student(student):
    students = storage.student.get_student(student[0])
    if len(students) > 0 and students[0] == student:
        return True
    return False


def check_discipline(discipline):
    disciplines = storage.discipline.get_discipline(discipline[0])
    if len(disciplines) > 0 and disciplines[0] == discipline:
        return True
    return False


def check_statement(statement):
    statements_test = storage.statement_test.get(statement[0], statement[1])
    if len(statements_test) > 0 and statements_test[0] == statement:
        return True
    statements_exam = storage.statement_exam.get(statement[0], statement[1])
    if len(statements_exam) > 0 and statements_exam[0] == statement:
        return True
    return False
