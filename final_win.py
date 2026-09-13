from PyQt5.QtCore import * # type: ignore
from PyQt5.QtWidgets import * # type: ignore
from instr import *

class FinalWin(QWidget): # type: ignore
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.initUi()
        self.set_appear()
        self.show()

    def result(self):
        age = int(self.exp.age)
        if age < 7:
            self.index = 0
            return "Tidak ada data untuk umur ini"
        self.index = (4 * (int(self.exp.t1) + int(self.exp.t2) + int(self.exp.t3)) - 200) / 10
        if age == 7 or age == 8:
            if self.index >= 21:
                return txt_res1
            elif self.index < 21 and self.index >= 17:
                return txt_res2
            elif self.index < 17 and self.index >= 12:
                return txt_res3
            elif self.index < 12 and self.index >= 6.5:
                return txt_res4
            else:
                return txt_res5
        elif age == 9 or age == 10:
            if self.index >= 19.5:
                return txt_res1
            elif self.index < 19.5 and self.index >= 15.5:
                return txt_res2
            elif self.index < 15.5 and self.index >= 10.5:
                return txt_res3
            elif self.index < 10.5 and self.index >= 5:
                return txt_res4
            else:
                return txt_res5
        elif age == 11 or age == 12:
            if self.index >= 18:
                return txt_res1
            elif self.index < 18 and self.index >= 14:
                return txt_res2
            elif self.index < 14 and self.index >= 9:
                return txt_res3
            elif self.index < 9 and self.index >= 3.5:
                return txt_res4
            else:
                return txt_res5
        elif age == 13 or age == 14:
            if self.index >= 16.5:
                return txt_res1
            elif self.index < 16.5 and self.index >= 12.5:
                return txt_res2
            elif self.index < 12.5 and self.index >= 7.5:
                return txt_res3
            elif self.index < 7.5 and self.index >= 2:
                return txt_res4
            else:
                return txt_res5
        elif age >= 15:
            if self.index >= 15:
                return txt_res1
            elif self.index < 15 and self.index >= 11:
                return txt_res2
            elif self.index < 11 and self.index >= 6:
                return txt_res3
            elif self.index < 6 and self.index >= 0.5:
                return txt_res4
            else:
                return txt_res5

    def initUi(self):
        self.name_text = QLabel(txt_name + self.exp.name) # type: ignore
        self.workh_text = QLabel(txt_workheart + self.result()) # type: ignore
        self.index_text = QLabel(txt_index + str(self.index)) # type: ignore

        self.layout_line = QVBoxLayout() # type: ignore
        self.layout_line.addWidget(self.name_text, alignment=Qt.AlignCenter) # type: ignore
        self.layout_line.addWidget(self.workh_text, alignment=Qt.AlignCenter) # type: ignore
        self.layout_line.addWidget(self.index_text, alignment=Qt.AlignCenter) # type: ignore
        self.setLayout(self.layout_line)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)