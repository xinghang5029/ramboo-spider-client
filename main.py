# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication
from ui.ui_main import Ui_Main
from util.rest_service import RestService
from ui.ui_login import Ui_login
from scrapy_spider.spider_process import SpiderProcess
import sys
if __name__ == '__main__':
    app = QApplication(sys.argv)

    # main = Ui_Main()

    # rest_server = RestService()
    # rest_server.start()

    # rest_server.trigger.connect(rest_server.deal_data)
    # file_thread = threading.Thread(target=DetailThread().acq_field, args=())
    # file_thread.start()

    # main.show()

    login = Ui_login()
    login.show()
    sys.exit(app.exec_())

    # spider = SpiderProcess()
    # spider.start()