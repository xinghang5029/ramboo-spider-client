# -*- coding: utf-8 -*-
from util.js import MyJs
from util.channel import QChannel

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView,QWebEnginePage
from PyQt5.QtWebChannel import QWebChannel
from util.pageToQt1 import PageToQt
from PyQt5.QtCore import QUrl
import sys,traceback,time

class MyWebView(QWebEngineView):

    def __init__(self,prev,parent=None):
        super(QWebEngineView,self).__init__(parent)
        self.loadFinished.connect(self.__loadFinished)
        self.prev = prev





    def __loadFinished(self,result):
        # self.page().runJavaScript(QChannel.CONTENT)
        self.page().runJavaScript(MyJs.INIT_EVENT)



    def createWindow(self, QWebEnginePage_WebWindowType):
        try:
            new_webview = MyWebView(self.prev)
            self.prev.create_tab(new_webview)
            return new_webview
        except Exception as a:
            print(traceback.format_exc())





















if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = MyWebView()
    login.load(QUrl("http://www.bidcenter.com.cn/newssearchyz-19852799.html"))
    channel = QWebChannel()
    myObj = PageToQt()
    channel.registerObject('bridge', myObj)
    login.page().setWebChannel(channel)
    login.show()


    sys.exit(app.exec_())

