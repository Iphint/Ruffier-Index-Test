from PyQt5.QtCore import * # type: ignore
from PyQt5.QtWidgets import * # type: ignore

from instr import *
from second_win import *

app = QApplication([]) # type: ignore

class MainWin(QWidget): # type: ignore
    def __init__(self):
        super().__init__()
        self.initUi()
        self.connects()
        self.set_appear()
        self.show()

    def initUi(self):
        self.btn_next = QPushButton(txt_next, self) # type: ignore
        self.hello_txt = QLabel(txt_hello) # type: ignore
        self.instruction = QLabel(txt_instruction) # type: ignore
        self.layout_line = QVBoxLayout() # type: ignore
        self.layout_line.addWidget(self.hello_txt, alignment=Qt.AlignCenter) # type: ignore
        self.layout_line.addWidget(self.instruction, alignment=Qt.AlignCenter) # type: ignore
        self.layout_line.addWidget(self.btn_next, alignment=Qt.AlignCenter) # type: ignore
        self.setLayout(self.layout_line)

    def next_click(self):
        self.hide()
        self.tw = TestWin() 
        self.tw.show()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
    
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

mw = MainWin()
app.exec_()