import logging
from PyQt6.QtWidgets import *
from Logger import main_logger

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

        # Button signal binding
        fuel_type_btn.clicked.connect(self.clicked_fuel_type)
        trips_taken_btn.clicked.connect(self.clicked_trips_taken)
        daily_rate_btn.clicked.connect(self.clicked_daily_rate)
        make_btn.clicked.connect(self.clicked_make)
        type_btn.clicked.connect(self.clicked_type)
        age_btn.clicked.connect(self.clicked_age)

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

    def clicked_fuel_type(self):
        main_logger.info(f'{__name__} - fuel type button clicked')

    def clicked_trips_taken(self):
        main_logger.info(f'{__name__} - trips taken button clicked')

    def clicked_daily_rate(self):
        main_logger.info(f'{__name__} - daily rate button clicked')

    def clicked_make(self):
        main_logger.info(f'{__name__} - make button clicked')
    
    def clicked_type(self):
        main_logger.info(f'{__name__} - type button clicked')

    def clicked_age(self):
        main_logger.info(f'{__name__} - age button clicked')