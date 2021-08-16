from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import uic
import sys

class UI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Main.ui", self)


def main():
    app = QApplication(sys.argv)
    window = UI()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__': 
    main()

