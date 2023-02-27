from gitlabclient.main import GitlabClient
from jiraclient.main import JiraClient

if __name__ == "__main__":
    have_done_data = GitlabClient().obtain_merge_requests()

    to_do_data = JiraClient().obtain_jira_tasks(
        anti_statuses=['Done', 'Closed'])

    print(to_do_data, have_done_data)
