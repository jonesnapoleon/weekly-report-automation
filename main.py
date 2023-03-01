from emailclient.content.email_content import EmailContent, get_email_subject
from emailclient.content.jira_status_chart import PieChart
from emailclient.gmail import GmailClient
from gitlabclient.main import GitlabClient
from jiraclient.main import JiraClient

if __name__ == "__main__":
    gitlab_client = GitlabClient()
    jira_client = JiraClient()
    gmail_client = GmailClient()

    have_done_data = gitlab_client.obtain_merge_requests()
    to_do_data = jira_client.obtain_jira_tasks()

    piechart_status = jira_client.obtain_jira_piechart_status()
    PieChart(piechart_status).generate_and_save_image()

    email_subject = get_email_subject()
    email_content = EmailContent(have_done_data, to_do_data)

    gmail_client.setup_email(email_subject).add_body(
        email_content).send_message().quit()

# have_done_email_content = HTMLSection(data=have_done_data,
#                                       title=HAVE_DONE_MESSAGE, type='HAVE_DONE').process()
# to_do_email_content = HTMLSection(data=to_do_data,
#                                   title=TO_DO_MESSAGE, type='TO_DO').process()

# PieChart(jira_status=piechart_status,
#          title=PIECHART_MESSAGE).generate_image()

# EmailSection(have_done_data, title=HAVE_DONE_MESSAGE)
# EmailSection(to_do_data, title=TO_DO_MESSAGE)

# email_content = get_email_content(
#     have_done_email_content + to_do_email_content)

# gmail_client.send_message(email_subject, email_content, EMAIL_RECIPIENTS)
# gmail_client.quit()
