from PyQt5.QtWidgets import QApplication, QDialog, QHBoxLayout, QVBoxLayout, QSpinBox, QLabel, QLineEdit
import sys
from PyQt5.QtGui import QIcon, QFont

class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200,400,400)

        self.setWindowTitle("PyQt5 Template")
        self.setWindowIcon(QIcon("python.png"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())