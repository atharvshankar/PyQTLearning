from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget, QMainWindow, QPushButton, QGroupBox, QHBoxLayout, QVBoxLayout, QRadioButton,QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize
import sys


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle("Atharv PyQT5")
        self.setWindowIcon(QIcon("python.png"))
        # self.create_buttons()
        self.create_radiobutton()
        # self.initUI()
        self.label = QLabel("")
        self.label.setFont(QFont('sanserif',14))
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupbox)
        vbox.addWidget(self.label)
        self.setLayout(vbox)

    # def initUI(self):
        # self.label = QtWidgets.QLabel(self)
        # self.label.setText("Hi Abhi") 
        # self.label.move(50,50)

        # self.b1 = QtWidgets.QPushButton(self)
        # self.b1.setText("Click me")
        # self.b1.clicked.connect(self.clicked)

    # def create_buttons(self):
    #     btn1 = QPushButton("Hello I am a button",self)
    #     btn1.adjustSize()
    #     btn1.setText("Button one")
    #     btn1.setGeometry(100,100,100,100)
    #     btn1.setIcon(QIcon("python.png"))
    #     btn1.setStyleSheet('color:red')
    #     btn1.clicked.connect(self.clicked_btn)

    #     btn2 = QPushButton(self)
    #     btn2.setText("Button 2")
    #     btn2.adjustSize()
    #     btn2.setGeometry(200,100,100,100)
    #     btn2.setIcon(QIcon("python.png"))
    #     btn2.setStyleSheet("color: red;"
    #                     "background-color: white;")

    def clicked(self):
        self.label.setText("You pressed the button")
        self.update()
    
    def clicked_btn(self):
        print("YO")

    def update(self):
        self.label.adjustSize()
    
    def create_radiobutton(self):
        self.groupbox = QGroupBox("What is your favourite ice cream?")
        self.groupbox.setFont(QFont("sanserif",15))

        hbox = QHBoxLayout()
        self.rad1 = QRadioButton("Butterscotch")
        self.rad1.setChecked(True)
        self.rad1.setIcon(QIcon('python.png'))
        self.rad1.setIconSize(QSize(40,40))
        self.rad1.setFont(QFont('sanserif',14))
        self.rad1.toggled.connect(self.on_selected)
        hbox.addWidget(self.rad1)

        self.rad2 = QRadioButton("Chocolate")
        self.rad2.toggled.connect(self.on_selected)
        hbox.addWidget(self.rad2)

        self.rad3 = QRadioButton("Vanilla")
        self.rad3.toggled.connect(self.on_selected)
        hbox.addWidget(self.rad3)

        self.groupbox.setLayout(hbox)

    def on_selected(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            self.label.setText("You have selected: " + radio_button.text())

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    window()