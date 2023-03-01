from issue.issue_adapter import IssueEmailAdapter
from issue.issue_interface import IssueInterface


class JiraIssue(IssueInterface):
    def __init__(self, task):
        self.metadata = self.__extract_metadata(task)

    def __extract_metadata(self, data):
        issue_key = data['key']
        task_summary = data['fields']['summary']
        task_status = data['fields']['status']['name']
        return {'issue_key': issue_key, 'task_summary': task_summary, 'task_status': task_status}

    @property
    def id(self):
        return self.metadata.get('issue_key')

    @property
    def task_status(self):
        return self.metadata.get('task_status')

    @property
    def html_repr(self):
        return IssueEmailAdapter(self.id, self.metadata['task_status'],
                                 self.metadata['task_summary']).html_repr

    @property
    def text_repr(self):
        return IssueEmailAdapter(self.id, self.metadata['task_status'],
                                 self.metadata['task_summary']).text_repr
