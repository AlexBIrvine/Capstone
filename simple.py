import sys
from PyQt6.QtWidgets import QApplication, QWidget

def main():
    """
    First simple GUI, used to test functionality
    """

    app = QApplication(sys.argv)

    window = QWidget()
    window.resize(250,200)
    window.move(300,300)

    window.setWindowTitle("Simple")
    window.show()

    sys.exit(app.exec())

if __name__ == '__main__': 
    main()

