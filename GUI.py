import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout

class Main_Window(QWidget):

    def __init__(self):
        super().__init__()

        # Sets the size to 80% of available screenspace
        self.resize(self.screen().availableGeometry().size().width()/1.2, self.screen().availableGeometry().size().height()/1.2)
        self.center()

        # Create buttons
        first_Button = QPushButton("First")
        second_Button = QPushButton("Second")
        third_Button = QPushButton("Third")
        fourth_Button = QPushButton("Fourth")
        fifth_Button = QPushButton("Fifth")
        sixth_Button = QPushButton("Sixth")
        seventh_Button = QPushButton("Seventh")

        # Create container to hold buttons and add buttons
        button_container = QHBoxLayout()
        button_container.addWidget(first_Button)
        button_container.addWidget(second_Button)
        button_container.addWidget(third_Button)
        button_container.addWidget(fourth_Button)
        button_container.addWidget(fifth_Button)
        button_container.addWidget(sixth_Button)
        button_container.addWidget(seventh_Button)

        # Create vertical container to place button container on bottom
        vertical_container = QVBoxLayout()
        vertical_container.addStretch(1)
        vertical_container.addLayout(button_container)


        # Adds widgets, title and shows GUI
        self.setLayout(vertical_container)
        self.setWindowTitle('Car Rental Predictor')
        self.show()




    def center(self):
        """
        Queries for center of screen and moves window to center
        """
        window_position = self.frameGeometry()
        center_of_screen = self.screen().availableGeometry().center()

        window_position.moveCenter(center_of_screen)
        self.move(window_position.topLeft())



def main():
    """
    Main GUI and starting point of the program
    """

    app = QApplication(sys.argv)
    window = Main_Window()
    sys.exit(app.exec())


if __name__ == '__main__': 
    main()

