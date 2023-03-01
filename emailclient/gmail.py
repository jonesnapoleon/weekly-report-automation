
import mimetypes
import smtplib
import ssl
from email.message import EmailMessage
from email.utils import make_msgid
from pathlib import Path
from string import Template

from constants import (DEFAULT_JIRA_STATUS_IMAGE_PATH, EMAIL_RECIPIENTS,
                       GMAIL_EMAIL, GMAIL_PASSWORD)
from emailclient.content.email_content import EmailContent


class GmailClient:

    def __init__(self, email=GMAIL_EMAIL, password=GMAIL_PASSWORD) -> None:
        SMTP_PORT = 587
        SMTP_SERVER = "smtp.gmail.com"

        simple_email_context = ssl.create_default_context()
        self.email_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

        self.email_server.starttls(context=simple_email_context)
        self.email_server.login(email, password)

        self.email_sender = email

    def setup_email(self, subject, email_to=EMAIL_RECIPIENTS):
        print('Setting up email')

        try:
            self.message = EmailMessage()

            self.message['Subject'] = subject
            self.message['From'] = self.email_sender
            self.message['To'] = email_to
        except Exception as e:
            print(e)

        return self

    def __add_text_message(self, text_content):
        template = Template(text_content)

        self.message.set_content(template.safe_substitute(
            IMAGE=f'[image: {self.message["Subject"]}]'))

        return self

    def __add_html_message(self, html_content):
        template = Template(html_content)

        self.cid = make_msgid()[1:-1]

        self.message.add_alternative(template.safe_substitute(
            IMAGE=f'<img src="cid:{self.cid}" />'), subtype='html')

        return self

    def __add_image_content(self, image_path):
        maintype, subtype = mimetypes.guess_type(str(image_path.split('/')[-1]))[
            0].split('/', 1)

        self.message.get_payload()[1].add_related(
            Path(image_path).read_bytes(), maintype, subtype, cid=f"<{self.cid}>")

        Path(image_path).write_bytes(bytes(self.message))

        return self

    def add_body(self, email_content: EmailContent, image_path=DEFAULT_JIRA_STATUS_IMAGE_PATH):
        print('Constructing email body')
        try:
            self.__add_text_message(email_content.text_content)
            self.__add_html_message(email_content.html_content)

            self.__add_image_content(image_path)

        except Exception as e:
            print(e)

        return self

    def send_message(self):
        print('Sending email...')
        try:
            self.email_server.send_message(
                self.message, self.message['From'], self.message['To'])
            print('Email sent successfully')

        except Exception as e:
            print('Fail to send email', e)

        return self

    def quit(self):
        self.email_server.quit()
