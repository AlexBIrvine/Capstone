import sys
import os.path
import DataPreperation
from Logger import main_logger, send_log_email
from KMeansTab import KMeansTab  
from LogisticRegressionTab import LogisticRegressionTab
from PyQt6.QtWidgets import QApplication, QTabWidget, QWidget, QVBoxLayout


class Main_Window(QWidget):

    def __init__(self):
        super().__init__()

        # Sets the size to 50% of available screenspace & centers it
        screenPercent = 1.5
        self.resize(self.screen().availableGeometry().size().width()/screenPercent, 
                    self.screen().availableGeometry().size().height()/screenPercent)
        self.center()

        vbox = QVBoxLayout()
        tabs = QTabWidget()
        tab1 = KMeansTab()
        tab2 = LogisticRegressionTab()
        tabs.addTab(tab1, "K-Means Clusters Visualization")
        tabs.addTab(tab2, "Recommended Vehicle Prediction")
        vbox.addWidget(tabs)

        self.setLayout(vbox)
        self.setWindowTitle("Catch-A-Ride Vehicle Recommendation Engine")

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
    main_logger.info(f'{__name__} - Program started')
    
    # Create cleaned dataset if it doesn't already exist
    if (not os.path.exists('CarRentalDataCleaned.csv')):
        main_logger.info(f'{__name__} - Creating cleaned dataset')
        DataPreperation.data_prep()

    # Create catelogical values dictionary if it doesn't already exist
    if (not os.path.exists('categorical_values.json')):
        main_logger.info(f'{__name__} - Creating catelogical values dictionary')
        DataPreperation.create_catelogical_json()
    
    # Start GUI
    app = QApplication(sys.argv)
    window = Main_Window()
    window.show()
    ret = app.exec()
    send_log_email()
    sys.exit(ret)


if __name__ == '__main__': 
    main()

