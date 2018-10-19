# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication,QMainWindow,QSplitter,\
    QHBoxLayout,QLineEdit,QAction,QPushButton
from PyQt5.Qt import Qt
from PyQt5.Qt import QCursor,QIcon
from PyQt5.QtCore import QUrl
from PyQt5.QtWebChannel import QWebChannel

from ui.ui_step import Ui_Setp
from ui.ui_main_webview11 import Ui_Main_WebView
from util.pageToQt1 import PageToQt
from ui.ui_rule import Ui_Rule
from ui.ui_basic import Ui_Basic
from ui.ui_mode import Ui_Mode
from logic.rule_process import RuleProcess
from ui.ui_step_label import Ui_Setp_Label
import sys

class Ui_Process(QMainWindow):
    """
    规则录制界面
    """

    def __init__(self, task_id,parent = None):
        QMainWindow.__init__(self, parent)
        self.setWindowTitle("规则录制界面")
        self.task_id = task_id

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.toolbar=self.addToolBar("step")
        self.prev_step  = QAction(QIcon("../images/prev-step.png"), "上一步", self)
        self.next_step  = QAction(QIcon("../images/next-step.png"), "下一步", self)
        self.save_step  = QAction(QIcon("../images/save-step.png"), "保存", self)
        self.setting_step  = QAction(QIcon("../images/setting.png"), "采集设置", self)
        self.toolbar.addAction(self.prev_step)
        self.toolbar.addAction(self.next_step)
        self.toolbar.addAction(self.save_step)
        self.toolbar.addAction(self.setting_step)
        self.toolbar.addSeparator()
        self.step_label = Ui_Setp_Label()
        self.toolbar.addWidget(self.step_label)
        self.toolbar.addSeparator()
        self.split = QSplitter(self)
        self.split.setOrientation(Qt.Vertical)
        self.mode = Ui_Mode(self)
        self.transcribe = Ui_Rule(self)
        self.basic = Ui_Basic(self,parent=self)
        self.split.addWidget(self.basic)
        self.split.addWidget(self.mode)
        self.split.addWidget(self.transcribe)
        self.split.widget(0).show()
        self.split.widget(1).hide()
        self.split.widget(2).hide()
        self.setCentralWidget(self.split)

        self.rule_process = RuleProcess(self)
        self.rule_process.task_id = self.task_id
        self.prev_step.triggered.connect(lambda :self.rule_process.process(0))
        self.next_step.triggered.connect(lambda :self.rule_process.process(1))
        self.save_step.triggered.connect(lambda :self.rule_process.save(self.task_id))
        self.setting_step.triggered.connect(lambda :self.rule_process.process(2))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Ui_Process(1)
    main.show()

    main.transcribe.browse.webview.load(QUrl("http://www.bidcenter.com.cn/newssearchyz-19852799.html"))
    channel = QWebChannel()
    myObj = PageToQt(main.transcribe)
    channel.registerObject('bridge', myObj)
    main.transcribe.browse.webview.page().setWebChannel(channel)


    sys.exit(app.exec_())