from PyQt6.QtWidgets import *

class KMeansTab(QWidget):
    def __init__(self):
        super().__init__()

        # Create buttons
        fuel_type_btn = QPushButton("Fuel type")
        trips_taken_btn = QPushButton("Trips taken")
        daily_rate_btn = QPushButton("Daily Rate")
        make_btn = QPushButton("Make")
        type_btn = QPushButton("Type")
        age_btn = QPushButton("Age")

        # Button layout
        buttons = QWidget()
        button_container = QHBoxLayout()
        button_container.addWidget(fuel_type_btn)
        button_container.addWidget(trips_taken_btn)
        button_container.addWidget(daily_rate_btn)
        button_container.addWidget(make_btn)
        button_container.addWidget(type_btn)
        button_container.addWidget(age_btn)
        buttons.setLayout(button_container)

        # Main layout
        main_container = QVBoxLayout()
        main_container.addStretch(1)
        main_container.addWidget(buttons)
        self.setLayout(main_container)
