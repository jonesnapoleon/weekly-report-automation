
import smtplib
import ssl
from email.message import EmailMessage

from constants import GMAIL_EMAIL, GMAIL_PASSWORD


class GmailClient:

    def __init__(self, email=GMAIL_EMAIL, password=GMAIL_PASSWORD) -> None:
        SMTP_PORT = 587
        SMTP_SERVER = "smtp.gmail.com"

        simple_email_context = ssl.create_default_context()
        self.email_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

        self.email_server.starttls(context=simple_email_context)
        self.email_server.login(email, password)

        self.email_sender = email

    def send_message(self, subject, body, email_to):

        try:
            message = EmailMessage()

            message['Subject'] = subject
            message['From'] = self.email_sender
            message['To'] = email_to
            message.add_header('Content-Type', 'text/html')
            message.set_content(body, subtype='html')

            self.email_server.send_message(
                message, message['From'], message['To'])

        except Exception as e:
            print(e)

    def quit(self):
        self.email_server.quit()
