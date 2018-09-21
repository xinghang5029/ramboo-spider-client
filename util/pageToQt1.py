# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtProperty
from PyQt5.QtWidgets import QWidget,QMessageBox

from util.table_util import Table_Util
from lxml import etree

import json,traceback,re

class PageToQt(QWidget):

    def __init__(self,prev,strval = '100'):
        super(PageToQt,self).__init__()
        self.strval = strval
        self.prev = prev

    def _getStrValue(self):
        return self.strval

    def _setStrValue(self,str):
        try:
            self.strval = str
            info = json.loads(str)
            acq_type = self.prev.prev.step_label.acq_type
            table_list = [self.prev.step.navi_table,self.prev.step.flip_table,self.prev.step.field_table]
            self.target_table = list(filter(lambda x: not x.isHidden(), table_list))[0]
            Table_Util.insert_single_data(self.target_table,info)
            self.add_more_data()

        except Exception as a:
            QMessageBox.warning(self.prev.step,"温馨提示","规则录制出现异常:{}".format(traceback.format_exc()))


    def add_more_data(self,):
        rows = self.target_table.rowCount()
        if rows >= 2:
            xpath_before = (self.target_table.item(rows-2,2).text())
            xpath_after = (self.target_table.item(rows-1,2).text())
            if len(xpath_before) == len(xpath_after):
                self.xpath_before_list = xpath_before.split("/")
                xpath_after_list = xpath_after.split("/")
                self.index = 0;
                self.diff_str = None
                for i,v in enumerate(xpath_after_list):
                    if v not in self.xpath_before_list:
                        self.diff_str = v
                        self.index = i
                        break
                if self.diff_str:
                    self.prev.browse.webview.page().toHtml(self.getHtml)

    def getHtml(self,*k,**v):
        try:
            html = k[0]
            start = int(re.findall(r'\d+',self.diff_str)[0])
            selectors = etree.HTML(html)
            while start <= 100:
                self.diff_str = self.diff_str.replace(str(start),str(start+1))
                self.xpath_before_list[self.index] = self.diff_str
                xpath = "/".join(self.xpath_before_list)
                content = selectors.xpath(xpath)
                if len(content):
                    resultContent =  ''.join(content[0].xpath('string(.)').replace('\n','').split())
                    info = {}
                    info['xpath'] = xpath
                    info['text'] = resultContent
                    Table_Util.insert_single_data(self.target_table,info)
                start = start + 1
        except Exception as a:
            print(traceback.format_exc())


    #需要定义的对外发布的方法
    strValue= pyqtProperty(str,_getStrValue,_setStrValue)