# -*- coding: utf-8 -*
from PyQt5.QtWidgets import QTreeWidgetItem,QAction,QMessageBox,QTreeWidgetItemIterator,QPushButton
from PyQt5.Qt import QCursor,QIcon,Qt
from PyQt5.QtCore import QSize
from dao.basic_dao import BasicDao
from functools import partial
from spider_process.download import DownLoad
from spider_process.spider import Spider
from util.rbQueue import RbQueue
import time,threading

class TaskList(object):

    check_node = []

    def __init__(self,widget):
        self.widget = widget


    def load_data(self,):
        """
        根据站点id加载采集的录制规则
        :param task_id:
        :return:
        """
        self.widget.tree.clear()
        TaskList.check_node = []
        theme_list = BasicDao.get_all_theme()
        for theme in theme_list:
            themeitem = QTreeWidgetItem(self.widget.tree)
            themeitem.setSizeHint(0,QSize(50,40))
            themeitem.setIcon(0,QIcon("../images/theme.png"))
            themeitem.setText(0,theme['name'])
            themeitem.setText(5,theme['code'])
            themeitem.setText(7,'theme')
            category_list = BasicDao.get_category_by_theme(theme['code'],False)
            for category in category_list:
                categoryitem = QTreeWidgetItem(themeitem)
                categoryitem.setIcon(0,QIcon("../images/category.png"))
                categoryitem.setText(0,category['name'])
                categoryitem.setText(5,category['code'])
                categoryitem.setText(7,'category')
                task_list = BasicDao.task_info_by_category(category['code'])
                for task in task_list:
                    taskitem = QTreeWidgetItem(categoryitem)
                    taskitem.setText(0,task['name'])
                    taskitem.setText(1,task['url'])
                    taskitem.setText(2,str(task['acqType']))
                    taskitem.setText(3,task['user'])
                    taskitem.setText(6,str(task['id']))
                    taskitem.setText(7,'task')
                    taskitem.setCheckState(0,Qt.Unchecked)
                    button = QPushButton()
                    button.setText("采集")
                    button.clicked.connect(partial(self.acq,task['id']))
                    self.widget.tree.setItemWidget(taskitem,4,button)
                self.circle_load(category['id'],categoryitem)
        self.widget.tree.expandAll()






    def circle_load(self,parent,item):
        category_list = BasicDao.get_category_by_parent(parent)
        for category in category_list:
            categoryitem = QTreeWidgetItem(item)
            categoryitem.setIcon(0,QIcon("../images/category.png"))
            categoryitem.setText(0,category['name'])
            categoryitem.setText(5,category['code'])
            categoryitem.setText(7,'category')
            self.circle_load(category['id'],categoryitem)
            task_list = BasicDao.task_info_by_category(category['code'])
            for task in task_list:
                taskitem = QTreeWidgetItem(categoryitem)
                taskitem.setText(0,task['name'])
                taskitem.setText(1,task['url'])
                taskitem.setText(2,str(task['acqType']))
                taskitem.setText(3,task['user'])
                taskitem.setText(6,str(task['id']))
                taskitem.setText(7,'task')
                taskitem.setCheckState(0,Qt.Unchecked)
                taskitem.setHidden(True)
                button = QPushButton()
                button.setText("采集")
                button.clicked.connect(partial(self.acq,task['id']))
                self.widget.tree.setItemWidget(taskitem,4,button)

    def click_process(self,item,index):
        if item.checkState(index) == Qt.Checked:
            if item not in TaskList.check_node:
                TaskList.check_node.append(item)
        else:
            if item in TaskList.check_node:
                TaskList.check_node.remove(item)


    def search_node(self):
        """
        根据任务名称，查找节点
        :return:
        """
        try:
            # 先加载所有的，在filter
            self.widget.task.load_data()
            text = self.widget.search_text.text().strip()
            # 遍历树
            item = QTreeWidgetItemIterator(self.widget.tree)
            #该类的value()即为QTreeWidgetItem
            while item.value():
                if item.value().text(7) == 'task':
                    name = item.value().text(0)
                    if name.count(text) > 0:
                        item.value().setHidden(False)
                    else:
                        item.value().setHidden(True)

                item = item.__iadd__(1) #游标加1，继续迭代

        except Exception as a:
            print(a)


    def delete_task(self):
        """
        删除任务
        :return:
        """
        try:
            # 获取选中节点的id
            id_arr = [item.text(6) for item in TaskList.check_node]
        except Exception as a:
            print(a)
        result = BasicDao.delete_task_by_ids(id_arr)
        if result:
            self.load_data()
            QMessageBox.information(self.widget,"温馨提示","删除成功")
        else:
            QMessageBox.information(self.widget,"温馨提示","删除失败")


    def acq(self,task_id):
        """
        数据采集
        :param task_id: 站点任务id
        :return:
        """
        try:
            navi_thread = threading.Thread(target=self.acq_navi, args=(task_id,))
            navi_thread.start()



        except Exception as a:
            print(a)


    def acq_navi(self,task_id):
        info = BasicDao.task_info_by_id(task_id)
        settings = {}
        settings["url"] = info['url']
        settings["timeout"] = 10
        settings["headers"] = None
        settings["cookies"] = None
        settings["proxy"] = None
        # download = DownLoad(settings)
        download = DownLoad(settings,type="dfa")
        spider = Spider(download,info)
        spider.start()

        file_thread = threading.Thread(target=self.acq_field, args=())
        file_thread.start()


    def acq_field(self):
        settings = {}
        settings["timeout"] = 10
        settings["headers"] = None
        settings["cookies"] = None
        settings["proxy"] = None

        while True:
            if not RbQueue.rb_queue.empty():
                task = RbQueue.rb_queue.get()
                settings["url"] = task['url']
                # download = DownLoad(settings)
                download = DownLoad(settings,type="fdsf")
                spider = Spider(download,task['rule'])
                spider.detail_start()

            else:
                time.sleep(1)
                break
        print("=========================本次采集完成===============================")