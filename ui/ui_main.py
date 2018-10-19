# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication,QMainWindow,QSplitter,QWidget,QTabWidget,QLabel
from PyQt5.Qt import Qt
from PyQt5.QtCore import QUrl
from PyQt5.QtWebChannel import QWebChannel

from ui.ui_webview import MyWebView
from util.pageToQt1 import PageToQt
from ui.ui_rule import Ui_Rule
from ui.ui_login import Ui_login
from ui.ui_process import Ui_Process
from ui.ui_task_list import Ui_Task
from util.rest_service import RestService
from util.style import WidgetStyle


import sys,traceback

class Ui_Main(QMainWindow):

    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        splitter =  QSplitter(self)
        splitter.setOrientation(Qt.Horizontal)
        self.setCentralWidget(splitter)
        self.setMinimumSize(1200,800)
        self.setWindowTitle('采集器')
        # self.showMaximized()




        left_widget = QWidget(self)
        left_widget.setMinimumWidth(200)
        left_widget.setStyleSheet("background:white")

        self.right_widget = QTabWidget()
        self.right_widget.currentChanged.connect(self.deal)
        self.right_widget.setObjectName("right")
        self.right_widget.setTabShape(QTabWidget.Triangular)
        self.right_widget.setDocumentMode(True)
        self.right_widget.setMovable(True)
        self.right_widget.setTabsClosable(True)
        self.right_widget.addTab(Ui_Task(self), "任务列表")
        self.right_widget.setStyleSheet(WidgetStyle.QTabWidget)
        self.right_widget.tabCloseRequested.connect(self.close_Tab)


        splitter.addWidget(left_widget)
        splitter.addWidget(self.right_widget)
        splitter.setStretchFactor(0,1);
        splitter.setStretchFactor(1,6);


    def deal(self,index):
        """
        切换标签时，要重设RestService中的widget变量，目的是为了录制规则时，填充到对应的table上
        :param index:
        :return:
        """
        widget = self.right_widget.widget(index)
        if isinstance(widget,Ui_Process):
            RestService.widget = widget.transcribe

    def create_tab(self,type,id,name):
        """
        创建标签页
        :param type: 0：新建任务 1：加载任务
        :param id: 任务id
        :param name: 任务名称
        :return:
        """
        if type == 0:
            self.right_widget.addTab(Ui_Process(0,self), "新建任务")
        elif type == 1:
            self.right_widget.addTab(Ui_Process(id,self), name)
        self.right_widget.setCurrentIndex(self.right_widget.count()-1)


    def close_Tab(self,index):
        """
        关闭tab
        :param index:
        :return:
        """
        try:
            self.right_widget.removeTab(index)
        except Exception as a:
            print(traceback.format_exc())







    # def resizeEvent(self,event):
    #     if self.isResize:
    #         height = self.right_widget.size().height()
    #         width = self.right_widget.size().width()
    #         self.webview.setMinimumSize(width,height)
    #         self.webview.setMaximumSize(width,height)
    #     else:
    #         self.isResize = True







if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        main = Ui_Main()
        rest_server = RestService()
        rest_server.start()
        rest_server.trigger.connect(rest_server.deal_data)
        main.show()
    except Exception as a:
        print(traceback.format_exc())
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
