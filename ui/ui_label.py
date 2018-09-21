# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QLabel,QMessageBox
from PyQt5.QtGui import QPixmap

class My_Label(QLabel):
    """
    针对采集模式的标签
    """
    def __init__(self,index,prev,parent=None):
        super(My_Label,self).__init__(parent)
        self.index = index
        self.prev = prev



    def mouseMoveEvent(self,e):
        pass


    def mousePressEvent(self,e):
        """
        采集模式选择处理逻辑
        :param e:
        :return:
        """
        try:
            self.prev.prev.step_label.acq_type = self.index
            self.prev.mode_1.setPixmap(QPixmap('../images/mode-1.png'))
            self.prev.mode_2.setPixmap(QPixmap('../images/mode-2.png'))
            self.prev.mode_3.setPixmap(QPixmap('../images/mode-3.png'))
            self.setPixmap(QPixmap('../images/s-mode-{}.png'.format(str(self.index))))
            self.prev.i_mode.setPixmap(QPixmap('../images/i-mode-{}.png'.format(str(self.index))))
            if self.index < 3:
                # 非单页模式
                self.prev.prev.step_label.no_singel_widget.show()
                self.prev.prev.step_label.singel_widget.hide()
            else:
                self.prev.prev.step_label.no_singel_widget.hide()
                self.prev.prev.step_label.singel_widget.show()


        except Exception as a:
            QMessageBox.warning (self.prev,
                                 "错误信息",
                                 "模式选择异常{}".format(str(a)))
            return



    def mouseReleaseEvent(self,e):
        pass


class My_Label_TWO(QLabel):
    def __init__(self,index,prev,parent=None):
        super(My_Label_TWO,self).__init__(parent)
        self.index = index
        self.prev = prev


    def mouseMoveEvent(self,e):
        pass


    def mousePressEvent(self,e):

        pass


    def mouseReleaseEvent(self,e):
        pass
