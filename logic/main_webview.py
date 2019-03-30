# -*- coding: utf-8 -*-
from PyQt5.QtCore import QUrl
from PyQt5.QtWebChannel import QWebChannel
from util.pageToQt import PageToQt
class MainWebView(object):

    def __init__(self,ui):
        self.ui = ui

    def refresh(self,url):
        currentView = self.ui.tabWidget.currentWidget().centralWidget()
        currentView.load(QUrl(url))
