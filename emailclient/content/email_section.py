from typing import List

from issue.issue_adapter import IssueEmailAdapter


class EmailSection:
    def __init__(self, issues: List[IssueEmailAdapter], title):
        self.issues = issues
        self.title = title

    def generate_html(self):
        rows = [
            f'<li>{issue.html_repr}</li>' for issue in self.issues]

        return self.title + '<br/>' + '<ul>' + ''.join(rows) + '</ul>'

    def generate_text(self):
        rows = [issue.text_repr for issue in self.issues]

        return self.title + '\n' + '\n' + '\n'.join(rows)
