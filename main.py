# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication
from ui.ui_login import Ui_login
from scrapy_spider.spider_process import SpiderProcess
import sys
if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Ui_login()
    login.show()
    sys.exit(app.exec_())

    # spider = SpiderProcess()
    # spider.start()