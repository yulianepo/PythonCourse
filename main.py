from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import sys

class Mainwindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.name = "BOT"
        self.setCentralWidget(QWidget())
        self.layout = QVBoxLayout(self.centralWidget())

        self.label = QLabel(self.text())
        self.name_box = QLineEdit("Please enter your name and Press Enter")

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.name_box)
        self.name_box.returnPressed.connect(self.update_label)

    def update_label(self):
        self.label.setText(self.text_name())

    def text_name(self):
        self.name = self.name_box.text()
        return f"Hello {self.name}"

    def text(self):
        return f"Hello {self.name}"


app = QApplication(sys.argv)
w = Mainwindow()
w.show()
app.exec_()

