from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import *
from Logger import main_logger
from CSV_tools import get_catelogical_dict, data_prep
from LogisticRegressionModel import getLogisticRegression

class LogisticRegressionTab(QWidget):
    def __init__(self):
        super().__init__()
        data_prep()
        self.categorical_values = get_catelogical_dict()

        # Fuel type controls
        fuel_type_label = QLabel("Fuel Type")
        self.fuel_type_list = QComboBox()
        self.load_fuelType_values()
        fuel_type_container = QVBoxLayout()
        fuel_type_container.addWidget(fuel_type_label)
        fuel_type_container.addWidget(self.fuel_type_list)
        fuel_type = QWidget()
        fuel_type.setLayout(fuel_type_container)
        self.fuel_type_list.currentIndexChanged.connect(self.clicked_fuel_type)

        # Make controls
        make_label = QLabel("Make")
        self.make_list = QComboBox()
        self.make_list.addItem("")
        self.load_make_values()
        make_container = QVBoxLayout()
        make_container.addWidget(make_label)
        make_container.addWidget(self.make_list)
        make = QWidget()
        make.setLayout(make_container)
        self.make_list.currentIndexChanged.connect(self.clicked_make)

        # Model controls
        model_label = QLabel("Model")
        self.model_list = QComboBox()
        model_container = QVBoxLayout()
        model_container.addWidget(model_label)
        model_container.addWidget(self.model_list)
        model = QWidget()
        model.setLayout(model_container)
        self.model_list.currentIndexChanged.connect(self.clicked_model)

        # Type controls
        type_label = QLabel("Type")
        self.type_list = QComboBox()
        self.load_vehicleType_values()
        type_container = QVBoxLayout()
        type_container.addWidget(type_label)
        type_container.addWidget(self.type_list)
        vehicle_type = QWidget()
        vehicle_type.setLayout(type_container)
        self.type_list.currentIndexChanged.connect(self.clicked_type)

        # Vehicle age controls
        age_label = QLabel("Vehicle Age")
        age_validator = QIntValidator(0, 10, self)
        self.age_input = QLineEdit()
        self.age_input.setValidator(age_validator)
        age_container = QVBoxLayout()
        age_container.addWidget(age_label)
        age_container.addWidget(self.age_input)
        age = QWidget()
        age.setLayout(age_container)
        self.age_input.textChanged.connect(self.clicked_age)

        # The main setup
        main_container = QVBoxLayout()
        main_container.addStretch(1)

        control_container = QHBoxLayout()
        control_container.addWidget(make)
        control_container.addWidget(model)
        control_container.addWidget(vehicle_type)
        control_container.addWidget(fuel_type)
        control_container.addWidget(age)
        control_container.addStretch(1)

        reset_btn = QPushButton("Reset")
        submit_btn = QPushButton("Submit")
        reset_btn.clicked.connect(self.clicked_reset)
        submit_btn.clicked.connect(self.clicked_submit)
        control_container.addWidget(reset_btn)
        control_container.addWidget(submit_btn)

        controls = QWidget()
        controls.setLayout(control_container)

        main_container.addWidget(controls)
        self.setLayout(main_container)

    def clicked_fuel_type(self):
        main_logger.info(f'{__name__} - Fuel type field changed to {self.fuel_type_list.currentText()}')

    def clicked_make(self):
        main_logger.info(f'{__name__} - Make field changed to {self.make_list.currentText()}')
        self.load_model_values(str(self.make_list.currentText()))
        self.load_fuelType_values()
        self.load_vehicleType_values()

    def clicked_model(self):
        main_logger.info(f'{__name__} - Model field changed to {self.model_list.currentText() or "nothing"}')
        if len(self.model_list.currentText()) > 0:
            self.load_fuelType_values(str(self.model_list.currentText()))
            self.load_vehicleType_values(str(self.model_list.currentText()))

    def clicked_type(self):
        main_logger.info(f'{__name__} - Type field changed to {self.type_list.currentText()}')

    def clicked_age(self):
        main_logger.info(f'{__name__} - Age field changed to {self.age_input.text()}')

    def clicked_reset(self):
        main_logger.info(f'{__name__} - Reset clicked')
        self.make_list.setCurrentIndex(0)
        self.load_model_values()
        self.load_vehicleType_values()
        self.load_fuelType_values()
        self.age_input.clear()

    def clicked_submit(self):
        main_logger.info(f'{__name__} - Submit clicked')
        fields = []
        values = []

        if self.make_list.currentText() != "":
            make_keys = list(self.categorical_values['vehicle_makes'].keys())
            make_values = list(self.categorical_values['vehicle_makes'].values())
            make_index = str(make_values.index(self.make_list.currentText()))
            values.append(int(make_keys.index(make_index)))
            fields.append('vehicle.make_cat')

        if self.model_list.currentText() != "":
            model_keys = list(self.categorical_values['vehicle_models'].keys())
            model_values = list(self.categorical_values['vehicle_models'].values())
            model_index = str(model_values.index(self.model_list.currentText()))
            values.append(int(model_keys.index(model_index)))
            fields.append('vehicle.model_cat')

        if self.type_list.currentText() != "":
            vType_keys = list(self.categorical_values['vehicle_types'].keys())
            vType_values = list(self.categorical_values['vehicle_types'].values())
            vType_index = str(vType_values.index(self.type_list.currentText()))
            values.append(int(vType_keys.index(vType_index)))
            fields.append('vehicle.type_cat')

        if self.fuel_type_list.currentText() != "":
            fType_keys = list(self.categorical_values['fuel_types'].keys())
            fType_values = list(self.categorical_values['fuel_types'].values())
            fType_index = str(fType_values.index(self.fuel_type_list.currentText()))
            values.append(int(fType_keys.index(fType_index)))
            fields.append('fuelType_cat')

        if self.age_input.text() != "":
            values.append(int(self.age_input.text()))
            fields.append('vehicle.age')

        if (len(fields) > 0):
            getLogisticRegression(fields, values)

    def load_fuelType_values(self, model = None):
        if model == None:
            self.fuel_type_list.clear()
            self.fuel_type_list.addItem("")
            self.fuel_type_list.addItems(sorted(list(self.categorical_values['fuel_types'].values())))
        else: 
            model_keys = list(self.categorical_values['vehicle_models'].keys())
            model_values = list(self.categorical_values['vehicle_models'].values())
            index = model_values.index(model)

            model_key = model_keys[index]
            model_to_fType = self.categorical_values['model_to_fType']
            fType_key = str(model_to_fType[model_key])
            fType = self.categorical_values['fuel_types'][fType_key]

            self.fuel_type_list.clear()
            self.fuel_type_list.addItem(fType)


    def load_make_values(self):
        self.make_list.addItems(sorted(list(self.categorical_values['vehicle_makes'].values())))


    def load_model_values(self, make = None):
        if make == None or make == "":
            self.model_list.clear()
        else: 
            make_keys = list(self.categorical_values['vehicle_makes'].keys())
            make_values = list(self.categorical_values['vehicle_makes'].values())
            index = make_values.index(make)
            
            make_key = int(make_keys[index])
            model_keys = []
            models = self.categorical_values['vehicle_models']
            model_to_make = self.categorical_values['model_to_make']
            return_models = []

            for key, value in model_to_make.items():
                if value == make_key:
                    model_keys.append(key)

            for model in model_keys:
                return_models.append(models[model])

            self.model_list.clear()
            self.model_list.addItem("")
            self.model_list.addItems(sorted(return_models))



    def load_vehicleType_values(self, model = None):
        if model == None:
            self.type_list.clear()
            self.type_list.addItem("")
            self.type_list.addItems(sorted(list(self.categorical_values['vehicle_types'].values())))
        else: 
            model_keys = list(self.categorical_values['vehicle_models'].keys())
            model_values = list(self.categorical_values['vehicle_models'].values())
            index = model_values.index(model)
            model_key = model_keys[index]

            model_to_vType = self.categorical_values['model_to_vType']
            vType_key = str(model_to_vType[model_key])
            vType = self.categorical_values['vehicle_types'][vType_key]

            self.type_list.clear()
            self.type_list.addItem(vType)