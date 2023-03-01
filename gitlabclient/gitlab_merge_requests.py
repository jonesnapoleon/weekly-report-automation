import re

from issue.issue_adapter import IssueEmailAdapter
from issue.issue_interface import IssueInterface


class GitlabMergeRequest(IssueInterface):

    def __init__(self, mr_data, metadata=None):
        self.metadata = metadata if metadata is not None else self.__extract_merge_request_object(
            mr_data)

    def __extract_merge_request_object(self, mr_data):
        ticket = self.__get_ticket(mr_data)
        project_name = self.__get_project_name(mr_data)
        title = self.__get_title(mr_data)
        return {'ticket': ticket, 'title': title, 'project_name': project_name}

    def __get_project_name(self, mr_data):
        try:
            url = mr_data['web_url']
            repo_path = url.split('/-/merge_request')[0]
            project_slug = repo_path.split('/')[-1]
            return ' '.join([slug.upper() for slug in project_slug.split('-')])
        except:
            return url

    def __get_ticket(self, mr_data):
        heading = mr_data['title']

        try:
            if 'chore' in heading and 'release' in heading:
                return ''

            REGEX_RULE = r'\[(.*)\]'
            regex_result = re.search(REGEX_RULE, heading).group(1)

            while len(regex_result.split(']')) > 1:
                regex_result = regex_result.split(']')[0]

            return regex_result
        except:
            return heading

    def __get_title(self, mr_data):
        heading = mr_data['title']

        try:
            if 'chore' in heading and 'release' in heading:
                return f'Release {self.metadata["project_name"]}'

            full_title = heading.split(']')[-1]
            title_elements = full_title.split(':')

            if len(title_elements) == 1:
                return title_elements[0].strip()

            return ':'.join(title_elements[1:]).strip()

        except:
            return heading

    @property
    def html_repr(self):
        return IssueEmailAdapter(self.metadata['ticket'], self.metadata['project_name'],
                                 self.metadata['title']).html_repr

    @property
    def text_repr(self):
        return IssueEmailAdapter(self.metadata['ticket'], self.metadata['project_name'],
                                 self.metadata['title']).text_repr
