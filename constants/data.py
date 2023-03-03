from string import Template

DEFAULT_DATE_DELTA = 48

JIRA_BROWSE_PATH = "https://jira.shopee.io/browse/"
DEFAULT_JIRA_PROJECT_NAME = 'SIPP'

HAVE_DONE_MESSAGE = "Last week, I've done:"
TO_DO_MESSAGE = 'This week, I will do:'
PIECHART_MESSAGE = 'Current issue statuses'


EMAIL_RECIPIENTS = ['jones.autumn@seamoney.com',
                    'condro.wiyono@seamoney.com']


EMAIL_CONTENT_HTML_TEMPLATE = Template(
    'Hello Mister,<br/>$CONTENT<br/>$IMAGE<br/>Regards,<br/>Jones Napoleon')

EMAIL_CONTENT_TEXT_TEMPLATE = Template(
    'Hello Mister,\n$CONTENT\n$IMAGE\nRegards,\nJones Napoleon')

EMAIL_SUBJECT_PLACEHOLDER = Template(
    '[Weekly Report] Jones Napoleon Autumn: $LAST_WEEK - $THIS_WEEK')


DEFAULT_JIRA_STATUS_IMAGE_PATH = 'jira_status.jpg'
