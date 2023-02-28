

import mimetypes
import smtplib
import ssl
from email.message import EmailMessage
from email.utils import make_msgid
from pathlib import Path
from string import Template

from constants import DEFAULT_IMAGE_PATH, GMAIL_EMAIL, GMAIL_PASSWORD


class GmailClient:

    def __init__(self, email=GMAIL_EMAIL, password=GMAIL_PASSWORD) -> None:
        SMTP_PORT = 587
        SMTP_SERVER = "smtp.gmail.com"

        simple_email_context = ssl.create_default_context()
        self.email_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

        self.email_server.starttls(context=simple_email_context)
        self.email_server.login(email, password)

        self.email_sender = email

    def send_message(self, subject, body, email_to, image_path=DEFAULT_IMAGE_PATH):

        try:
            msg = EmailMessage()

            msg['Subject'] = subject
            msg['From'] = self.email_sender
            msg['To'] = ", ".join(email_to)

            template = Template(body)
            template.safe_substitute(IMAGE=f'[image: {subject}]')

            msg.set_content(template.safe_substitute(
                IMAGE=f'[image: {subject}]'))

            cid = make_msgid()[1:-1]

            msg.add_alternative(template.safe_substitute(
                IMAGE=f'<img src="cid:{cid}" />'), subtype='html')

            maintype, subtype = mimetypes.guess_type(str(image_path.split('/')[-1]))[
                0].split('/', 1)

            msg.get_payload()[1].add_related(
                Path(image_path).read_bytes(), maintype, subtype, cid=f"<{cid}>")

            Path(image_path).write_bytes(bytes(msg))

            self.email_server.send_message(msg, msg['From'], msg['To'])

        except Exception as e:
            print(e)

    def quit(self):
        self.email_server.quit()
