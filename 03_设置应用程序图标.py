import sys #能获取参数的api
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon #添加图标的api

'''
窗口的setwindowicon方法用于设置窗口的图标，只在windows中可用
QApplication中的setwindowIcon方法用于设置主窗口的图标和应用程序的图标，但调用了窗口的setwindowIcon方法。
QApplication中的setwindowIcon方法就只能用于设置应用程序图标了
'''

class Iconform(QMainWindow): #继承QMainWindow
    def __init__(self,parent=None):
        super(Iconform,self).__init__(parent)
        self.initUI()
    def initUI(self):
        self.setWindowTitle('设置图标')
        self.setGeometry(600,600,250,250)
        self.setWindowIcon(QIcon('./images/01.jpg'))

if __name__=='__main__':
    app =QApplication(sys.argv)
   # app.setWindowIcon(QIcon('./images/01.jpg')) #设置图标
    main=Iconform()
    main.show()
    sys.exit(app.exec())