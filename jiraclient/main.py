from typing import List

from atlassian import Jira

from constants import (JIRA_BASE_URL, JIRA_PERSONAL_ACCESS_TOKEN,
                       JIRA_USERNAME, THRESHOLD_DATE_DELTA)
from issue.issue_interface import IssueInterface

from .jira_issue import JiraIssue


class JiraClient:
    def __init__(self):
        self.jira = Jira(url=JIRA_BASE_URL, username=JIRA_USERNAME,
                         token=JIRA_PERSONAL_ACCESS_TOKEN)

    def __get_jql_request(self, anti_statuses=[], created_date=None):
        time_filter = f'AND createdDate > -{created_date}d' if created_date is not None else ''
        status_filter = f'AND status not in ({", ".join(anti_statuses)})' if anti_statuses else ''

        return f'project = SIPP AND (Developer = currentUser() OR assignee = currentUser()) {status_filter} {time_filter} ORDER BY createdDate DESC'

    def obtain_jira_tasks(self) -> List[IssueInterface]:
        todo_data = self.jira.jql(self.__get_jql_request(
            anti_statuses=[], created_date=THRESHOLD_DATE_DELTA))

        task_map = {}

        for issue in todo_data['issues']:
            subtasks = issue['fields']['subtasks']

            for subtask in subtasks:
                subtask_issue = JiraIssue(subtask)
                task_map[subtask_issue.id] = subtask_issue

            try:
                parenttask = issue['fields']['parent']
                parenttask_issue = JiraIssue(parenttask)
                task_map[parenttask_issue.id] = parenttask_issue

            except:
                continue

        return list(filter(lambda data: data.task_status not in ['Done', 'Closed'], task_map.values()))

    def obtain_jira_piechart_status(self):
        piechart_status = self.jira.jql(
            self.__get_jql_request(anti_statuses=['Done', 'Closed'], created_date=None))

        task_statuses = {}

        for issue in piechart_status['issues']:
            task_status = JiraIssue(issue).task_status
            task_statuses[task_status] = task_statuses.get(task_status, 0) + 1

        return task_statuses
