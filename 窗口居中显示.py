import sys #能获取参数的api
from PyQt5.QtWidgets import QDesktopWidget,QMainWindow,QApplication #QDesktopWidget api可以获取屏幕尺寸
from PyQt5.QtGui import QIcon #添加图标的api

class centerform(QMainWindow): #继承QMainWindow
    def __init__(self,parent=None):
        super(centerform,self).__init__(parent)

        self.setWindowTitle('窗口居中')

        self.resize(400,300)#设置窗口尺寸
        self.status =self.statusBar()#获取状态栏
        self.status.showMessage('状态栏显示消息5秒',5000)


    def center(self):
        screen=QDesktopWidget().screenGeometry()

        size=self.geometry()
        newleft=(screen.width()-size.width()/2)
        newtop=(screen.height()-size.height()/2)

        #self.move(newleft,newtop)        #居中显示
        self.move(1000,0)  #移动到（1000,0）坐标

if __name__=='__main__':
    app =QApplication(sys.argv)
    app.setWindowIcon(QIcon('./images/01.jpg')) #设置图标
    main=centerform()
    main.center()
    main.show()
    sys.exit(app.exec())
