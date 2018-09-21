# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication,QMainWindow,QSplitter,QWidget,\
    QHBoxLayout,QLabel,QTableWidget,QDockWidget,QPushButton,QVBoxLayout
from PyQt5.Qt import Qt
from util.table_util import Table_Util
import sys

class Ui_Setp(QMainWindow):

    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.setWindowTitle("规则内容展示")


        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.split = QSplitter(self)
        self.split.setOrientation(Qt.Vertical)

        self.illustrate = QLabel(self.split)
        self.illustrate.setContentsMargins(10,10,10,10)
        self.illustrate.setText("此处填写每一步的说明")
        self.illustrate.setStyleSheet("font:bold;color:#8A2BE2")

        self.navi_table = QTableWidget(self.split)
        self.navi_table.setObjectName("navi_table")
        self.navi_table.setColumnCount(4)
        self.navi_table.horizontalHeader().setStyleSheet("QHeaderView::section{padding:2px 4px;background-color: rgb(170, 170, 255)}");
        self.navi_table.horizontalHeader().setStretchLastSection(True)
        # self.navi_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents);
        # self.navi_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents);
        self.navi_table.setHorizontalHeaderLabels(["动作", "提取元素", "XPATH","URL处理"])


        self.flip_table = QTableWidget(self.split)
        self.flip_table.setObjectName("flip_table")
        self.flip_table.setColumnCount(5)
        self.flip_table.horizontalHeader().setStyleSheet("QHeaderView::section{padding:2px 4px;background-color: rgb(170, 170, 255)}");
        self.flip_table.horizontalHeader().setStretchLastSection(True)
        # self.flip_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents);
        # self.flip_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents);
        # self.flip_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents);
        # self.flip_table.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents);
        self.flip_table.setHorizontalHeaderLabels(["动作", "提取元素", "XPATH", "开始页码","终止页码"])
        self.flip_table.hide()


        self.field_table = QTableWidget(self.split)
        self.field_table.setObjectName("field_table")
        self.field_table.setColumnCount(6)
        self.field_table.horizontalHeader().setStyleSheet("QHeaderView::section{padding:2px 4px;background-color: rgb(170, 170, 255)}");
        self.field_table.horizontalHeader().setStretchLastSection(True)
        # self.field_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents);
        # self.field_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents);
        # self.field_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents);
        # self.field_table.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents);
        self.field_table.setHorizontalHeaderLabels(["动作", "提取元素", "XPATH", "字段名称","正则","函数"])
        self.field_table.hide()
        self.split.addWidget(self.illustrate)
        self.split.addWidget(self.navi_table)
        self.split.addWidget(self.flip_table)
        self.split.addWidget(self.field_table)
        self.setCentralWidget(self.split)

        table_tool=QDockWidget(self.tr("表格工具"),self)
        title_widget = QWidget(self)
        title_widget.setStyleSheet("background:#FFC125")
        title_widget_layout = QHBoxLayout()
        title_widget.setLayout(title_widget_layout)
        title_widget_layout.addWidget(QLabel("表格工具"))
        table_tool.setTitleBarWidget(title_widget);
        table_tool.setFeatures(QDockWidget.DockWidgetMovable|QDockWidget.DockWidgetFloatable)
        table_tool.setAllowedAreas(Qt.AllDockWidgetAreas)
        table_tool_widget = QWidget(table_tool)
        table_tool_widget.setStyleSheet("background:#FFFFFF")
        table_tool_widget_layout = QVBoxLayout()
        table_tool_widget.setLayout(table_tool_widget_layout)
        cleanDataBtn= QPushButton(table_tool_widget)
        cleanDataBtn.setText("清除表格")
        cleanDataBtn_1= QPushButton(table_tool_widget)
        cleanDataBtn_1.setText("功能一")
        cleanDataBtn.clicked.connect(lambda :Table_Util.clean_table(self))
        table_tool_widget_layout.addWidget(cleanDataBtn)
        table_tool_widget_layout.addWidget(cleanDataBtn_1)
        table_tool.setWidget(table_tool_widget)
        self.addDockWidget(Qt.RightDockWidgetArea,table_tool)









if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Ui_Setp()
    main.show()


    sys.exit(app.exec_())