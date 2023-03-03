from string import Template

DEFAULT_DATE_DELTA = 48

JIRA_BROWSE_PATH = "https://jones.jira.com/browse/"
DEFAULT_JIRA_PROJECT_NAME = 'JONES_PROJECT'

HAVE_DONE_MESSAGE = "Last week, I've done:"
TO_DO_MESSAGE = 'This week, I will do:'
PIECHART_MESSAGE = 'Current issue statuses'


EMAIL_RECIPIENTS = ['noreply@jones.com',
                    'hi1@jones.com']


EMAIL_CONTENT_HTML_TEMPLATE = Template(
    'Hello Mister,<br/>$CONTENT<br/>$IMAGE<br/>Regards,<br/>Jones Napoleon')

EMAIL_CONTENT_TEXT_TEMPLATE = Template(
    'Hello Mister,\n$CONTENT\n$IMAGE\nRegards,\nJones Napoleon')

EMAIL_SUBJECT_PLACEHOLDER = Template(
    '[Weekly Report] Jones Napoleon Autumn: $LAST_WEEK - $THIS_WEEK')


DEFAULT_JIRA_STATUS_IMAGE_PATH = 'jira_status.jpg'
