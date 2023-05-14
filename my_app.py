#  Импорт модулей и файла с переменными и тестами
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit
from instr import *

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('#!/bin/bash')
main_win.move(win_x, win_y)
main_win.resize(win_width, win_height)
main_win.show()
main_win.show()
app.exec_()
# Создание вертикальной линии
v_line = QVBoxLayout()
# Создание 2 горизонтальных линий
g_line1 = QHBoxLayout()
g_line2 = QHBoxLayout()
# Надпись: ФИО и добавление его к горизонтальной линии
label1 = QLabel(txt_name)
label1.setText('34')
g_line1.addWidget(label1, alignment = Qt.AlignCenter)
main_win.setLayout(g_line1)