# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtProperty
from PyQt5.QtWidgets import QWidget

class PageToQt(QWidget):

    def __init__(self,strval = '100'):
        super(PageToQt,self).__init__()
        self.strval = strval

    def _getStrValue(self):
        return self.strval

    def _setStrValue(self,str):
        self.strval = str
        print(str)

    #需要定义的对外发布的方法
    strValue= pyqtProperty(str,_getStrValue,_setStrValue)