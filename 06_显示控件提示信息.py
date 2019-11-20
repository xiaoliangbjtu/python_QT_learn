import sys
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QPushButton,QWidget,QToolTip
from PyQt5.QtGui import QFont

class tooltipform(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif',12))
        self.setToolTip('今天是<b>星期五</b>')
        self.setGeometry(300,300,300,300)
        self.setWindowTitle('设置提示信息')

        self.button1=QPushButton('按钮')
        self.button1.setToolTip('<b>this is a button</b>')  #<b>  </b>作用为加粗字体
        layout=QHBoxLayout()
        layout.addWidget(self.button1)

        mainform=QWidget()
        mainform.setLayout(layout)
        self.setCentralWidget(mainform)

if __name__=='__main__':
    app =QApplication(sys.argv)

    main=tooltipform()
    main.show()
    sys.exit(app.exec())