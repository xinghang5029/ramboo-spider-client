# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication,QMainWindow,QSplitter,QWidget,\
    QHBoxLayout,QLineEdit,QAction,QTabWidget
from PyQt5.Qt import Qt
from PyQt5.Qt import QCursor,QIcon
from PyQt5.QtCore import QUrl
from PyQt5.QtWebChannel import QWebChannel

from ui.ui_webview import MyWebView
from util.pageToQt import PageToQt
from ui.left.main import MainMenu
from ui.right.main import MainContent

from logic.main_webview import MainWebView
import sys

class Ui_Main_WebView(QMainWindow):

    def __init__(self, prev, parent = None):
        QMainWindow.__init__(self, parent)
        self.setWindowTitle("自定义浏览器")
        self.isResize = False
        self.prev = prev


        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.widget = QWidget(self)
        self.widget.setMinimumSize(self.size().width(),self.size().height())


        self.webview = MyWebView(self,parent=self.widget)
        self.webview.setMinimumHeight(self.widget.size().height())
        self.layout.addWidget(self.widget)
        self.setCentralWidget(self.widget)






        self.toolbar=self.addToolBar("search")
        self.site = QLineEdit()
        self.site.setStyleSheet("height:30px")
        self.toolbar.addWidget(self.site)
        self.refresh  = QAction(QIcon("../images/refresh.png"), "刷新", self)
        self.toolbar.addAction(self.refresh)
        self.toolbar.actionTriggered[QAction].connect(lambda :MainWebView(self).refresh(self.site.text()))
        self.toolbar.addSeparator()





    def resizeEvent(self,event):
        if self.isResize:
            height = self.size().height()
            width = self.size().width()
            self.webview.setMinimumSize(width,height)
            self.webview.setMaximumSize(width,height)
        else:
            self.isResize = True







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