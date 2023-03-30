from PyQt5.QtWidgets import QApplication, QDialog, QHBoxLayout, QVBoxLayout, QSpinBox, QLabel, QLineEdit
import sys
from PyQt5.QtGui import QIcon, QFont

class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200,400,400)
        self.setWindowTitle("PyQt5 Spinbox")
        self.setWindowIcon(QIcon("python.png"))
        self.create_spinbox()

    def create_spinbox(self):
        hbox = QHBoxLayout()
        label = QLabel("Laptop Price: ")

        self.lineEdit = QLineEdit()
        self.spinbox = QSpinBox()
        self.spinbox.valueChanged.connect(self.spin_selected)
        self.totalResult = QLineEdit()

        hbox.addWidget(label)
        hbox.addWidget(self.lineEdit)
        hbox.addWidget(self.spinbox)
        hbox.addWidget(self.totalResult)

        self.setLayout(hbox)

    def spin_selected(self):
        if self.lineEdit.text() != 0:
            price = int(self.lineEdit.text())
            totalPrice = self.spinbox.value() * price

            self.totalResult.setText(str(totalPrice))
        else: 
            print("Wrong Value")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())