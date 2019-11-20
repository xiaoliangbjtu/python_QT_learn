'''
主窗口类型：
QMainWindow:可以包含菜单栏、工具栏、和标题栏。
QWidget:不确定窗口的用途，就使用。
QDialog:是对话窗口的基类。没有菜单栏、工具栏、状态栏。
'''

import sys #能获取参数的api
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon #添加图标的api

class firstmainwin(QMainWindow): #继承QMainWindow
    def __init__(self,parent=None):
        super(firstmainwin,self).__init__(parent)

        self.setWindowTitle('第一个窗口应用程序')

        self.resize(400,300)#设置窗口尺寸
        self.status =self.statusBar()#获取状态栏
        self.status.showMessage('状态栏显示消息5秒',5000)

if __name__=='__main__':
    app =QApplication(sys.argv)
    app.setWindowIcon(QIcon('./images/01.jpg')) #设置图标
    main=firstmainwin()
    main.show()
    sys.exit(app.exec())