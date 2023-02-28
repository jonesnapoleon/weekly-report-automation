from constants import (EMAIL_RECIPIENTS, HAVE_DONE_MESSAGE, PIECHART_MESSAGE,
                       TO_DO_MESSAGE)
from emailclient.body import get_email_content, get_email_subject
from emailclient.chart import PieChart
from emailclient.gmail import GmailClient
from emailclient.section import HTMLSection
from gitlabclient.main import GitlabClient
from jiraclient.main import JiraClient

if __name__ == "__main__":
    gitlab_client = GitlabClient()
    jira_client = JiraClient()
    gmail_client = GmailClient()

    have_done_data = gitlab_client.obtain_merge_requests()
    to_do_data = jira_client.obtain_jira_tasks(
        anti_statuses=['Done', 'Closed'])
    piechart_status = jira_client.obtain_jira_piechart_status()

    have_done_email_content = HTMLSection(data=have_done_data,
                                          title=HAVE_DONE_MESSAGE, type='HAVE_DONE').process()
    to_do_email_content = HTMLSection(data=to_do_data,
                                      title=TO_DO_MESSAGE, type='TO_DO').process()
    PieChart(
        jira_status=piechart_status, title=PIECHART_MESSAGE).process()

    email_subject = get_email_subject()
    email_content = get_email_content(
        have_done_email_content + to_do_email_content)

    gmail_client.send_message(email_subject, email_content, EMAIL_RECIPIENTS)
    gmail_client.quit()
