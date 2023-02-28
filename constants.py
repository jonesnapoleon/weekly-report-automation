from decouple import config

GITLAB_USERNAME = config('GITLAB_USERNAME')
GITLAB_BASE_URL = config('GITLAB_BASE_URL')
GITLAB_PERSONAL_ACCESS_TOKEN = config('GITLAB_PERSONAL_ACCESS_TOKEN')


JIRA_BASE_PATH = config('JIRA_BASE_PATH')
JIRA_USERNAME = config('JIRA_USERNAME')
JIRA_PERSONAL_ACCESS_TOKEN = config('JIRA_PERSONAL_ACCESS_TOKEN')

THRESHOLD_DATE_DELTA = 48

HAVE_DONE_MESSAGE = "Last week, I've done:"
TO_DO_MESSAGE = 'This week, I will do:'

GMAIL_EMAIL = config('GMAIL_EMAIL')
GMAIL_PASSWORD = config('GMAIL_PASSWORD')

EMAIL_RECIPIENTS = ['jones.autumn@seamoney.com', 'condro.wiyono@seamoney.com']
