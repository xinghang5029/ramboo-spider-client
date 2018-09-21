# -*- coding: utf-8 -*

from dao.basic_dao import BasicDao
from PyQt5.QtGui import QPixmap
from util.table_util import Table_Util
import json,re

class BasicProcess(object):

    def __init__(self,widget):
        self.widget = widget


    def load_data(self,task_id):
        """
        根据站点id加载采集的录制规则
        :param task_id:
        :return:
        """
        theme_list = BasicDao.get_all_theme()
        self.widget.task_theme_box.addItem("请选择","0")
        theme_code_list = ['0']
        for theme in theme_list:
            self.widget.task_theme_box.addItem(theme['name'],theme['code'])
            theme_code_list.append(theme['code'])
        info = BasicDao.task_info_by_id(task_id)
        if info:
            # =================================基本信息=====================================================
            self.widget.site_name_edit.setText(info['name'])
            self.widget.site_url_edit.setText(info['url'])
            self.widget.task_theme_box.setCurrentIndex(theme_code_list.index(info['theme']))
            index = self.widget.category_code_list.index(info['category'])
            if index > 0:
                index = index -1
            self.widget.task_category_box.setCurrentIndex(index)
            # ==================================采集模式=====================================================
            self.widget.prev.mode.mode_1.setPixmap(QPixmap('../images/mode-1.png'))
            self.widget.prev.mode.mode_2.setPixmap(QPixmap('../images/mode-2.png'))
            self.widget.prev.mode.mode_3.setPixmap(QPixmap('../images/mode-3.png'))
            self.widget.prev.step_label.acq_type =  info['acqType']
            if info['acqType'] != 0:
                mode_list = [self.widget.prev.mode.mode_1,self.widget.prev.mode.mode_2,self.widget.prev.mode.mode_3]
                mode_list[info['acqType']-1].setPixmap(QPixmap('../images/s-mode-{}.png'.format(str(info['acqType']))))

            # ==================================列表内容=====================================================
            rule = json.loads(info['rule'])
            if rule['navi']:
                for info in rule['navi']:
                    Table_Util.insert_single_data(self.widget.prev.transcribe.step.navi_table,info)

            #  ==================================翻页内容=====================================================
            if rule['flip']:
                for info in rule['flip']:
                    Table_Util.insert_single_data(self.widget.prev.transcribe.step.flip_table,info)
            #  ==================================详情内容=====================================================
            if rule['field']:
                for info in rule['field']:
                    Table_Util.insert_single_data(self.widget.prev.transcribe.step.field_table,info)

