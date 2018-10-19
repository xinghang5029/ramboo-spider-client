# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import QApplication,QGridLayout,QDialog,QWidget,QVBoxLayout,QPushButton,QLineEdit,\
    QTextEdit,QCheckBox,QLabel,QRadioButton,QButtonGroup,QSpinBox,QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.Qt import QCursor
from dao.basic_dao import BasicDao
import sys,json
class Ui_Acq_Setting(QDialog):
    def __init__(self,task_id,parent=None):
        super(QDialog,self).__init__(parent)
        self.task_id = task_id
        self.init_ui()


    def init_ui(self):
        # 设置窗体无边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedSize(500,600);
        # 设置背景透明
        self.setAttribute(Qt.WA_TranslucentBackground)
        parent_grid = QVBoxLayout()
        parent_grid.setSpacing(0)
        self.setLayout(parent_grid)

        top_grid_widget = QWidget(self)
        top_grid_widget.setObjectName("top_widget")
        top_grid = QGridLayout()
        top_grid_widget.setLayout(top_grid)
        top_grid_widget.setFixedHeight(40)
        top_grid.setSpacing(0)
        top_grid.setContentsMargins(0,0,0,0)
        top_grid.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
        top_grid_widget.setStyleSheet("#top_widget{background:#434343;border-top-right-radius: 5px;border-top-left-radius: 5px}")


        close_btn_style = r'QPushButton{border:solid 0px grey;width:40px;height:40px;border-radius:0px;color:white;}' \
                     r'QPushButton:hover{background-color:rgb(220,20,60); border-style: inset; }'
        min_btn_style = r'QPushButton{border:solid 0px grey;width:40px;height:40px;border-radius:0px;color:white;}' \
                          r'QPushButton:hover{background-color:rgb(220,220,220); border-style: inset; }'
        close_btn = QPushButton(top_grid_widget)
        close_btn.setText("X")
        close_btn.setStyleSheet(close_btn_style)
        close_btn.setContentsMargins(0,0,0,0)
        close_btn.clicked.connect(self.close_dialog)
        min_btn = QPushButton(top_grid_widget)
        min_btn.setText("-")
        min_btn.setStyleSheet(min_btn_style)
        min_btn.setContentsMargins(0,0,0,0)
        min_btn.clicked.connect(self.showMinimized)
        title_label = QLabel(top_grid_widget)
        title_label.setText("采集设置")
        title_label.setStyleSheet("QLabel{font:bold;color:white;margin-right:125}")



        top_grid.addWidget(close_btn,0,2,1,1)
        top_grid.addWidget(min_btn,0,1,1,1)
        top_grid.addWidget(title_label,0,0,1,1)

        button_grid_widget = QWidget(self)
        button_grid = QGridLayout()
        button_grid_widget.setLayout(button_grid)
        button_grid_widget.setStyleSheet("QWidget{background:#F5F5F5}")
        button_grid.setSpacing(20)
        button_grid.setContentsMargins(35,30,0,0)
        button_grid.setAlignment(Qt.AlignTop|Qt.AlignLeft)

        yr_label = QLabel(button_grid_widget)
        yr_label.setText("导航动态渲染")
        yr_label.setStyleSheet("font:bold;")
        yr_buttonGroup=QButtonGroup(button_grid_widget)
        self.yr_yes=QRadioButton('是')
        self.yr_no=QRadioButton('否')
        self.yr_no.setChecked(True)
        yr_buttonGroup.addButton(self.yr_yes)
        yr_buttonGroup.addButton(self.yr_no)


        detail_yr_label = QLabel(button_grid_widget)
        detail_yr_label.setText("详情动态渲染")
        detail_yr_label.setStyleSheet("font:bold;")
        detail_yr_buttonGroup=QButtonGroup(button_grid_widget)
        self.detail_yr_yes=QRadioButton('是')
        self.detail_yr_no=QRadioButton('否')
        self.detail_yr_no.setChecked(True)
        detail_yr_buttonGroup.addButton(self.detail_yr_yes)
        detail_yr_buttonGroup.addButton(self.detail_yr_no)

        ip_label = QLabel(button_grid_widget)
        ip_label.setText("使用IP代理")
        ip_label.setStyleSheet("font:bold;")
        ip_buttonGroup=QButtonGroup(button_grid_widget)
        self.ip_yes=QRadioButton('是')
        self.ip_no=QRadioButton('否')
        self.ip_yes.setChecked(True)
        ip_buttonGroup.addButton(self.ip_yes)
        ip_buttonGroup.addButton(self.ip_no)

        ua_label = QLabel(button_grid_widget)
        ua_label.setText("用户代理(UA)")
        ua_label.setStyleSheet("font:bold;")
        ua_buttonGroup=QButtonGroup(button_grid_widget)
        self.ua_default=QRadioButton('默认')
        self.ua_random=QRadioButton('随机')
        self.ua_default.setChecked(True)
        ua_buttonGroup.addButton(self.ua_default)
        ua_buttonGroup.addButton(self.ua_random)
        ua_pool_btn = QPushButton(button_grid_widget)
        ua_pool_btn.setText("UA池")
        self.us_default_value = QTextEdit(button_grid_widget)

        navi_thread_label = QLabel(button_grid_widget)
        navi_thread_label.setText("导航线程数")
        navi_thread_label.setStyleSheet("font:bold;")

        self.navi_thread_num = QSpinBox(button_grid_widget)
        self.navi_thread_num.setStyleSheet(r'QSpinBox{height:30;width:50;background:white}')

        detail_thread_label = QLabel(button_grid_widget)
        detail_thread_label.setText("详情线程数")
        detail_thread_label.setStyleSheet("font:bold;")

        self.detail_thread_num = QSpinBox(button_grid_widget)
        self.detail_thread_num.setStyleSheet(r'QSpinBox{height:30;width:50;background:white}')

        self.saveBtn = QPushButton(button_grid_widget)
        self.saveBtn.setText("确定")
        self.saveBtn.setStyleSheet(r'QPushButton{background-color:#6495ED;color:white}')
        self.saveBtn.clicked.connect(self.save_setting)
        self.cancelBtn = QPushButton(button_grid_widget)
        self.cancelBtn.setText("取消")
        self.cancelBtn.setStyleSheet(r'QPushButton{background-color:grey;color:white}')
        self.cancelBtn.clicked.connect(self.close_dialog)

        button_grid.addWidget(ip_label,0,0,1,1)
        button_grid.addWidget(self.ip_yes,0,1,1,1)
        button_grid.addWidget(self.ip_no,0,2,1,1)

        button_grid.addWidget(yr_label,1,0,1,1)
        button_grid.addWidget(self.yr_yes,1,1,1,1)
        button_grid.addWidget(self.yr_no,1,2,1,1)

        button_grid.addWidget(detail_yr_label,2,0,1,1)
        button_grid.addWidget(self.detail_yr_yes,2,1,1,1)
        button_grid.addWidget(self.detail_yr_no,2,2,1,1)



        button_grid.addWidget(ua_label,3,0,1,1)
        button_grid.addWidget(self.ua_default,3,1,1,1)
        button_grid.addWidget(self.ua_random,3,2,1,1)
        button_grid.addWidget(ua_pool_btn,3,3,1,1)

        button_grid.addWidget(self.us_default_value,4,0,1,4)

        button_grid.addWidget(navi_thread_label,5,0,1,1)
        button_grid.addWidget(self.navi_thread_num,5,1,1,1)

        button_grid.addWidget(detail_thread_label,5,2,1,1)
        button_grid.addWidget(self.detail_thread_num,5,3,1,1)

        button_grid.addWidget(self.saveBtn,7,2,1,1)
        button_grid.addWidget(self.cancelBtn,7,3,1,1)



        button_grid.setRowStretch(0,1)
        button_grid.setRowStretch(1,1)
        button_grid.setRowStretch(2,1)
        button_grid.setRowStretch(3,2)
        button_grid.setRowStretch(4,1)
        button_grid.setRowStretch(5,1)
        button_grid.setRowStretch(6,1)
        button_grid.setRowStretch(7,1)
        button_grid.setRowStretch(8,1)




        parent_grid.addWidget(top_grid_widget)
        parent_grid.addWidget(button_grid_widget)

        self.load_data()






    def save_setting(self):
        if self.task_id == 0:
            QMessageBox.information(self,"温馨提示","请先保存录制的站点规则，再设置采集规则")

        else:
            acq_strategy = {}
            acq_strategy['ipProxy'] = (0 if (self.ip_yes.isChecked()) else 1)
            acq_strategy['navi_flag'] = (0 if (self.yr_yes.isChecked()) else 1)
            acq_strategy['detail_flag'] = (0 if (self.detail_yr_yes.isChecked()) else 1)
            acq_strategy['ua'] = (0 if (self.ua_default.isChecked()) else 1)
            acq_strategy['ua_default'] = self.us_default_value.toPlainText()
            acq_strategy['navi_thread'] = self.navi_thread_num.text()
            acq_strategy['detail_thread'] = self.detail_thread_num.text()

            BasicDao.save_acq_strategy(self.task_id,json.dumps(acq_strategy))

            print(acq_strategy)
        self.close_dialog()


    def load_data(self):
        if self.task_id:
            info = BasicDao.query_strategy_by_taskid(self.task_id)
            if info:
                rule = json.loads(info['rule'])
                self.ip_no.setChecked((False if (rule['ipProxy']==0) else True))
                # self.ip_no.setChecked(True)
                self.yr_yes.setChecked((True if (rule['navi_flag']==0) else False))
                self.detail_yr_yes.setChecked((True if (rule['detail_flag']==0) else False))
                self.ua_random.setChecked((False if (rule['ua']==0) else True))
                self.navi_thread_num.setValue(int(rule['navi_thread']))
                self.detail_thread_num.setValue(int(rule['detail_thread']))







    def close_dialog(self):
        '''
        关闭应用程序
        :return:
        '''
        try:
            self.close()
        except Exception as a:
            print(a)

    # 以下三个函数是覆写窗体函数，实现无标题移动功能
    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos() #获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  #更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos()-self.m_Position)#更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        self.setCursor(QCursor(Qt.ArrowCursor))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Ui_Acq_Setting()
    login.show()
    sys.exit(app.exec_())


