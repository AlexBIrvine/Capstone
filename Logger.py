import logging
import logging.handlers

# Create logger
logging.basicConfig(level = logging.DEBUG)
main_logger = logging.getLogger(__name__)

# Create handlers
file_handler = logging.FileHandler('./app.log', 'w')  # Setting to 'w' erases log on startup.  
file_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_format)
file_handler.setLevel(logging.DEBUG)
main_logger.addHandler(file_handler)

