from PyQt5.QtCore import * # type: ignore
from PyQt5.QtWidgets import * # type: ignore
from PyQt5.QtGui import * # type: ignore

from instr import *
from final_win import *

class Experiment():
    def __init__(self, age, name, test1, test2, test3):
        self.age = age
        self.name = name
        self.t1 = test1
        self.t2 = test2
        self.t3 = test3

class TestWin(QWidget): # type: ignore
    def __init__(self):
        super().__init__()
        self.initUi()
        self.connects()
        self.set_appear()
        self.show()
    
    def initUi(self):
        self.btn_next = QPushButton(txt_sendresults, self) # type: ignore
        self.btn_test1 = QPushButton(txt_starttest1, self) # type: ignore
        self.btn_test2 = QPushButton(txt_starttest2, self) # type: ignore
        self.btn_test3 = QPushButton(txt_starttest3, self) # type: ignore

        self.text_name = QLabel(txt_name) # type: ignore
        self.text_age = QLabel(txt_age) # type: ignore
        self.text_test1 = QLabel(txt_test1) # type: ignore
        self.text_test2 = QLabel(txt_test2) # type: ignore
        self.text_test3 = QLabel(txt_test3) # type: ignore
        self.text_timer = QLabel(txt_timer) # type: ignore

        self.line_name = QLineEdit(txt_hintname) # type: ignore
        self.line_age = QLineEdit(txt_hintage) # type: ignore
        self.line_test1 = QLineEdit(txt_hinttest1) # type: ignore
        self.line_test2 = QLineEdit(txt_hinttest2) # type: ignore
        self.line_test3 = QLineEdit(txt_hinttest3) # type: ignore

        self.l_line = QVBoxLayout() # type: ignore
        self.r_line = QVBoxLayout() # type: ignore
        self.h_line = QHBoxLayout() # type: ignore
        self.r_line.addWidget(self.text_timer, alignment=Qt.AlignCenter) # type: ignore
        self.l_line.addWidget(self.text_name, alignment=Qt.AlignLeft) # type: ignore
        self.l_line.addWidget(self.line_name, alignment=Qt.AlignLeft) # type: ignore
        self.l_line.addWidget(self.text_age, alignment=Qt.AlignLeft) # type: ignore
        self.l_line.addWidget(self.line_age, alignment=Qt.AlignLeft) # type: ignore
        self.l_line.addWidget(self.text_test1, alignment=Qt.AlignLeft) # type: ignore
        self.l_line.addWidget(self.btn_test1, alignment=Qt.AlignLeft) # type: ignore
        self.l_line.addWidget(self.text_test2, alignment=Qt.AlignLeft) # type: ignore
        self.l_line.addWidget(self.btn_test2, alignment=Qt.AlignLeft) # type: ignore
        self.l_line.addWidget(self.text_test3, alignment=Qt.AlignLeft) # type: ignore
        self.l_line.addWidget(self.btn_test3, alignment=Qt.AlignLeft) # type: ignore
        self.l_line.addWidget(self.line_test2, alignment=Qt.AlignLeft) # type: ignore
        self.l_line.addWidget(self.line_test3, alignment=Qt.AlignLeft) # type: ignore

        self.l_line.addWidget(self.btn_next, alignment=Qt.AlignCenter) # type: ignore

        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setStyleSheet("color: red; font-size: 20px;")
        self.text_timer.setFont(QFont("Arial", 20, QFont.Bold)) # type: ignore
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setStyleSheet("color: orange; font-size: 20px;")
        self.text_timer.setFont(QFont("Arial", 20, QFont.Bold)) # type: ignore
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setStyleSheet("color: green; font-size: 20px;")
        self.text_timer.setFont(QFont("Arial", 20, QFont.Bold)) # type: ignore
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.text_timer.setStyleSheet("color: red; font-size: 20px;")
        elif int(time.toString("hh:mm:ss")[6:8]) >= 30:
            self.text_timer.setStyleSheet("color: orange; font-size: 20px;")
        else:
            self.text_timer.setStyleSheet("color: green; font-size: 20px;")
        self.text_timer.setFont(QFont("Arial", 20, QFont.Bold)) # type: ignore
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer_test(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer() # type: ignore
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer_squats(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer() # type: ignore
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)

    def timer_final(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer() # type: ignore
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)

    def next_click(self):
        self.hide()
        self.exp = Experiment(self.line_age.text(), self.line_name.text(), self.line_test1.text(), self.line_test2.text(), self.line_test3.text())
        self.tw = FinalWin(self.exp)
        self.tw.show()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
        self.btn_test1.clicked.connect(self.timer_test)
        self.btn_test2.clicked.connect(self.timer_squats)
        self.btn_test3.clicked.connect(self.timer_final)
    
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
