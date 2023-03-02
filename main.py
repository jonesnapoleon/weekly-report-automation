from emailclient.content.email_content import EmailContent, get_email_subject
from emailclient.content.jira_status_chart import PieChart
from emailclient.main import GmailClient
from gitlabclient.main import GitlabClient
from jiraclient.main import JiraClient

if __name__ == "__main__":
    gitlab_client = GitlabClient()
    jira_client = JiraClient()
    gmail_client = GmailClient()

    have_done_data = gitlab_client.obtain_merge_requests()
    to_do_data = jira_client.obtain_jira_tasks()

    task_statuses = jira_client.obtain_jira_task_statuses()
    PieChart(task_statuses).generate_and_save_image()

    email_subject = get_email_subject()
    email_content = EmailContent(have_done_data, to_do_data)

    gmail_client.setup_email(email_subject).add_body(
        email_content).send_message().quit()
