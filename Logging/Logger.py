import logging
import logging.handlers
import yagmail


# Make this into a class

# Create logger
main_logger = logging.getLogger(__name__)

# Create handlers & set levels
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('app.log')

console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.ERROR)
main_logger.addHandler(console_handler)
main_logger.addHandler(file_handler)

# Send email with log attachment
email_sender = yagmail.SMTP("sixpakal.bot@gmail.com").send(
    to="alex.b.irvine@gmail.com",
    subject="This is where I put the subject",
    contents="Another test", 
    attachments="app.log",
)


def main():
    print("working")

    main_logger.debug('still working')
    main_logger.info("Also working")
    main_logger.error('Crashed')
    print(main_logger.handlers)

if __name__ == '__main__':
    main()