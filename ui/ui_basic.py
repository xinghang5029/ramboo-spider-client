# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication,QMainWindow,QSplitter,QWidget,\
    QLabel,QComboBox,QLineEdit,QGridLayout
from PyQt5.Qt import Qt
from logic.basic_process import BasicProcess
from dao.basic_dao import BasicDao

import sys

class Ui_Basic(QMainWindow):
    """
    基本信息界面
    """

    def __init__(self,prev,parent = None):
        QMainWindow.__init__(self, parent)
        self.setWindowTitle("规则录制界面")
        self.prev = prev


        self.split = QSplitter(self)
        self.split.setOrientation(Qt.Vertical)
        self.split.setContentsMargins(0,10,10,0)

        self.label = QLabel(self.split)
        self.label.setText("请填写任务基本信息")
        self.label.setStyleSheet("font:bold;color:#8A2BE2")
        self.label.setContentsMargins(10,10,10,10)

        self.basic_widget = QWidget(self.split)
        self.basic_widget_layout = QGridLayout()
        self.basic_widget.setLayout(self.basic_widget_layout)
        self.basic_widget_layout.setAlignment(Qt.AlignTop)
        self.basic_widget.setStyleSheet("background:white")

        label_style = r'QLabel{font:bold}'
        edit_style = r'QLineEdit{border: 1px solid #D1D1D1;font-size: 20px;} ' \
                     r'QLineEdit:focus{border: 1px solid #87CEEB;color: #87CEEB;}'
        box_style = r'QComboBox{border: 1px solid #D1D1D1;font-size: 20px;}' \
                    r'QComboBox QAbstractItemView{ border: 1px solid #87CEEB;selection-background-color: #87CEEB;}'
        site_name_label = QLabel(self.basic_widget)
        site_name_label.setText("任务名称     ")
        site_name_label.setStyleSheet(label_style)
        self.site_name_edit = QLineEdit(self.basic_widget)
        self.site_name_edit.setFixedSize(700,40)
        self.site_name_edit.setStyleSheet(edit_style)
        self.site_name_edit.setFocus(True)
        self.site_name_edit.setText("百度")
        site_url_label = QLabel(self.basic_widget)
        site_url_label.setText("采集网址      ")
        site_url_label.setStyleSheet(label_style)
        self.site_url_edit = QLineEdit(self.basic_widget)
        self.site_url_edit.setFixedSize(700,40)
        self.site_url_edit.setStyleSheet(edit_style)
        self.site_url_edit.setText("http://www.ccgp-neimenggu.gov.cn/category/cggg?type_name=1")
        task_theme_label = QLabel(self.basic_widget)
        task_theme_label.setText("所属主题      ")
        task_theme_label.setStyleSheet(label_style)
        self.task_theme_box = QComboBox(self.basic_widget)
        self.task_theme_box.setFixedSize(700,40)
        self.task_theme_box.setStyleSheet(box_style)
        self.task_theme_box.currentIndexChanged.connect(self.category_by_theme)
        task_category_label = QLabel(self.basic_widget)
        task_category_label.setText("所属类别      ")
        task_category_label.setStyleSheet(label_style)
        self.task_category_box = QComboBox(self.basic_widget)
        self.task_category_box.setFixedSize(700,40)
        self.task_category_box.setStyleSheet(box_style)



        self.basic_widget_layout.addWidget(site_name_label,0,0,1,1,Qt.AlignLeft)
        self.basic_widget_layout.addWidget(self.site_name_edit,0,1,1,1,Qt.AlignLeft)
        self.basic_widget_layout.addWidget(site_url_label,1,0,1,1,Qt.AlignLeft)
        self.basic_widget_layout.addWidget(self.site_url_edit,1,1,1,1,Qt.AlignLeft)
        self.basic_widget_layout.addWidget(task_theme_label,2,0,1,1,Qt.AlignLeft)
        self.basic_widget_layout.addWidget(self.task_theme_box,2,1,1,1,Qt.AlignLeft)
        self.basic_widget_layout.addWidget(task_category_label,3,0,1,1,Qt.AlignLeft)
        self.basic_widget_layout.addWidget(self.task_category_box,3,1,1,1,Qt.AlignLeft)
        self.basic_widget_layout.setColumnStretch(0,1)
        self.basic_widget_layout.setColumnStretch(1,100)


        self.split.addWidget(self.label)
        self.split.addWidget(self.basic_widget)
        self.split.setStretchFactor(0,1)
        self.split.setStretchFactor(1,30)
        self.setCentralWidget(self.split)

        BasicProcess(self).load_data(self.prev.task_id)


    def category_by_theme(self,index):
        self.category_code_list = ['0']
        try:
            current_theme_code = self.task_theme_box.itemData(index)
            if not current_theme_code == "0":
                self.task_category_box.clear()
                # self.task_category_box.addItem("请选择","0")
                category_list = BasicDao.get_category_by_theme(current_theme_code,True)
                for category in category_list:
                    self.task_category_box.addItem(category['name'],category['code'])
                    self.category_code_list.append(category['code'])

            else:
                self.task_category_box.clear()
                self.task_category_box.addItem("请选择","0")
        except Exception as a:
            pass






if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Ui_Basic()
    main.show()


    sys.exit(app.exec_())