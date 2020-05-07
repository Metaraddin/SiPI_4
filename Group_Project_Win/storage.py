import sys
import psycopg2 as psql
from Database.database import Database
from Database.students import Student
from Database.groups import Groups
from Database.statement_exam import StatementExam
from Database.statement_test import StatementTest
from Database.employee import Employee
from Database.discipline import Discipline
from gen_new import generator
from PyQt5 import QtWidgets, QtGui, QtCore

groups = None
student = None
discipline = None
statement_exam = None
statement_test = None
employee = None


def connect(ip, port):
    global student, groups, statement_exam, statement_test, discipline, employee
    try:
        database = Database('sipi_gp', 'client_gp', 'client', ip, port)
    except psql.OperationalError:
        return False
    groups = Groups(database)
    student = Student(database)
    discipline = Discipline(database)
    statement_exam = StatementExam(database)
    statement_test = StatementTest(database)
    employee = Employee(database)
    generator()
    return True


palette_dark = QtGui.QPalette()
palette_dark.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
palette_dark.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
palette_dark.setColor(QtGui.QPalette.Base, QtGui.QColor(15, 15, 15))
palette_dark.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
palette_dark.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
palette_dark.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
palette_dark.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
palette_dark.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
palette_dark.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
palette_dark.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
palette_dark.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.Text, QtCore.Qt.darkGray)
palette_dark.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.Light, QtCore.Qt.black)
palette_dark.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, QtCore.Qt.darkGray)
palette_dark.setColor(QtGui.QPalette.Highlight, QtCore.Qt.darkGray)
palette_dark.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)

palette_white = QtGui.QPalette()
palette_white.setColor(QtGui.QPalette.Window, QtCore.Qt.white)
palette_white.setColor(QtGui.QPalette.WindowText, QtCore.Qt.black)
palette_white.setColor(QtGui.QPalette.Base, QtCore.Qt.white)
palette_white.setColor(QtGui.QPalette.AlternateBase, QtCore.Qt.white)
palette_white.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.black)
palette_white.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.black)
palette_white.setColor(QtGui.QPalette.Text, QtCore.Qt.black)
palette_white.setColor(QtGui.QPalette.Button, QtCore.Qt.white)
palette_white.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.black)
palette_white.setColor(QtGui.QPalette.BrightText, QtCore.Qt.green)
palette_white.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.Text, QtCore.Qt.darkGray)
palette_white.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.Light, QtCore.Qt.white)
palette_white.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, QtCore.Qt.lightGray)
palette_white.setColor(QtGui.QPalette.Highlight, QtCore.Qt.lightGray)
palette_white.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)

app = QtWidgets.QApplication(sys.argv)
dir_ = QtCore.QDir('Google Sans')
_id = QtGui.QFontDatabase.addApplicationFont('GUI/Fonts/GoogleSans-Regular.ttf')
_id = QtGui.QFontDatabase.addApplicationFont('GUI/Fonts/GoogleSans-Medium.ttf')
_id = QtGui.QFontDatabase.addApplicationFont('GUI/Fonts/GoogleSans-Bold.ttf')
app.setStyle('Fusion')
app.setFont(QtGui.QFont('Google Sans', 10))
app.setAttribute(QtCore.Qt.AA_DisableWindowContextHelpButton)
app.setWindowIcon(QtGui.QIcon('GUI/icon.ico'))

current_theme = 0


def set_white_theme():
    global current_theme
    current_theme = 0
    app.setPalette(palette_white)


def set_dark_theme():
    global current_theme
    current_theme = 1
    app.setPalette(palette_dark)


set_white_theme()
