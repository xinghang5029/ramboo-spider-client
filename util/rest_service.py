# coding=utf-8
from wsgiref.simple_server import make_server
from PyQt5.QtCore import QThread
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget,QMessageBox
from util.table_util import Table_Util
from lxml import etree
import urllib.parse
import json,traceback,re

class RestService(QThread):


    trigger = QtCore.pyqtSignal(str)
    widget = None

    def __init__(self,parent=None):
        QThread.__init__(self,parent)


    def application(self,environ, start_response):
        if environ.get('PATH_INFO', 'no')==r'/internet':
            try:
                request_body_size = int(environ.get('CONTENT_LENGTH', 0))
            except (ValueError):
                request_body_size = 0
            request_body = environ['wsgi.input'].read(request_body_size)
            content = request_body.decode("UTF-8")
            data = urllib.parse.unquote_to_bytes(content).decode('UTF-8')
            self.trigger.emit(data.replace("rule_info=",""))
        response_body = 'success'
        status = '200 OK'
        response_headers = [('Content-Type', 'text/plain;charset=gbk'),]
        start_response(status, response_headers)
        return [response_body.encode("UTF-8")]

    def deal_data(self,data):
        try:
            info = json.loads(data)
            acq_type = RestService.widget.prev.step_label.acq_type
            table_list = [RestService.widget.step.navi_table,RestService.widget.step.flip_table,RestService.widget.step.field_table]
            self.target_table = list(filter(lambda x: not x.isHidden(), table_list))[0]
            Table_Util.insert_single_data(self.target_table,info)
            self.add_more_data()
        except Exception as a:
            QMessageBox.warning(RestService.widget.step,"温馨提示","规则录制出现异常:{}".format(traceback.format_exc()))

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
                    RestService.widget.browse.webview.page().toHtml(self.getHtml)

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


    def run(self):
        httpd = make_server('0.0.0.0', 9997, self.application)
        httpd.serve_forever()






