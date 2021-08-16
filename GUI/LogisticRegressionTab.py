from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import *


class LogisticRegressionTab(QWidget):
    def __init__(self):
        super().__init__()

        # Fuel type controls
        fuel_type_label = QLabel("Fuel Type")
        fuel_type_list = QComboBox()
        fuel_type_list.addItem("Add more later")   # Pull list from csv file
        fuel_type_container = QVBoxLayout()
        fuel_type_container.addWidget(fuel_type_label)
        fuel_type_container.addWidget(fuel_type_list)
        fuel_type = QWidget()
        fuel_type.setLayout(fuel_type_container)

        # Trips Taken controls (Add input validation)
        trips_taken_label = QLabel("Trips Taken")
        trips_taken_input = QLineEdit()
        onlyInt = QIntValidator()
        trips_taken_input.setValidator(onlyInt)
        trips_taken_container = QVBoxLayout()
        trips_taken_container.addWidget(trips_taken_label)
        trips_taken_container.addWidget(trips_taken_input)
        trips_taken = QWidget()
        trips_taken.setLayout(trips_taken_container)

        # City controls (possible removal)
        city_label = QLabel("City")
        city_list = QComboBox()
        city_list.addItem("Add more later")   # Pull list from csv file
        city_container = QVBoxLayout()
        city_container.addWidget(city_label)
        city_container.addWidget(city_list)
        city = QWidget()
        city.setLayout(city_container)

        # Daily Rate controls (Add input validation)
        daily_rate_label = QLabel("Daily Rate")
        daily_rate_validator = QIntValidator(0, 500, self)
        daily_rate_input = QLineEdit()
        daily_rate_input.setValidator(daily_rate_validator)
        daily_rate_container = QVBoxLayout()
        daily_rate_container.addWidget(daily_rate_label)
        daily_rate_container.addWidget(daily_rate_input)
        daily_rate = QWidget()
        daily_rate.setLayout(daily_rate_container)

        # Make controls
        make_label = QLabel("Make")
        make_list = QComboBox()
        make_list.addItem("Add more later") # Pull list from csv file
        make_container = QVBoxLayout()
        make_container.addWidget(make_label)
        make_container.addWidget(make_list)
        make = QWidget()
        make.setLayout(make_container)

        # Type controls
        type_label = QLabel("Type")
        type_list = QComboBox()
        type_list.addItem("Add more later")   # Pull list from csv file
        type_container = QVBoxLayout()
        type_container.addWidget(type_label)
        type_container.addWidget(type_list)
        vehicle_type = QWidget()
        vehicle_type.setLayout(type_container)

        # Vehicle age controls
        age_label = QLabel("Vehicle Age")
        age_validator = QIntValidator(0, 10, self)
        age_input = QLineEdit()
        age_input.setValidator(age_validator)
        age_container = QVBoxLayout()
        age_container.addWidget(age_label)
        age_container.addWidget(age_input)
        age = QWidget()
        age.setLayout(age_container)

        # The main setup
        main_container = QVBoxLayout()
        main_container.addStretch(1)

        control_container = QHBoxLayout()
        control_container.addWidget(fuel_type)
        control_container.addWidget(trips_taken)
        control_container.addWidget(daily_rate)
        control_container.addWidget(make)
        control_container.addWidget(vehicle_type)
        control_container.addWidget(age)
        controls = QWidget()
        controls.setLayout(control_container)

        main_container.addWidget(controls)

        self.setLayout(main_container)


