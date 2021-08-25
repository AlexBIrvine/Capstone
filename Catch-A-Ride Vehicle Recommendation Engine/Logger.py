import logging
import logging.handlers
import yagmail
import datetime

# Create logger
logging.basicConfig(level = logging.DEBUG)
main_logger = logging.getLogger(__name__)

# Create handlers
file_handler = logging.FileHandler('./app.log', 'w')  # Setting to 'w' erases log on startup.  
file_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_format)
file_handler.setLevel(logging.DEBUG)
main_logger.addHandler(file_handler)

def send_log_email():
    """
    Sends an email from a temporary gmail account to the developer containing the log file generated during the user session.
    """
    yagmail.register('sixpakal.bot@gmail.com', '972305Bot')

    email_sender = yagmail.SMTP("sixpakal.bot@gmail.com").send(
        to="alex-irvine-capstone@mailinator.com",
        subject=f"{datetime.datetime.now()} - Program log",
        contents="User has closed the program, log attached", 
        attachments="app.log",
    )
