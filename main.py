from gitlab import obtain_merge_requests
from jira import obtain_jira_tasks

if __name__ == "__main__":
    have_done_data = obtain_merge_requests()

    to_do_data = obtain_jira_tasks(anti_statuses=['Done', 'Closed'])
    print(to_do_data, have_done_data)
