# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPixmap,QMovie
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtCore import QUrl
from util.support import Support
from dao.basic_dao import BasicDao
from util.table_util import Table_Util
from util.rest_service import RestService
from ui.ui_acq_setting import Ui_Acq_Setting
from util.pageToQt import PageToQt
from ui.ui_thread import MyQthread
import traceback,time
class RuleProcess(object):

    """
    整个规则录制处理类
    """
    task_id = 0
    def __init__(self,prev):
        self.prev = prev
        self.no_single_step_obj = [self.prev.step_label.navi,self.prev.step_label.flip,self.prev.step_label.field,self.prev.step_label.finish]

        self.step = 0
        self.sub_step = 0

    def process(self,index):
        try:
            if index == 0:
                self.prev_step()
            elif index == 1:
                self.next_step()
            elif index == 2:
                self.show_setting()

        except Exception as a:
            print(a)

    def save(self,task_id):
        """
        保存录制的站点规则
        :param task_id: 任务id
        :return:
        """

        try:
            task_name = self.prev.basic.site_name_edit.text()
            task_url = self.prev.basic.site_url_edit.text()
            theme = self.prev.basic.task_theme_box.itemData(self.prev.basic.task_theme_box.currentIndex())
            category = self.prev.basic.task_category_box.itemData(self.prev.basic.task_category_box.currentIndex())
            rule_content = {}
            if self.basic_info_check(task_name,task_url,theme,category):
                # ==========================基本信息===================================
                basic = {}
                basic['id'] = self.task_id
                basic["name"] = task_name
                basic["url"] = task_url
                basic["theme"] = theme
                basic["category"] = category
                basic['state'] = 0
                basic['user'] = 'admin'
                basic['acqType'] = self.prev.step_label.acq_type
                rule_content["basic"] = basic

                # ==========================规则信息===================================
                navi_data = Table_Util.get_navi_table(self.prev.transcribe.step.navi_table)
                flip_data = Table_Util.get_flip_table(self.prev.transcribe.step.flip_table)
                field_data = Table_Util.get_field_table(self.prev.transcribe.step.field_table)


                rule_content['rule'] = {}
                rule_content['rule']['navi'] = navi_data
                rule_content['rule']['flip'] = flip_data
                rule_content['rule']['field'] = field_data
                if self.task_id == 0:
                    id = BasicDao.insert_single_task(rule_content)
                    if id:
                        self.task_id = id
                else:
                    BasicDao.update_single_task(rule_content)
                QMessageBox.information (self.prev,
                                     "温馨提示",
                                     "保存成功")
                print(rule_content)
        except Exception as a:
            QMessageBox.warning (self.prev,
                                 "温馨提示",
                                 "保存出错啦"+traceback.format_exc())

    def show_step(self,index):
        for i in range(3):
            if i == index:
                self.prev.split.widget(int(index)).show()
            else:
                self.prev.split.widget(i).hide()



    def next_step(self):
        if self.prev.step_label.acq_type ==  0 and self.step == 1:
            QMessageBox.warning (self.prev,
                                 "温馨提示",
                                 "请选择采集的网页类型")
            return

        if self.step == 1:
            if self.prev.step_label.acq_type ==  0:
                QMessageBox.warning (self.prev,
                                     "温馨提示",
                                     "请选择采集的网页类型")
                return
            else:
                if self.prev.step_label.acq_type < 3:
                    # 非单页模式
                    self.prev.step_label.no_singel_widget.show()
                    self.prev.step_label.singel_widget.hide()
                else:
                    self.prev.step_label.no_singel_widget.hide()
                    self.prev.step_label.singel_widget.show()

        if self.prev.step_label.acq_type !=3:  # 非单页采集的处理逻辑
            if self.step  == 0:
                if self.basic_step_process():
                    self.show_step(self.step+1)
                else:
                    self.step = self.step - 1
            elif self.step == 1:
                self.show_step(self.step+1)
                self.nvai_step_process()
            elif self.step == 2:
                if not self.prev.transcribe.step.navi_table.rowCount():
                    QMessageBox.warning (self.prev,
                                         "温馨提示",
                                         "您还未录制任何列表规则！")
                    return
                self.flip_step_process()
            elif self.step == 3:
                self.field_step_process()
            elif self.step == 4:
                self.finish_step_process()

            if self.step == 5:
                QMessageBox.warning (self.prev,
                                     "温馨提示",
                                     "已到最后一步!")
                return
            self.step = self.step + 1
        else:
            if self.step  == 0:
                if self.basic_step_process():
                    self.show_step(self.step+1)
                else:
                    self.step = self.step - 1
            elif self.step == 1:
                self.show_step(self.step+1)
                self.nvai_step_process()
            elif self.step == 2:
                self.flip_step_process()
            elif self.step == 3:
                if self.prev.step_label.acq_type !=3:
                    self.field_step_process()
                else:
                    self.finish_step_process()
            elif self.step == 4:
                if self.prev.step_label.acq_type !=3:
                    self.finish_step_process()
                else:
                    QMessageBox.warning (self.prev,
                                         "温馨提示",
                                         "已到最后一步!")
                    return

            if self.step == 5:
                QMessageBox.warning (self.prev,
                                     "温馨提示",
                                     "当前已是整个流程的最后一步!")
                return
            self.step = self.step + 1

    def prev_step(self):
        if self.step == 0:
            QMessageBox.warning (self.prev,
                                 "温馨提示",
                                 "当前已是整个流程的第一步!")
            return
        if self.step == 1:
            self.show_step(self.step-1)
            self.step = self.step-1
            m = QMovie('../images/s-step-1.gif')
            self.prev.step_label.basic_info.setMovie(m)
            m.start()
            self.prev.step_label.site_type.setPixmap(QPixmap('../images/c-step-2.png'))
        if self.step == 2:
            self.show_step(self.step-1)
            self.step = self.step-1
            m = QMovie('../images/s-step-2.gif')
            self.prev.step_label.site_type.setMovie(m)
            m.start()
            if self.prev.step_label.acq_type !=3:
                self.prev.step_label.navi.setPixmap(QPixmap('../images/c-step-3.png'))
            else:
                self.prev.step_label.single_field.setPixmap(QPixmap('../images/c-step-5.png'))
        if self.step == 3:
            self.step = self.step-1
            if self.prev.step_label.acq_type !=3:
                m = QMovie('../images/s-step-3.gif')
                self.prev.step_label.navi.setMovie(m)
                m.start()
                self.prev.step_label.flip.setPixmap(QPixmap('../images/c-step-4.png'))
                self.prev.transcribe.step.split.widget(1).show()
                self.prev.transcribe.step.split.widget(2).hide()
                self.prev.transcribe.step.split.widget(3).hide()
                self.prev.transcribe.step.illustrate.setText("请用鼠标点击页面中的列表项")
                self.prev.transcribe.browse.tabWidget.setCurrentIndex(0)
            else:
                m = QMovie('../images/s-step-5.gif')
                self.prev.step_label.single_field.setMovie(m)
                m.start()
                self.prev.step_label.single_filp.setPixmap(QPixmap('../images/c-step-4.png'))
                self.prev.transcribe.step.split.widget(3).show()
                self.prev.transcribe.step.split.widget(1).hide()
                self.prev.transcribe.step.split.widget(2).hide()
                self.prev.transcribe.step.illustrate.setText("请用鼠标点击需要采集的页面元素")

        if self.step == 4:
            self.step = self.step-1
            if self.prev.step_label.acq_type !=3:
                m = QMovie('../images/s-step-4.gif')
                self.prev.step_label.flip.setMovie(m)
                m.start()
                self.prev.step_label.field.setPixmap(QPixmap('../images/c-step-5.png'))
            else:
                m = QMovie('../images/s-step-4.gif')
                self.prev.step_label.single_filp.setMovie(m)
                m.start()
                self.prev.step_label.single_finish.setPixmap(QPixmap('../images/c-step-6.png'))
            self.prev.transcribe.step.split.widget(2).show()
            self.prev.transcribe.step.split.widget(1).hide()
            self.prev.transcribe.step.split.widget(3).hide()
            self.prev.transcribe.browse.tabWidget.setCurrentIndex(0)
            self.prev.transcribe.step.illustrate.setText("请用鼠标点击页面中的翻页元素，设置翻页规则。如果不设置，则默认不翻页。")
        if self.step == 5:
            self.step = self.step-1
            if self.prev.step_label.acq_type !=3:
                m = QMovie('../images/s-step-5.gif')
                self.prev.step_label.field.setMovie(m)
                m.start()
                self.prev.step_label.finish.setPixmap(QPixmap('../images/c-step-6.png'))
                self.prev.transcribe.step.split.widget(3).show()
                self.prev.transcribe.step.split.widget(1).hide()
                self.prev.transcribe.step.split.widget(2).hide()

    def show_setting(self):
        acq_setting = Ui_Acq_Setting(self.task_id)
        acq_setting.show()
        acq_setting.exec_()


    def basic_info_check(self,task_name,task_url,theme,category):
        if not task_name.strip():
            QMessageBox.warning (self.prev,
                                 "温馨提示",
                                 "任务名称不可为空!")
            self.prev.basic.site_name_edit.setFocus(True)
            return False
        if not task_url.strip():
            QMessageBox.warning (self.prev,
                                 "温馨提示",
                                 "采集网址不可为空!")
            self.prev.basic.site_url_edit.setFocus(True)
            return False
        if not Support.check_url(task_url):
            QMessageBox.warning (self.prev,
                                 "温馨提示",
                                 "您输入的采集网址不合法")
            self.prev.basic.site_url_edit.setFocus(True)
            return False
        if theme == "0":
            QMessageBox.warning (self.prev,
                                 "温馨提示",
                                 "您选择所属主题")
            self.prev.basic.task_theme_box.setFocus(True)
            return False
        if category == "0":
            QMessageBox.warning (self.prev,
                                 "温馨提示",
                                 "您选择所属类别")
            self.prev.basic.task_category_box.setFocus(True)
            return False
        return True


    def basic_step_process(self):
        """
        基本信息处理，验证基本信息和图标处理
        :return:
        """
    #     基本信息验证
        task_name = self.prev.basic.site_name_edit.text()
        task_url = self.prev.basic.site_url_edit.text()
        theme = self.prev.basic.task_theme_box.itemData(self.prev.basic.task_theme_box.currentIndex())
        category = self.prev.basic.task_category_box.itemData(self.prev.basic.task_category_box.currentIndex())
        if self.basic_info_check(task_name,task_url,theme,category):
            current_theme_code = self.prev.basic.task_theme_box.itemData(self.prev.basic.task_theme_box.currentIndex())
            if current_theme_code == "0":
                QMessageBox.warning (self.prev,
                                     "温馨提示",
                                     "请选择主题")
                self.prev.basic.task_theme_box.setFocus(True)
                return False
        #       图标处理
            m = QMovie('../images/s-step-2.gif')
            self.prev.step_label.site_type.setMovie(m)
            m.start()
            self.prev.step_label.basic_info.setPixmap(QPixmap('../images/c-step-1.png'))
            return True
        else:
            return False

    def nvai_step_process(self):
        """
        列表信息处理
        :return:
        """
        self.prev.transcribe.browse.webview.load(QUrl(self.prev.basic.site_url_edit.text()))


        if self.prev.step_label.acq_type !=3:
            m = QMovie('../images/s-step-3.gif')
            self.prev.step_label.navi.setMovie(m)
            m.start()
            self.prev.transcribe.step.split.widget(1).show()
            self.prev.transcribe.step.split.widget(2).hide()
            self.prev.transcribe.step.split.widget(3).hide()

            self.prev.transcribe.step.illustrate.setText("请用鼠标点击页面中的列表项")


        else:
            m = QMovie('../images/s-step-5.gif')
            self.prev.step_label.single_field.setMovie(m)
            m.start()

            self.prev.transcribe.step.split.widget(1).hide()
            self.prev.transcribe.step.split.widget(2).hide()
            self.prev.transcribe.step.split.widget(3).show()
            self.prev.transcribe.step.illustrate.setText("请用鼠标点击需要采集的页面元素")

        self.prev.step_label.basic_info.setPixmap(QPixmap('../images/c-step-1.png'))
        self.prev.step_label.site_type.setPixmap(QPixmap('../images/c-step-2.png'))
        self.prev.transcribe.browse.tabWidget.setCurrentIndex(0)

    def flip_step_process(self):
        """
        翻页处理
        :return:
        """
        if self.prev.step_label.acq_type !=3:
            m = QMovie('../images/s-step-4.gif')
            self.prev.step_label.flip.setMovie(m)
            m.start()
            self.prev.step_label.basic_info.setPixmap(QPixmap('../images/c-step-1.png'))
            self.prev.step_label.site_type.setPixmap(QPixmap('../images/c-step-2.png'))
            self.prev.step_label.navi.setPixmap(QPixmap('../images/c-step-3.png'))

            self.prev.transcribe.step.split.widget(1).hide()
            self.prev.transcribe.step.split.widget(2).show()
            self.prev.transcribe.step.split.widget(3).hide()


        else:
            m = QMovie('../images/s-step-4.gif')
            self.prev.step_label.single_filp.setMovie(m)
            m.start()
            self.prev.step_label.basic_info.setPixmap(QPixmap('../images/c-step-1.png'))
            self.prev.step_label.site_type.setPixmap(QPixmap('../images/c-step-2.png'))
            self.prev.step_label.single_field.setPixmap(QPixmap('../images/c-step-5.png'))

            self.prev.transcribe.step.split.widget(2).show()
            self.prev.transcribe.step.split.widget(1).hide()
            self.prev.transcribe.step.split.widget(3).hide()
        self.prev.transcribe.step.illustrate.setText("请用鼠标点击页面中的翻页元素，设置翻页规则。如果不设置，则默认不翻页。")
        self.prev.transcribe.browse.tabWidget.setCurrentIndex(0)


    def field_step_process(self):
        """
        详情处理
        :return:
        """
        m = QMovie('../images/s-step-5.gif')
        self.prev.step_label.field.setMovie(m)
        m.start()
        self.prev.step_label.basic_info.setPixmap(QPixmap('../images/c-step-1.png'))
        self.prev.step_label.site_type.setPixmap(QPixmap('../images/c-step-2.png'))
        self.prev.step_label.navi.setPixmap(QPixmap('../images/c-step-3.png'))
        self.prev.step_label.flip.setPixmap(QPixmap('../images/c-step-4.png'))

        self.prev.transcribe.step.split.widget(1).hide()
        self.prev.transcribe.step.split.widget(2).hide()
        self.prev.transcribe.step.split.widget(3).show()

        self.prev.transcribe.step.illustrate.setText("请用鼠标点击需要采集的页面元素")
        self.prev.transcribe.browse.tabWidget.setCurrentIndex(1);
        # self.prev.transcribe.browse.tabWidget.currentWidget().centralWidget().page().runJavaScript(MyJs.INIT_EVENT)


    def finish_step_process(self):
        """
        结束保存处理
        :return:
        """
        self.prev.step_label.basic_info.setPixmap(QPixmap('../images/c-step-1.png'))
        self.prev.step_label.site_type.setPixmap(QPixmap('../images/c-step-2.png'))
        self.prev.step_label.navi.setPixmap(QPixmap('../images/c-step-3.png'))
        self.prev.step_label.flip.setPixmap(QPixmap('../images/c-step-4.png'))
        self.prev.step_label.field.setPixmap(QPixmap('../images/c-step-5.png'))
        self.prev.step_label.finish.setPixmap(QPixmap('../images/c-step-6.png'))

        self.prev.step_label.single_finish.setPixmap(QPixmap('../images/c-step-6.png'))
        self.prev.step_label.single_filp.setPixmap(QPixmap('../images/c-step-4.png'))
        self.prev.step_label.single_field.setPixmap(QPixmap('../images/c-step-5.png'))





