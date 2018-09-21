# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow,QSplitter,QHBoxLayout
from PyQt5.Qt import Qt

from ui.ui_step import Ui_Setp
from ui.ui_main_webview11 import Ui_Main_WebView

class Ui_Rule(QMainWindow):
    """
    规则录制界面
    """

    def __init__(self, prev,parent = None):
        QMainWindow.__init__(self, parent)
        self.setWindowTitle("规则录制界面")
        self.prev = prev


        self.layout = QHBoxLayout()
        self.setLayout(self.layout)



        self.split = QSplitter(self)
        self.split.setOrientation(Qt.Vertical)

        self.step = Ui_Setp(self)
        self.browse = Ui_Main_WebView(self)


        self.split.addWidget(self.step)
        self.split.addWidget(self.browse)
        self.split.setStretchFactor(0,2)
        self.split.setStretchFactor(1,2)
        self.setCentralWidget(self.split)


