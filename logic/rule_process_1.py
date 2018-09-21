# -*- coding: utf-8 -*-
from PyQt5.QtCore import QUrl
from PyQt5.QtWebChannel import QWebChannel
from util.pageToQt import PageToQt
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPixmap,QMovie
class RuleProcess(object):

    """
    整个规则录制处理类
    """
    step = 0
    sub_step = 0
    def __init__(self,prev):
        self.prev = prev
        self.step_obj = [self.prev.step_label.basic_info,self.prev.step_label.site_type,self.prev.step_label.navi,
                         self.prev.step_label.flip,self.prev.step_label.field,self.prev.step_label.finish]



    def process(self,index):
        try:
            if index == 0:
                self.prev_step()
            elif index == 1:
                self.next_step()

        except Exception as a:
            print(a)


    def show_step(self,index):
        for i in range(3):
            if i == index:
                self.prev.split.widget(int(index)).show()
            else:
                self.prev.split.widget(i).hide()


    def next_step(self):
        if self.prev.step_label.acq_type ==  0 and RuleProcess.step == 1:
            QMessageBox.warning (self.prev,
                                 "温馨提示",
                                 "请选择采集的网页类型")
            return
        # 非单页采集的处理逻辑
        if self.prev.step_label.acq_type !=3:
            if RuleProcess.step == 2:
                if  RuleProcess.sub_step == 3:
                    QMessageBox.warning (self.prev,
                                         "温馨提示",
                                         "当前步骤已是最后一步,无法再继续下一步！")
                    return
                else:
                    RuleProcess.sub_step = RuleProcess.sub_step + 1
                    print(str(RuleProcess.sub_step))
                for i in range(6):
                    if not self.step_obj[i].isHidden():
                        self.step_obj[i].setPixmap(QPixmap('../images/c-step-{}.png'.format(i+1)))
                m = QMovie('../images/s-step-{}.gif'.format(RuleProcess.sub_step+3))
                self.step_obj[RuleProcess.step+RuleProcess.sub_step].setMovie(m)
                m.start()
            else:
                self.show_step(RuleProcess.step+1)
                RuleProcess.step = RuleProcess.step + 1
                for i in range(6):
                    if not self.step_obj[i].isHidden():
                        self.step_obj[i].setPixmap(QPixmap('../images/c-step-{}.png'.format(i+1)))

                m = QMovie('../images/s-step-{}.gif'.format(RuleProcess.step+1))
                self.step_obj[RuleProcess.step].setMovie(m)
                m.start()
        else:
            print("单页采集")
            self.show_step(RuleProcess.step+1)
            if RuleProcess.step == 1:
                self.prev.step_label.basic_info.setPixmap(QPixmap('../images/c-step-1.png'))
                self.prev.step_label.site_type.setPixmap(QPixmap('../images/c-step-2.png'))
                self.prev.step_label.flip.setPixmap(QPixmap('../images/c-step-4.png'))
                self.prev.step_label.field.setPixmap(QPixmap('../images/step-6.png'))
                self.prev.step_label.finish.hide()
                m = QMovie('../images/s-step-5.gif')
                self.prev.step_label.navi.setMovie(m)
                m.start()
                RuleProcess.step = RuleProcess.step + 1
            elif RuleProcess.step == 2:
                self.prev.step_label.basic_info.setPixmap(QPixmap('../images/c-step-1.png'))
                self.prev.step_label.site_type.setPixmap(QPixmap('../images/c-step-2.png'))
                self.prev.step_label.navi.setPixmap(QPixmap('../images/c-step-5.png'))
                self.prev.step_label.field.setPixmap(QPixmap('../images/step-6.png'))
                self.prev.step_label.finish.hide()
                m = QMovie('../images/s-step-4.gif')
                self.prev.step_label.flip.setMovie(m)
                m.start()
                RuleProcess.step = RuleProcess.step + 1
            elif RuleProcess.step == 3:
                self.prev.step_label.basic_info.setPixmap(QPixmap('../images/c-step-1.png'))
                self.prev.step_label.site_type.setPixmap(QPixmap('../images/c-step-2.png'))
                self.prev.step_label.navi.setPixmap(QPixmap('../images/c-step-5.png'))
                self.prev.step_label.flip.setPixmap(QPixmap('../images/c-step-4.png'))
                self.prev.step_label.finish.hide()
                m = QMovie('../images/s-step-6.gif')
                self.prev.step_label.field.setMovie(m)
                m.start()
                RuleProcess.step = RuleProcess.step + 1
            else:
                QMessageBox.warning (self.prev,
                                     "温馨提示",
                                     "当前步骤已是最后一步,无法再继续下一步！")
                return


            # m = QMovie('../images/s-step-{}.gif'.format(RuleProcess.step+3))
            # self.step_obj[RuleProcess.step+1].setMovie(m)
            # m.start()



    def prev_step(self):
        if self.prev.step_label.acq_type !=3:
            if RuleProcess.step == 0:
                QMessageBox.warning (self.prev,
                                     "温馨提示",
                                     "当前步骤已是第一步了,无法再返回上一步！")
                return
            elif RuleProcess.step == 1:
                pass
            else:
                if RuleProcess.sub_step > 0:
                    RuleProcess.step = RuleProcess.step + 1
                    RuleProcess.sub_step = RuleProcess.sub_step - 1
                    print(str(RuleProcess.sub_step))
            self.show_step(RuleProcess.step-1)
            RuleProcess.step = RuleProcess.step - 1

            for i in range(6):
                if not self.step_obj[i].isHidden():
                    self.step_obj[i].setPixmap(QPixmap('../images/c-step-{}.png'.format(i+1)))
            if RuleProcess.step == 2:
                m = QMovie('../images/s-step-{}.gif'.format(RuleProcess.sub_step+3))
                self.step_obj[RuleProcess.step+RuleProcess.sub_step].setMovie(m)
                m.start()
            else:
                m = QMovie('../images/s-step-{}.gif'.format(RuleProcess.step+1))
                self.step_obj[RuleProcess.step].setMovie(m)
                m.start()
        else:
            if RuleProcess.step == 1:
                self.prev.step_label.basic_info.setPixmap(QPixmap('../images/c-step-1.png'))
                self.prev.step_label.site_type.setPixmap(QPixmap('../images/c-step-2.png'))
                self.prev.step_label.navi.setPixmap(QPixmap('../images/c-step-5.png'))
                self.prev.step_label.flip.setPixmap(QPixmap('../images/c-step-4.png'))
                self.prev.step_label.finish.hide()
                m = QMovie('../images/s-step-6.gif')
                self.prev.step_label.field.setMovie(m)
                m.start()
                RuleProcess.step = RuleProcess.step + 1