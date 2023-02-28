from atlassian import Jira

from constants import (JIRA_BASE_PATH, JIRA_PERSONAL_ACCESS_TOKEN,
                       JIRA_USERNAME, THRESHOLD_DATE_DELTA)


class JiraClient:
    def __init__(self):
        self.jira = Jira(url=JIRA_BASE_PATH, username=JIRA_USERNAME,
                         token=JIRA_PERSONAL_ACCESS_TOKEN)

        self.todo_data = self.jira.jql(self.__get_jql_request_for_todo())

        self.piechart_status = self.jira.jql(
            self.__get_jql_request_for_piechart_status())

    def __extract_metadata(self, data):
        issue_key = data['key']

        task_summary = data['fields']['summary']
        task_status = data['fields']['status']['name']

        issue_type_name = data['fields']['issuetype']['name']

        return {'issue_key': issue_key, 'task_summary': task_summary, 'task_status': task_status, 'issue_type_name': issue_type_name}

    def __get_jql_request_for_todo(self):
        return f'project = SIPP AND (Developer = currentUser() OR assignee = currentUser()) AND createdDate > -{THRESHOLD_DATE_DELTA}d ORDER BY createdDate DESC'

    def __get_jql_request_for_piechart_status(self):
        return f'project = SIPP AND (Developer = currentUser() OR assignee = currentUser()) AND status not in (Done, Closed) ORDER BY createdDate DESC'

    def obtain_jira_tasks(self, anti_statuses=[]):
        result = []

        for issue in self.todo_data['issues']:
            subtasks = issue['fields']['subtasks']

            for subtask in subtasks:
                result.append(self.__extract_metadata(subtask))

            try:
                parenttask = issue['fields']['parent']
                result.append(self.__extract_metadata(parenttask))
            except:
                continue

        return list(filter(lambda data: data['task_status'] not in anti_statuses, result))

    def obtain_jira_piechart_status(self):
        task_statuses = {}

        for issue in self.piechart_status['issues']:
            task_status = self.__extract_metadata(issue)['task_status']
            task_statuses[task_status] = task_statuses.get(task_status, 0) + 1

        return task_statuses
