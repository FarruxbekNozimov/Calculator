from PyQt5.QtWidgets import QPushButton, QMessageBox, QWidget, QLabel
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtWidgets
import random as r
import math
import sys
class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.start()
        self.all()

    class HyperlinkLabel(QLabel):
        def __init__(self, parent=None):
            super().__init__()
            self.setStyleSheet('font-size: 35px')
            self.setOpenExternalLinks(True)
            self.setParent(parent)

    def style1(self, obj, color, border):
        obj.setStyleSheet(f"padding-bottom: 2px;background-color: {color};border-radius: {border}px;font: bold 18px ;border: 1px solid black;")

    def start(self):
        self.setFixedSize(374, 450)
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon('2.png'))
        self.setStyleSheet("background-color: #333;")

        # MAKE BUTTON
        self.label = QLin(self)
        self.Btn_1 = QPushButton(self)
        self.Btn_2 = QPushButton(self)
        self.Btn_3 = QPushButton(self)
        self.Btn_4 = QPushButton(self)
        self.Btn_5 = QPushButton(self)
        self.Btn_6 = QPushButton(self)
        self.Btn_7 = QPushButton(self)
        self.Btn_8 = QPushButton(self)
        self.Btn_9 = QPushButton(self)
        self.Btn_0 = QPushButton(self)
        self.Btn_C = QPushButton(self)
        self.Btn_PM = QPushButton(self)
        self.Btn_Dot = QPushButton(self)
        self.Btn_Plus = QPushButton(self)
        self.Btn_Qoch = QPushButton(self)
        self.Btn_Back = QPushButton(self)
        self.Btn_Fact = QPushButton(self)
        self.Btn_Teng = QPushButton(self)
        self.Btn_Qyop = QPushButton(self)
        self.Btn_Ildiz = QPushButton(self)
        self.Btn_Minus = QPushButton(self)
        self.Btn_Grade = QPushButton(self)
        self.Btn_Kopay = QPushButton(self)
        self.Btn_Color = QPushButton(self)
        self.Btn_Bolish = QPushButton(self)
        self.Btn_Question = QPushButton(self)

        # SET GEOMETRY
        self.label.setGeometry(15, 20, 345, 100)
        self.Btn_1.setGeometry(20, 310, 51, 27)
        self.Btn_2.setGeometry(90, 310, 51, 27)
        self.Btn_3.setGeometry(160, 310, 51, 27)
        self.Btn_4.setGeometry(20, 260, 51, 27)
        self.Btn_5.setGeometry(90, 260, 51, 27)
        self.Btn_6.setGeometry(160, 260, 51, 27)
        self.Btn_7.setGeometry(20, 210, 51, 27)
        self.Btn_8.setGeometry(90, 210, 51, 27)
        self.Btn_9.setGeometry(160, 210, 51, 27)
        self.Btn_0.setGeometry(20, 360, 51, 27)
        self.Btn_C.setGeometry(20, 160, 51, 27)
        self.Btn_PM.setGeometry(300, 210, 51, 27)
        self.Btn_Dot.setGeometry(230, 160, 51, 27)
        self.Btn_Plus.setGeometry(230, 360, 51, 27)
        self.Btn_Qyop.setGeometry(160, 160, 51, 27)
        self.Btn_Qoch.setGeometry(90, 160, 51, 27)
        self.Btn_Back.setGeometry(300, 160, 51, 27)
        self.Btn_Fact.setGeometry(300, 360, 51, 27)
        self.Btn_Teng.setGeometry(90, 360, 121, 27)
        self.Btn_Kopay.setGeometry(230, 260, 51, 27)
        self.Btn_Minus.setGeometry(230, 310, 51, 27)
        self.Btn_Grade.setGeometry(300, 260, 51, 27)
        self.Btn_Ildiz.setGeometry(300, 310, 51, 27)
        self.Btn_Bolish.setGeometry(230, 210, 51, 27)
        self.Btn_Color.setGeometry(20, 405, 260, 27)
        self.Btn_Question.setGeometry(300, 405, 51, 27)

        # SET STYLE
        self.style1(self.Btn_1, '#7177f0', '10')
        self.style1(self.Btn_2, '#7177f0', '10')
        self.style1(self.Btn_3, '#7177f0', '10')
        self.style1(self.Btn_4, '#7177f0', '10')
        self.style1(self.Btn_5, '#7177f0', '10')
        self.style1(self.Btn_6, '#7177f0', '10')
        self.style1(self.Btn_7, '#7177f0', '10')
        self.style1(self.Btn_8, '#7177f0', '10')
        self.style1(self.Btn_9, '#7177f0', '10')
        self.style1(self.Btn_0, '#7177f0', '10')
        self.style1(self.Btn_PM, '#3eb542', '13')
        self.style1(self.Btn_Dot, '#3eb542', '13')
        self.style1(self.Btn_Teng, '#3eb542', '13')
        self.style1(self.Btn_Fact, '#3eb542', '13')
        self.style1(self.Btn_Qyop, '#3eb542', '13')
        self.style1(self.Btn_Plus, '#3eb542', '13')
        self.style1(self.Btn_Qoch, '#3eb542', '13')
        self.style1(self.Btn_Kopay, '#3eb542', '13')
        self.style1(self.Btn_Minus, '#3eb542', '13')
        self.style1(self.Btn_Ildiz, '#3eb542', '13')
        self.style1(self.Btn_Grade, '#3eb542', '13')
        self.style1(self.Btn_Color, '#999', '13')
        self.style1(self.Btn_Bolish, '#3eb542', '13')
        self.style1(self.Btn_C, 'red', '13')
        self.style1(self.Btn_Back, 'red', '13')
        self.style1(self.Btn_Question, 'blue', '13')
        self.label.setStyleSheet("background:#fff;border-radius: 12px;font: 40px Agency FB;border: 2px dashed black;")



    def all(self):
        # RENAME BUTTONS AND SHORTCUTS
        self.colors = ['blue', 'brown', 'aqua', 'yellow', 'purple', 'red', 'orange']
        self.btns = { '1': self.Btn_1, '2': self.Btn_2, '3': self.Btn_3, '4': self.Btn_4, '5': self.Btn_5, '6': self.Btn_6, 'x': self.Btn_Kopay, '8': self.Btn_8, '7': self.Btn_7, '.': self.Btn_Dot, '9': self.Btn_9, '-': self.Btn_Minus, '/': self.Btn_Bolish, '0': self.Btn_0, '√': self.Btn_Ildiz, 'C': self.Btn_C, ')': self.Btn_Qyop, '+/-': self.Btn_PM, '+': self.Btn_Plus, '(': self.Btn_Qoch, '<--': self.Btn_Back, 'X!': self.Btn_Fact, '^': self.Btn_Grade, '=': self.Btn_Teng, 'CHANGE COLOR': self.Btn_Color, '?':self.Btn_Question}
        self.shortcuts = ['1', '2', '3', '4', '5', '6', '*', '8', '7', '.', '9', '-', '/', '0', 'Ctrl+1', 'Ctrl+Backspace', ')', 'Ctrl+-', '+', '(', 'Backspace', '!', '^', 'Return', 'Space', '?']
        for i, val in enumerate(self.btns):
            self.btns[val].setText(f"{val}")
            self.btns[val].setShortcut(f"{self.shortcuts[i]}")
        self.text_label = ""
        self.last = 'lime'
        # =============================================
        # OTHER FUNCTIONS

        # MAIN FUNCTION
        def main_fun(a):
            try:
                chars = self.text_label.replace('+', ' ').replace('-', ' ').replace('/', ' ').replace('x', ' ').replace('^', ' ').split(' ')
                if len(self.text_label) < 20:
                    if a == '(' and self.text_label == '':
                        self.text_label = self.text_label[:] + a[:]
                        self.label.setText(self.text_label)
                    elif a == ')' and '(' not in self.text_label:
                        alert_msg()
                    elif self.text_label == '' and not a.isdigit():
                        alert_msg()
                    elif a == '(' and (self.text_label[-1].isdigit() or self.text_label[-1] == '.'):
                        alert_msg()
                    elif a != '(' and not a.isdigit() and not self.text_label[-1].isdigit() and self.text_label[-1] != ')':
                        alert_msg()
                    else:
                        # for i in chars:
                        #     if i.count('.') <= 1:
                        self.text_label = self.text_label[:] + a[:]
                        self.label.setText(self.text_label)
                            # else:
                            #     alert_msg()
            except:
                alert_msg()

        # ERROR MSG
        def alert_msg():
            msg = QMessageBox()
            msg.setText("KALLANGIZGA QOIL !!!")
            msg.setWindowTitle("XATOLIK !!!")
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()

        # SHOW RESULT
        def result():
            try:
                if self.text_label[-1] not in '1234567890' and self.text_label[-1] != ')':
                   alert_msg()
                else:
                    self.text_label = self.text_label.replace('x', '*')
                    self.text_label = self.text_label.replace('^', '**')
                    self.text_label = str(eval(self.text_label))
                    self.text_label = self.text_label[:17]
                    for i in self.text_label:
                        if self.text_label[-1] == '0':
                            print(self.text_label)
                            self.text_label = self.text_label[:-1]
                    self.label.setText(self.text_label)
            except:
                alert_msg()

        # +/- CHARACTER
        def plus_minus():
            try:
                if self.text_label[0] != '-':
                    self.text_label = '-' + self.text_label[:]
                    self.label.setText(self.text_label)
                else:
                    self.text_label = self.text_label[1:]
                    self.label.setText(self.text_label)
            except:
                alert_msg()

        # CLEAR THE SHIT OF LABEL
        def clear():
            if self.text_label == '0/':
                self.setStyleSheet('background-color: #333')
                self.style1(self.Btn_Color, '#999', '13')
            self.text_label = ""
            self.label.setText(self.text_label)

        # FIND FACTORIAL OF NUMBER
        def facto():
            try:
                self.text_label = str(math.factorial(int(self.text_label)))
                self.label.setText(self.text_label)
            except:
                alert_msg()

        # FIND SQRT OF NUMBER
        def sqrt1():
            try:
                self.text_label = str(math.sqrt(float(self.text_label)))
                self.label.setText(self.text_label)
            except:
                alert_msg()

        # ONE STEP BACK
        def back():
            self.text_label = self.text_label[:-1]
            self.label.setText(self.text_label)

        # FOR CHANGE COLOR
        def change_color():
            a = r.choice(self.colors)
            while a == self.last:
                a = r.choice(self.colors)
            if a != self.last:
                print(a, self.last)
                self.setStyleSheet(f'background-color:{a}')
                self.style1(self.Btn_Color, self.last, '13')
            self.last = a

        def questions():
            msg = QMessageBox()
            msg.setText("""<h1><a href='https://t.me/Farruxbek_blog'>Murojaat va takliflar uchun...</a></h1>""")
            msg.setWindowTitle("Questions !!!")
            msg.setIcon(QMessageBox.Question)
            x = msg.exec_()

        self.Btn_1.clicked.connect(lambda: main_fun(self.Btn_1.text()))
        self.Btn_2.clicked.connect(lambda: main_fun(self.Btn_2.text()))
        self.Btn_3.clicked.connect(lambda: main_fun(self.Btn_3.text()))
        self.Btn_4.clicked.connect(lambda: main_fun(self.Btn_4.text()))
        self.Btn_5.clicked.connect(lambda: main_fun(self.Btn_5.text()))
        self.Btn_6.clicked.connect(lambda: main_fun(self.Btn_6.text()))
        self.Btn_Kopay.clicked.connect(lambda: main_fun(self.Btn_Kopay.text()))
        self.Btn_8.clicked.connect(lambda: main_fun(self.Btn_8.text()))
        self.Btn_7.clicked.connect(lambda: main_fun(self.Btn_7.text()))
        self.Btn_Dot.clicked.connect(lambda: main_fun(self.Btn_Dot.text()))
        self.Btn_9.clicked.connect(lambda: main_fun(self.Btn_9.text()))
        self.Btn_Minus.clicked.connect(lambda: main_fun(self.Btn_Minus.text()))
        self.Btn_Bolish.clicked.connect(lambda: main_fun(self.Btn_Bolish.text()))
        self.Btn_0.clicked.connect(lambda: main_fun(self.Btn_0.text()))
        self.Btn_Qyop.clicked.connect(lambda: main_fun(self.Btn_Qyop.text()))
        self.Btn_Plus.clicked.connect(lambda: main_fun(self.Btn_Plus.text()))
        self.Btn_Qoch.clicked.connect(lambda: main_fun(self.Btn_Qoch.text()))
        self.Btn_Grade.clicked.connect(lambda: main_fun(self.Btn_Grade.text()))

        self.Btn_C.clicked.connect(clear)
        self.Btn_PM.clicked.connect(plus_minus)
        self.Btn_Ildiz.clicked.connect(sqrt1)
        self.Btn_Back.clicked.connect(back)
        self.Btn_Fact.clicked.connect(facto)
        self.Btn_Teng.clicked.connect(result)
        self.Btn_Color.clicked.connect(change_color)
        self.Btn_Question.clicked.connect(questions)

app = QtWidgets.QApplication(sys.argv)
windows = Calculator()
windows.show()
sys.exit(app.exec_())