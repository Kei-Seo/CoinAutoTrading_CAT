import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# QTime 사용을 위해
from PyQt5.QtCore import *
from PyQt5 import uic
# 비트코인의 데이터를 가져오기 위해서
import pykorbit


# app = QApplication(sys.argv) # 모듈을 가저온다
# label = QLabel("케이") # 모듈을 가져온다.
# label.show()
# app.exec_() # 이벤트 루프 실행

form_class = uic.loadUiType("mywindow.ui")[0]


class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.inquiry_clicked)
        self.setWindowTitle("Kei CoCoIn")
        self.setWindowIcon(QIcon("icon.jpg"))

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.timeout)

    def inquiry_clicked(self):
        price = pykorbit.get_current_price("BTC")
        self.lineEdit.setText(str(price))

    def timeout(self):
        cur_time = QTime.currentTime()
        str_time = cur_time.toString("hh:mm:ss")
        self.statusBar().showMessage(str_time)






app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
