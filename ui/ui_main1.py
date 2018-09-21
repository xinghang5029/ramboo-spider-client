# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication,QMainWindow,QSplitter,QWidget
from PyQt5.Qt import Qt
from PyQt5.QtCore import QUrl
from PyQt5.QtWebChannel import QWebChannel

from ui.ui_webview import MyWebView
from util.pageToQt1 import PageToQt
from ui.ui_rule import Ui_Rule
from ui.ui_process import Ui_Process
from ui.ui_task_list import Ui_Task
from util.rest_service import RestService


import sys,threading

class Ui_Main(QMainWindow):

    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        splitter =  QSplitter(self)
        splitter.setOrientation(Qt.Horizontal)
        self.setCentralWidget(splitter)
        self.setMinimumSize(1200,800)
        # self.showMaximized()




        left_widget = QWidget(self)
        left_widget.setMinimumWidth(200)
        left_widget.setStyleSheet("background:white")

        self.right_widget = Ui_Task()


        splitter.addWidget(left_widget)
        splitter.addWidget(self.right_widget)
        splitter.setStretchFactor(0,1);
        splitter.setStretchFactor(1,6);







    # def resizeEvent(self,event):
    #     if self.isResize:
    #         height = self.right_widget.size().height()
    #         width = self.right_widget.size().width()
    #         self.webview.setMinimumSize(width,height)
    #         self.webview.setMaximumSize(width,height)
    #     else:
    #         self.isResize = True







if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Ui_Main()

    main.show()
    # main.right_widget.transcribe.browse.webview.load(QUrl("http://www.ccgp-jilin.gov.cn/shopHome/morePolicyNews.action?categoryId=124&noticetypeId=2"))
    # channel = QWebChannel()
    # myObj = PageToQt(main.right_widget.transcribe)
    # channel.registerObject('bridge', myObj)
    # main.right_widget.transcribe.browse.webview.page().setWebChannel(channel)
    # print(main.right_widget.transcribe)
    # rest_server = RestService(main.right_widget.transcribe)
    # rest_server.start()
    # rest_server.trigger.connect(rest_server.deal_data)

    sys.exit(app.exec_())
