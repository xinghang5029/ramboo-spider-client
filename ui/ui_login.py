# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import QApplication,QGridLayout,QWidget,QVBoxLayout,QPushButton,QLineEdit,QCheckBox,QLabel
from PyQt5.QtCore import Qt
from PyQt5.Qt import QCursor
import sys

class Ui_login(QWidget):
    def __init__(self,parent=None):
        super(QWidget,self).__init__(parent)
        self.init_ui()


    def init_ui(self):
        # 设置窗体无边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedSize(620,500);
        # 设置背景透明
        self.setAttribute(Qt.WA_TranslucentBackground)
        parent_grid = QVBoxLayout()
        parent_grid.setSpacing(0)
        self.setLayout(parent_grid)

        top_grid_widget = QWidget(self)
        top_grid_widget.setObjectName("top_widget")
        top_grid = QGridLayout()
        top_grid_widget.setLayout(top_grid)
        top_grid_widget.setFixedSize(600,150)
        top_grid.setSpacing(0)
        top_grid.setContentsMargins(0,0,0,0)
        top_grid.setAlignment(Qt.AlignRight|Qt.AlignTop)
        top_grid_widget.setStyleSheet("#top_widget{border-image:url(images/login.png)}")


        close_btn_style = r'QPushButton{border:solid 0px grey;width:30px;height:30px;border-radius:0px;color:white;}' \
                     r'QPushButton:hover{background-color:rgb(220,20,60); border-style: inset; }'
        min_btn_style = r'QPushButton{border:solid 0px grey;width:30px;height:30px;border-radius:0px;color:white;}' \
                          r'QPushButton:hover{background-color:rgb(220,220,220); border-style: inset; }'
        close_btn = QPushButton(top_grid_widget)
        close_btn.setText("X")
        close_btn.setStyleSheet(close_btn_style)
        close_btn.setContentsMargins(0,0,0,0)
        close_btn.clicked.connect(self.close)
        min_btn = QPushButton(top_grid_widget)
        min_btn.setText("-")
        min_btn.setStyleSheet(min_btn_style)
        min_btn.setContentsMargins(0,0,0,0)
        min_btn.clicked.connect(self.showMinimized)


        top_grid.addWidget(close_btn,0,1,1,1)
        top_grid.addWidget(min_btn,0,0,1,1)




        button_grid_widget = QWidget(self)
        button_grid = QGridLayout()
        button_grid_widget.setLayout(button_grid)
        button_grid_widget.setFixedSize(600,330)
        # button_grid_widget.setStyleSheet("border-image:url(images/buttom.png) 20 12 10 12")
        button_grid_widget.setStyleSheet("QWidget{border: 1px solid #7EC0EE;background:white}")
        button_grid.setSpacing(0)
        button_grid.setContentsMargins(0,30,0,0)
        button_grid.setAlignment(Qt.AlignTop|Qt.AlignHCenter)
        parent_grid.addWidget(top_grid_widget)
        parent_grid.addWidget(button_grid_widget)



        line_edit_style = "QLineEdit{background:transparent;border-width:0;border-image:url(images/line.png)}" \
                          "QLineEdit:focus{border-image:url(images/line_focus.png)}"


        username_edit = QLineEdit(button_grid_widget)
        username_edit.setPlaceholderText("请输入用户名");
        username_edit.setObjectName("username")
        username_edit.setStyleSheet(line_edit_style)
        username_edit.setFixedSize(400,50)
        username_edit.setFocus(True)

        password_edit = QLineEdit(button_grid_widget)
        password_edit.setPlaceholderText("请输入密码");
        password_edit.setObjectName("password")
        password_edit.setStyleSheet(line_edit_style)
        password_edit.setEchoMode(QLineEdit.Password)
        password_edit.setFixedSize(400,50)

        menu_widget = QWidget(button_grid_widget)
        menu_widget.setObjectName("menu_widget")
        menu_widget.setStyleSheet("#menu_widget{margin-top: 80px;border-width:0px}")
        menu_grid = QGridLayout()
        menu_widget.setLayout(menu_grid)
        menu_grid.setContentsMargins(0,30,0,0)
        menu_grid.setAlignment(Qt.AlignLeft)

        check_box_style = "QCheckBox{border: 0px solid gray;border-radius: 3px;padding: 1px 18px 1px 3px;min-width: 6em;}"
        remember_box = QCheckBox('记住密码', menu_widget)
        remember_box.setStyleSheet(check_box_style)
        autologin_box = QCheckBox('自动登录', menu_widget)
        autologin_box.setStyleSheet(check_box_style)
        menu_grid.addWidget(remember_box,0,0,1,1)
        menu_grid.addWidget(autologin_box,0,1,1,1)


        spacing = QLabel(button_grid_widget)
        spacing.setText("")
        spacing.setFixedSize(400,40)
        spacing.setVisible(True)
        spacing.setStyleSheet("QLabel{background: transparent;border:solid 0px grey}")

        spacing1 = QLabel(button_grid_widget)
        spacing1.setText("")
        spacing1.setFixedSize(400,10)
        spacing1.setVisible(True)
        spacing1.setStyleSheet("QLabel{background: transparent;border:solid 0px grey}")

        login_btn_style = r'QPushButton{font:bold 20px;border:solid 1px grey;width:30px;height:60px;border-radius:0px;color:white;border-image:url(images/login-btn.png)}' \
                        r'QPushButton:hover{ border-style: inset; }'

        login_btn = QPushButton(button_grid_widget)
        login_btn.setText("登录")
        login_btn.setStyleSheet(login_btn_style)


        button_grid.addWidget(username_edit,0,0,1,1)
        button_grid.addWidget(spacing1,1,0,1,1)
        button_grid.addWidget(password_edit,2,0,1,1)
        button_grid.addWidget(menu_widget,3,0,1,1)
        button_grid.addWidget(spacing,4,0,1,1)
        button_grid.addWidget(login_btn,5,0,1,1)






    def close(self):
        '''
        关闭应用程序
        :return:
        '''
        app = QApplication(sys.argv)
        app.exit(0)

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
    login = Ui_login()
    login.show()
    sys.exit(app.exec_())


