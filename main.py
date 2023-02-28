from constants import EMAIL_RECIPIENTS, HAVE_DONE_MESSAGE, TO_DO_MESSAGE
from emailclient.body import get_email_content, get_email_subject
from emailclient.gmail import GmailClient
from emailclient.section import HTMLSection
from gitlabclient.main import GitlabClient
from jiraclient.main import JiraClient

if __name__ == "__main__":
    have_done_data = GitlabClient().obtain_merge_requests()

    to_do_data = JiraClient().obtain_jira_tasks(
        anti_statuses=['Done', 'Closed'])

    JiraClient().obtain_jira_status_progresses

    have_done_email_content = HTMLSection(have_done_data,
                                          title=HAVE_DONE_MESSAGE, type='HAVE_DONE').process()

    to_do_email_content = HTMLSection(to_do_data,
                                      title=TO_DO_MESSAGE, type='TO_DO').process()

    email_subject = get_email_subject()
    email_content = get_email_content(
        have_done_email_content + to_do_email_content)

    gmail_client = GmailClient()
    gmail_client.send_message(email_subject, email_content, EMAIL_RECIPIENTS)
    gmail_client.quit()
