import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

# app = QApplication(sys.argv) # 모듈을 가저온다
# label = QLabel("케이") # 모듈을 가져온다.
# label.show()
# app.exec_() # 이벤트 루프 실행

form_class = uic.loadUiType("mywindow.ui")[0]


class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #self.setGeometry(100, 200, 600, 400)
        #self.setWindowTitle("Kei CoCoIn")
        #self.setWindowIcon(QIcon("icon.jpg"))

    def btn_clicked(self):
        print("버튼 클릭")


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
