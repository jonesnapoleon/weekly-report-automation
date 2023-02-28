from atlassian import Jira

from constants import (JIRA_BASE_PATH, JIRA_PERSONAL_ACCESS_TOKEN,
                       JIRA_USERNAME, THRESHOLD_DATE_DELTA)


class JiraClient:
    def __init__(self):
        self.jira = Jira(url=JIRA_BASE_PATH, username=JIRA_USERNAME,
                         token=JIRA_PERSONAL_ACCESS_TOKEN)

        self.data = self.jira.jql(self.__get_jql_request())

    def __extract_metadata(self, data):
        issue_key = data['key']

        task_summary = data['fields']['summary']
        task_status = data['fields']['status']['name']

        issue_type_name = data['fields']['issuetype']['name']

        return {'issue_key': issue_key, 'task_summary': task_summary, 'task_status': task_status, 'issue_type_name': issue_type_name}

    def __get_jql_request(self):
        return f'project = SIPP AND (Developer = currentUser() OR assignee = currentUser()) AND createdDate > -{THRESHOLD_DATE_DELTA}d ORDER BY createdDate DESC'

    def obtain_jira_tasks(self, anti_statuses=[]):

        result = []

        for issue in self.data['issues']:
            subtasks = issue['fields']['subtasks']

            for subtask in subtasks:
                result.append(self.__extract_metadata(subtask))

            try:
                parenttask = issue['fields']['parent']
                result.append(self.__extract_metadata(parenttask))
            except:
                continue

        return list(filter(lambda data: data['task_status'] not in anti_statuses, result))

    def obtain_jira_status_progresses(self):
        result = []

        for issue in self.data['issues']:
            subtasks = issue['fields']['subtasks']

            for subtask in subtasks:
                result.append(self.__extract_metadata(subtask))

            try:
                parenttask = issue['fields']['parent']
                result.append(self.__extract_metadata(parenttask))
            except:
                continue

        print(result)
