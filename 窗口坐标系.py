import sys
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QPushButton,QWidget

def onClick_Button():
    print('1')
    print(widget.x()," ",end="")  #窗口坐标x
    print(widget.y()," ",end="")  #窗口坐标y
    print(widget.width()," ",end="")  #工作区宽度
    print(widget.height())  #工作区高度

    print('2')
    print(widget.geometry().x()," ",end="")  #工作区
    print(widget.geometry().y()," ",end="")   #工作区
    print(widget.geometry().width()," ",end="")  #工作区
    print(widget.geometry().height())  #工作区

    print('3')
    print(widget.frameGeometry().x()," ",end="")  #窗口
    print(widget.frameGeometry().y()," ",end="")  #窗口
    print(widget.frameGeometry().width()," ",end="")  #窗口
    print(widget.frameGeometry().height())  #窗口



app= QApplication(sys.argv)

widget=QWidget()
btn=QPushButton(widget)
btn.setText('按钮')
btn.clicked.connect(onClick_Button)

btn.move(24,50)

widget.resize(300,240) #设置工作区的尺寸（不包括标题栏高度）
widget.move(250,300)

widget.setWindowTitle('屏幕坐标系')

widget.show()

sys.exit(app.exec())