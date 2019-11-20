'''
QLabel控件
setAlignment():设置文本对齐方式
setIndent():设置文本缩进
text（）：获取文本内容
setBuddy():设置伙伴关系
setText():设置文本内容
selectedText(）：返回所选择的字符
setWordWrap():设置是否允许换行

常用信号（事件）：
1.当鼠标滑过控件时触发：LinkHovered
2.当鼠标单击控件触发：linkActivateed
'''

import sys
from PyQt5.QtWidgets import QVBoxLayout,QMainWindow,QApplication,QLabel,QWidget
from PyQt5.QtGui import QPalette,QPixmap
from PyQt5.QtCore import Qt

class QLabeldemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()             #initUI()初始化函数这么调用，而不是self.initUI，切记要加括号

    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("<font color=yellow>这是一个本文标签.</font>")
        label1.setAutoFillBackground(True)
        patette=QPalette()
        patette.setColor(QPalette.Window,Qt.blue)
        label1.setPalette(patette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>欢迎使用python</a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('这是个图片标签')
        label3.setPixmap(QPixmap('./images/01.jpg'))

        label4.setToolTip('这个是超链接')

        label4.setOpenExternalLinks(True)
        label4.setText("<a href='https://123.sogou.com/'>感谢关注</a>")
        label4.setAlignment(Qt.AlignRight)
        vbox=QVBoxLayout()

        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        label2.linkHovered.connect(self.linkhovered)

        label4.linkActivated.connect(self.linkclick)

        self.setLayout(vbox)
        self.setWindowTitle('label控件演示')


    def linkhovered(self):
        print("label2当鼠标滑过触发")

    def linkclick(self):
        print('label4鼠标单击触发')

if __name__=='__main__':
    app =QApplication(sys.argv)
    main=QLabeldemo()
    main.show()
    sys.exit(app.exec())