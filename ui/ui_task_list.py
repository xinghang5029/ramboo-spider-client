# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication,QMainWindow,QSplitter,\
    QHBoxLayout,QTreeWidget,QTreeWidgetItem,QAction,QLineEdit
from PyQt5.Qt import Qt
from PyQt5.Qt import QCursor,QIcon
from logic.task_list import TaskList
from util.style import WidgetStyle
import sys

class Ui_Task(QMainWindow):
    """
    任务展示页面
    """

    def __init__(self, prev,parent = None):
        QMainWindow.__init__(self, parent)
        self.prev = prev
        self.setWindowTitle("任务展示界面")

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.toolbar=self.addToolBar("step")
        self.add  = QAction(QIcon("../images/add.png"), "新增", self)
        self.delete  = QAction(QIcon("../images/delete.png"), "删除", self)
        self.search_text = MyLineEdit(self)
        self.search_text.setPlaceholderText("请输入查询关键字");
        self.search_text.setContentsMargins(20,0,0,0)
        self.search_text.setMinimumHeight(40)
        self.refresh  = QAction(QIcon("../images/refresh.png"), "刷新", self)
        self.toolbar.addAction(self.add)
        self.add.triggered.connect(lambda :self.prev.create_tab(0,0,""))
        self.toolbar.addAction(self.delete)
        self.task = TaskList(self)
        self.delete.triggered.connect(lambda :self.task.delete_task())
        self.toolbar.addWidget(self.search_text)
        self.toolbar.addAction(self.refresh)
        self.refresh.triggered.connect(lambda :self.task.search_node())
        self.toolbar.addSeparator()
        self.split = QSplitter(self)
        self.split.setOrientation(Qt.Vertical)

        self.tree = QTreeWidget(self.split)
        self.tree.setColumnCount(8)
        # self.tree.setStyleSheet(r'QTreeView{font-size:20px}')
        self.tree.setStyleSheet(WidgetStyle.TREE_WIDGET)
        self.tree.itemDoubleClicked.connect(self.show_task)
        self.tree.itemChanged.connect(self.task.click_process)
        # self.tree.setColumnHidden(5,True)
        self.tree.setHeaderLabels(['名称','地址','采集类型','用户','操作'])
        self.tree.header().setDefaultAlignment (Qt.AlignHCenter| Qt.AlignVCenter)

        self.split.addWidget(self.tree)
        self.setCentralWidget(self.split)
        self.task.load_data()

    def show_task(self,item):
        try:
            type = item.text(7)
            if type == "task":
                id = int(item.text(6))
                name = item.text(0)
                self.prev.create_tab(1,id,name)
        except Exception as a:
            print(a)


class MyLineEdit(QLineEdit):

    def __init__(self, prev,parent = None):
        super(MyLineEdit, self).__init__()
        self.prev = prev


    def keyPressEvent(self, event):
        try:
            if str(event.key())=='16777220':  #回车
                self.prev.task.search_node()
            else:
                QLineEdit.keyPressEvent(self,event)
        except Exception as a:
            print(a)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Ui_Task()
    main.show()



    sys.exit(app.exec_())