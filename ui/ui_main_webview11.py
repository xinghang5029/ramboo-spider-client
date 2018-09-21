# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,\
    QHBoxLayout,QLineEdit,QAction,QTabWidget
from PyQt5.Qt import QIcon
from PyQt5.QtCore import QUrl
from PyQt5.QtWebChannel import QWebChannel

from ui.ui_webview import MyWebView
from util.pageToQt1 import PageToQt
from util.style import WidgetStyle


from logic.main_webview import MainWebView
import sys,traceback

class Ui_Main_WebView(QMainWindow):


    def __init__(self,prev, parent = None):
        QMainWindow.__init__(self, parent)
        self.setWindowTitle("自定义浏览器")
        self.isResize = False
        self.prev = prev
        self.flag = False

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.widget = QWidget(self)
        self.widget.setMinimumSize(self.size().width(),self.size().height())

        self.tabWidget = QTabWidget()
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tabWidget.setObjectName("myself")
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setStyleSheet(WidgetStyle.My_QTabWidget)
        self.tabWidget.tabCloseRequested.connect(self.close_Tab)

        self.webview = MyWebView(self)
        self.webview.setMinimumHeight(self.widget.size().height())
        self.create_tab(self.webview)
        self.layout.addWidget(self.tabWidget)
        self.setCentralWidget(self.tabWidget)



        self.toolbar=self.addToolBar("search")
        self.site = QLineEdit()
        self.site.setStyleSheet("height:30px")
        self.toolbar.addWidget(self.site)
        self.refresh  = QAction(QIcon("../images/refresh.png"), "刷新", self)
        self.toolbar.addAction(self.refresh)
        self.toolbar.actionTriggered[QAction].connect(lambda :MainWebView(self).refresh(self.site.text()))
        self.toolbar.addSeparator()





    # def resizeEvent(self,event):
    #     if self.isResize:
    #         height = self.size().height()
    #         width = self.size().width()
    #         self.webview.setMinimumSize(width,height)
    #         self.webview.setMaximumSize(width,height)
    #     else:
    #         self.isResize = True



    #创建tab
    def create_tab(self,webview):
        tab = QMainWindow()
        title = webview.url()
        self.tabWidget.addTab(tab, "链接")
        self.tabWidget.setCurrentWidget(tab)
        tab.setCentralWidget(webview)
        if not self.prev.step.navi_table.isHidden() or not self.prev.step.flip_table.isHidden():
            self.tabWidget.setCurrentIndex(0)


    #关闭tab
    def close_Tab(self,index):
        try:
            if self.tabWidget.count()>1 and index !=0:
                self.tabWidget.removeTab(index)
        except Exception as a:
            print(traceback.format_exc())







if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Ui_Main_WebView()
    main.show()


    main.webview.load(QUrl("http://www.bidcenter.com.cn/newssearchyz-19852799.html"))
    channel = QWebChannel()
    myObj = PageToQt()
    channel.registerObject('bridge', myObj)
    main.webview.page().setWebChannel(channel)

    sys.exit(app.exec_())