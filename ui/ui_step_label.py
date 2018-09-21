# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication,QMainWindow,QSplitter,QWidget, \
    QHBoxLayout,QLabel,QComboBox,QSpinBox,QLineEdit,QAction,QTableWidget,QTableWidgetItem
from PyQt5.Qt import Qt
from PyQt5.Qt import QCursor,QIcon
from PyQt5.QtCore import QUrl
from PyQt5.QtWebChannel import QWebChannel

from PyQt5.QtGui import QPixmap,QMovie

from ui.ui_webview import MyWebView
from util.pageToQt import PageToQt
from ui.left.main import MainMenu
from ui.right.main import MainContent

from logic.main_webview import MainWebView
from util.table_util import Table_Util
from ui.ui_label import My_Label_TWO
import sys

class Ui_Setp_Label(QMainWindow):
    '''
    步骤标签说明
    '''

    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        # 采集类型  0：未选择类型  1：列表或表格  2：列表详情  3：单页采集
        self.acq_type = 0

        self.split = QSplitter(self)
        self.split.setOrientation(Qt.Horizontal)
        self.setCentralWidget(self.split)

        self.step_widget = QWidget(self.split)
        self.step_widget_layout = QHBoxLayout()
        self.step_widget_layout.setAlignment(Qt.AlignRight)
        self.step_widget.setLayout(self.step_widget_layout)

        self.basic_info = My_Label_TWO(1,self)
        self.basic_info.setText("设置基本信息")
        # self.basic_info.setPixmap(QPixmap('../images/step-1.png'))
        m = QMovie('../images/s-step-1.gif')
        self.basic_info.setMovie(m)
        m.start()
        self.site_type = My_Label_TWO(2,self)
        self.site_type.setText("设置网页类型")
        self.site_type.setMovie(m)
        self.site_type.setPixmap(QPixmap('../images/step-2.png'))

        self.no_singel_widget = QWidget(self.step_widget)
        self.no_singel_widget.setFixedHeight(40)
        self.no_singel_widget_layout = QHBoxLayout()
        self.no_singel_widget.setLayout(self.no_singel_widget_layout)

        self.singel_widget = QWidget(self.step_widget)
        self.singel_widget_layout = QHBoxLayout(self.step_widget)
        self.singel_widget.setFixedHeight(40)
        # self.singel_widget_layout.setSpacing(0)
        self.singel_widget_layout.addSpacing(0)
        self.singel_widget.setContentsMargins(0,0,0,0)
        self.singel_widget_layout.setAlignment(Qt.AlignLeft)
        self.singel_widget.setLayout(self.singel_widget_layout)

        self.navi = My_Label_TWO(3,self)
        self.navi.setText("设置列表")
        self.navi.setPixmap(QPixmap('../images/step-3.png'))
        self.flip = My_Label_TWO(4,self)
        self.flip.setText("翻页")
        self.flip.setPixmap(QPixmap('../images/step-4.png'))
        self.field = My_Label_TWO(5,self)
        self.field.setText("设置字段")
        self.field.setPixmap(QPixmap('../images/step-5.png'))
        self.finish = My_Label_TWO(6,self)
        self.finish.setText("完成")
        self.finish.setPixmap(QPixmap('../images/step-7.png'))


        self.single_field = My_Label_TWO(3,self.singel_widget)
        self.single_field.setText("设置字段")
        self.single_field.setPixmap(QPixmap('../images/step-5.png'))
        self.single_filp = My_Label_TWO(4,self.singel_widget)
        self.single_filp.setText("翻页")
        self.single_filp.setPixmap(QPixmap('../images/step-4.png'))
        self.single_finish = My_Label_TWO(5,self.singel_widget)
        self.single_finish.setText("完成")
        self.single_finish.setPixmap(QPixmap('../images/step-7.png'))



        self.no_singel_widget_layout.addWidget(self.navi)
        self.no_singel_widget_layout.addWidget(self.flip)
        self.no_singel_widget_layout.addWidget(self.field)
        self.no_singel_widget_layout.addWidget(self.finish)
        self.no_singel_widget.hide()

        self.singel_widget_layout.addWidget(self.single_field)
        self.singel_widget_layout.addWidget(self.single_filp)
        self.singel_widget_layout.addWidget(self.single_finish)
        self.singel_widget.hide()

        self.step_widget_layout.addWidget(self.basic_info)
        self.step_widget_layout.addWidget(self.site_type)
        self.step_widget_layout.addWidget(self.no_singel_widget)
        self.step_widget_layout.addWidget(self.singel_widget)



        self.split.addWidget(self.step_widget)










if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Ui_Setp_Label()
    main.show()


    sys.exit(app.exec_())