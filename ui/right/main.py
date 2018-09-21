# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication,QMainWindow,QSplitter,QWidget,QHBoxLayout,QLabel,QTextEdit
import sys
class MainContent(QWidget):

    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.setStyleSheet("background:blue")
        self.layout = QHBoxLayout(self)
        self.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout)
        self.layout.setSpacing(0)
        self.textedit = QLabel(self)
        self.textedit.setText("dfas")
        self.layout.addWidget(self.textedit)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainContent()
    main.show()
    sys.exit(app.exec_())