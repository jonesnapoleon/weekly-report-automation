from datetime import datetime, timedelta

from constants.data import (EMAIL_CONTENT_HTML_TEMPLATE,
                            EMAIL_CONTENT_TEXT_TEMPLATE,
                            EMAIL_SUBJECT_PLACEHOLDER, HAVE_DONE_MESSAGE,
                            TO_DO_MESSAGE)

from .email_section import EmailSection


def get_email_subject():
    this_week = datetime.now()
    last_week = this_week - timedelta(7)

    this_week_repr = this_week.strftime('%x')
    last_week_repr = last_week.strftime('%x')

    subject = EMAIL_SUBJECT_PLACEHOLDER.safe_substitute(
        LAST_WEEK=last_week_repr, THIS_WEEK=this_week_repr)
    return subject


class EmailContent:
    def __init__(self, have_done_data, to_do_data):
        self.have_done_email_section = EmailSection(
            have_done_data, title=HAVE_DONE_MESSAGE)

        self.to_do_email_section = EmailSection(
            to_do_data, title=TO_DO_MESSAGE)

    @property
    def text_content(self):
        content_result = f'{self.have_done_email_section.generate_text()} \n {self.to_do_email_section.generate_text()}'

        result = EMAIL_CONTENT_TEXT_TEMPLATE.safe_substitute(
            CONTENT=content_result)
        return result

    @property
    def html_content(self):
        content_result = f'{self.have_done_email_section.generate_html()} <br/> {self.to_do_email_section.generate_html()}'

        result = EMAIL_CONTENT_HTML_TEMPLATE.safe_substitute(
            CONTENT=content_result)
        return result
