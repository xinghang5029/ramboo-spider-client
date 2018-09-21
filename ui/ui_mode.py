# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication,QMainWindow,QSplitter,QWidget,\
    QHBoxLayout,QLabel
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPixmap
from ui.ui_label import My_Label

import sys

class Ui_Mode(QMainWindow):
    """
    模式选择界面
    """

    def __init__(self, prev,parent = None):
        QMainWindow.__init__(self, parent)
        self.prev = prev
        self.setWindowTitle("规则录制界面")


        self.split = QSplitter(self)
        self.split.setOrientation(Qt.Vertical)
        self.split.setContentsMargins(0,10,10,0)

        self.label = QLabel(self.split)
        self.label.setText("请选择您要采集的网页类型")
        self.label.setStyleSheet("font:bold;color:#8A2BE2")
        self.label.setContentsMargins(10,10,10,10)

        self.mode_widget = QWidget(self.split)
        self.mode_widget_layout = QHBoxLayout()
        self.mode_widget.setLayout(self.mode_widget_layout)
        self.mode_widget.setStyleSheet("background:#7CCD7C")

        self.mode_1 = My_Label(1,self)
        self.mode_2 = My_Label(2,self)
        self.mode_3 = My_Label(3,self)
        mode_image_1= QPixmap('../images/mode-1.png')
        mode_image_2= QPixmap('../images/mode-2.png')
        mode_image_3= QPixmap('../images/mode-3.png')
        self.mode_1.setPixmap(mode_image_1)
        self.mode_2.setPixmap(mode_image_2)
        self.mode_3.setPixmap(mode_image_3)

        self.mode_widget_layout.addStretch()
        self.mode_widget_layout.addWidget(self.mode_1)
        self.mode_widget_layout.addWidget(self.mode_2)
        self.mode_widget_layout.addWidget(self.mode_3)
        self.mode_widget_layout.addStretch()



        self.mode_illustrate_widget = QWidget(self.split)
        self.mode_illustrate_widget_layout = QHBoxLayout()
        self.mode_illustrate_widget.setLayout(self.mode_illustrate_widget_layout)
        # self.mode_illustrate_widget.setStyleSheet("background:white")
        self.i_mode = QLabel(self.mode_illustrate_widget)
        i_mode_image= QPixmap('../images/i-mode-1.png')
        self.i_mode.setPixmap(i_mode_image)
        self.mode_illustrate_widget_layout.addStretch()
        self.mode_illustrate_widget_layout.addWidget(self.i_mode)
        self.mode_illustrate_widget_layout.addStretch()





        self.split.addWidget(self.label)
        self.split.addWidget(self.mode_widget)
        self.split.addWidget(self.mode_illustrate_widget)
        self.split.setStretchFactor(0,1)
        self.split.setStretchFactor(2,50)
        self.split.setStretchFactor(3,500)

        self.setCentralWidget(self.split)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Ui_Mode()
    main.show()
    sys.exit(app.exec_())