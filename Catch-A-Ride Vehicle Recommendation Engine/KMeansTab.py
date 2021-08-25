from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIntValidator
from PyQt6.QtGui import QPixmap
from Logger import main_logger
import Models as mdl


class KMeansTab(QWidget):
    """
    Creates a Widget that holds the main content of the K-Means Tab for the main program. 
    """
    def __init__(self):
        super().__init__()

        # List to map human readable values to dataframe column names.  Used by submit_clicked function
        self.columns_list = ['fuelType_cat', 'rating', 'renterTripsTaken', 'vehicle.make_cat' , 'vehicle.type_cat', 'vehicle.age']

        # X-Axis controls
        x_axis_label = QLabel('X Axis')
        self.x_axis_list = QComboBox()
        self.x_axis_list.addItems(['Fuel Type', 'Rating', 'Trips Taken', 'Make', 'Vehicle Type', 'Vehicle Age'])
        x_axis_container = QVBoxLayout()
        x_axis_container.addWidget(x_axis_label)
        x_axis_container.addWidget(self.x_axis_list)
        x_axis  = QWidget()
        x_axis.setLayout(x_axis_container)
        self.x_axis_list.currentIndexChanged.connect(self.check_valid)

        # Y-Axis controls
        y_axis_label = QLabel("Y Axis")
        self.y_axis_list = QComboBox()
        self.y_axis_list.addItems(['Fuel Type', 'Rating', 'Trips Taken', 'Make', 'Vehicle Type', 'Vehicle Age'])
        y_axis_container = QVBoxLayout()
        y_axis_container.addWidget(y_axis_label)
        y_axis_container.addWidget(self.y_axis_list)
        y_axis  = QWidget()
        y_axis.setLayout(y_axis_container)
        self.y_axis_list.currentIndexChanged.connect(self.check_valid)

        # Cluster control
        cluster_label = QLabel("Cluster count")
        cluster_validator = QIntValidator(1, 10, self)
        self.cluster_input = QLineEdit()
        self.cluster_input.setValidator(cluster_validator)
        cluster_container = QVBoxLayout()
        cluster_container.addWidget(cluster_label)
        cluster_container.addWidget(self.cluster_input)
        cluster = QWidget()
        cluster.setLayout(cluster_container)
        self.cluster_input.textChanged.connect(self.check_valid)

        # Graph container
        self.graph_image = QLabel()
        graph_container = QHBoxLayout()
        graph_container.addStretch(1)
        graph_container.addWidget(self.graph_image)
        graph_container.addStretch(1)
        graph = QWidget()
        graph.setLayout(graph_container)

        # Controls container
        control_container = QHBoxLayout()
        control_container.addWidget(x_axis)
        control_container.addWidget(y_axis)
        control_container.addWidget(cluster)
        control_container.addStretch(1)
        self.submit_btn = QPushButton("Submit")
        self.submit_btn .setEnabled(False)
        self.submit_btn.clicked.connect(self.clicked_submit)
        control_container.addWidget(self.submit_btn)
        controls = QWidget()
        controls.setLayout(control_container)

        # Main Container
        main_container = QVBoxLayout()
        main_container.addWidget(graph)
        main_container.addStretch(1)
        main_container.addWidget(controls)
        self.setLayout(main_container)

    def clicked_submit(self):
        """
        Upon clicking the submit button, the program takes the values entered, runs the KMeans model with them, then creates/displays the resulting graph.
        """
        main_logger.info(f'{__name__} - Submit clicked\nCurrent selections X={self.x_axis_list.currentText()} Y={self.y_axis_list.currentText()} Clusters={self.cluster_input.text()}')
        
        # Get values from GUI
        x_axis = self.columns_list[self.x_axis_list.currentIndex()]   
        y_axis = self.columns_list[self.y_axis_list.currentIndex()]
        cluster= int(self.cluster_input.text())
        
        # Run the KMeans model
        mdl.getKMeansGraph(x_axis, y_axis, cluster)
        
        # Get graph and update GUI
        pic = QPixmap('output.png')
        self.graph_image.setPixmap(pic)


    def check_valid(self):
        """
        Checks if the x-axis and y-axis values are the same, and checks if cluster number is inputted.  
        If either are not true, then it will disable the submit button to reduce errors.  
        If both are true, the submit button will be enabled. 
        """
        if self.cluster_input.text() != "" and (self.x_axis_list.currentText() != self.y_axis_list.currentText()):
            self.submit_btn.setEnabled(True)
        else: 
            self.submit_btn.setEnabled(False)

