import yagmail

def send_error_report_over_email():
    email_sender = yagmail.SMTP("sixpakal.bot@gmail.com").send(
        to="alex.b.irvine@gmail.com",
        subject="This is where I put the subject",
        contents="Another test", 
        attachments="app.log",
    )