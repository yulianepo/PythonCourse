from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import sys

class Mainwindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.result = 0
        self.n1 = 0
        self.n2 = 0
        self.op = None
        self.i = 1
        self.setCentralWidget(QWidget())
        self.layout = QVBoxLayout(self.centralWidget())

        self.text = QPlainTextEdit(str(self.result))
        self.btn_plus = QPushButton("+")
        self.btn_minus = QPushButton("-")
        self.btn_mult = QPushButton("*")
        self.btn_equal = QPushButton("=")

        self.layout.addWidget(self.text)
        self.layout.addWidget(self.btn_plus)
        self.layout.addWidget(self.btn_minus)
        self.layout.addWidget(self.btn_mult)
        self.layout.addWidget(self.btn_equal)

        self.text.textChanged.connect(self.update_num)
        self.btn_plus.clicked.connect(self.update_plus)
        self.btn_minus.clicked.connect(self.update_minus)
        self.btn_mult.clicked.connect(self.update_mult)

        self.btn_equal.clicked.connect(self.print_result)


    def update_num(self):
        self.i = (self.i+1) % 2
        if self.i == 0:
            self.n1 = int(self.text.toPlainText())
        else:
            self.n2 = int(self.text.toPlainText())

    def update_plus(self):
        self.op = '+'

    def update_minus(self):
        self.op = '-'

    def update_mult(self):
        self.op = '*'

    def print_result(self):
        self.text.setPlainText(str(self.calc()))

    def calc(self):
        if self.op == '+':
            return self.n1 + self.n2
        elif self.op == '-':
            return self.n1 - self.n2
        else:
            return self.n1 * self.n2



app = QApplication(sys.argv)
w = Mainwindow()
w.show()
app.exec_()

