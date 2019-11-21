'''
mainlayout.addwidget(控件对象，行索引（就是位置），列索引（位置），占用行数（大小），占用列数（大小）)

伙伴关系：点击一个，另一个跟着反应（本例子中，热键ALt+N 或者ALt+p 能切换焦点）
'''

from PyQt5.QtWidgets import *
import sys


class QLabelBuddy(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('QLabel伙伴关系')

        namelabel=QLabel('&Name',self)
        nameLineEdit=QLineEdit(self)
#设置伙伴关系
        namelabel.setBuddy(nameLineEdit)

        passwordlabel = QLabel('&Password', self)
        passwordLineEdit = QLineEdit(self)

        passwordlabel.setBuddy(passwordLineEdit)

        btnok=QPushButton('&ok')
        btncancel=QPushButton('&Cancel')

        mainlayput=QGridLayout(self)
        mainlayput.addWidget(namelabel,0,0)
        mainlayput.addWidget(nameLineEdit,0,1,1,2)

        mainlayput.addWidget(passwordlabel,1,0)
        mainlayput.addWidget(passwordLineEdit,1,1,1,2)

        mainlayput.addWidget(btnok,2,1)
        mainlayput.addWidget(btncancel,2,2)

if __name__=='__main__':
    app =QApplication(sys.argv)
    main=QLabelBuddy()
    main.show()
    sys.exit(app.exec())