# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication,QMainWindow,QSplitter,QWidget,QHBoxLayout,QLabel,QTextEdit
from PyQt5.QtCore import Qt
import sys
class MainMenu(QWidget):

    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet("background:grey")
        self.setContentsMargins(0,0,0,0)
        self.layout = QHBoxLayout(self)
        self.setLayout(self.layout)
        self.layout.setSpacing(0)
        self.textedit = QLabel(self)
        self.textedit.setText("dfas")
        self.layout.addWidget(self.textedit)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainMenu()
    main.show()
    sys.exit(app.exec_())