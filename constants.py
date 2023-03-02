from string import Template

from decouple import config

GITLAB_USERNAME = config('GITLAB_USERNAME')
GITLAB_BASE_URL = config('GITLAB_BASE_URL')
GITLAB_PERSONAL_ACCESS_TOKEN = config('GITLAB_PERSONAL_ACCESS_TOKEN')

JIRA_BASE_URL = config('JIRA_BASE_URL')
JIRA_USERNAME = config('JIRA_USERNAME')
JIRA_PERSONAL_ACCESS_TOKEN = config('JIRA_PERSONAL_ACCESS_TOKEN')

GMAIL_EMAIL = config('GMAIL_EMAIL')
GMAIL_PASSWORD = config('GMAIL_PASSWORD')
GMAIL_NAME = config('GMAIL_NAME')

DEFAULT_JIRA_STATUS_IMAGE_PATH = 'jira_status.jpg'

HAVE_DONE_MESSAGE = "Last week, I've done:"
TO_DO_MESSAGE = 'This week, I will do:'
DEFAULT_PIECHART_MESSAGE = 'Current issue statuses'


THRESHOLD_DATE_DELTA = 48
EMAIL_RECIPIENTS = ['jones.autumn@seamoney.com',
                    'condro.wiyono@seamoney.com']


EMAIL_CONTENT_HTML_TEMPLATE = Template(
    'Hello Mister,<br/>$CONTENT<br/>$IMAGE<br/>Regards,<br/>Jones Napoleon')

EMAIL_CONTENT_TEXT_TEMPLATE = Template(
    'Hello Mister,\n$CONTENT\n$IMAGE\nRegards,\nJones Napoleon')
