from datetime import datetime, timedelta
from string import Template


def get_email_subject():
    this_week = datetime.now()
    last_week = this_week - timedelta(7)

    this_week_repr = this_week.strftime('%x')
    last_week_repr = last_week.strftime('%x')

    return f'[Weekly Report] Jones Napoleon Autumn: {last_week_repr} - {this_week_repr}'


def get_email_content(main_content):
    EMAIL_CONTENT_TEMPLATE = Template(
        'Hello Julian, <br/> $CONTENT <br/> Regards, <br/> Jones Napoleon')

    result = EMAIL_CONTENT_TEMPLATE.safe_substitute(CONTENT=main_content)
    return result
