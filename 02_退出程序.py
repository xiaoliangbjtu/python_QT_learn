import sys
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QPushButton,QWidget

class QuiApplication(QMainWindow):
    def __init__(self):
        super(QuiApplication, self).__init__()
        self.resize(500,700)
        self.setWindowTitle('退出程序')

#添加按钮
        self.button1=QPushButton('退出程序')

        #将信号与槽关联
        self.button1.clicked.connect(self.onClick_button)
        layout=QHBoxLayout()
        layout.addWidget(self.button1)

        mainframe=QWidget()
        mainframe.setLayout(layout)

        self.setCentralWidget(mainframe)


    def onClick_button(self):#按钮单击事件方法（自定义的槽）
        sender =self.sender()
        print(sender.text()+'按钮被按下')
        app =QApplication.instance()
        #退出应用程序
        app.quit()

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QuiApplication()
    main.show()
    sys.exit(app.exec())