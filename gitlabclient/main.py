from collections import defaultdict
from datetime import datetime, timedelta
from typing import List

import requests

from constants import (GITLAB_BASE_URL, GITLAB_PERSONAL_ACCESS_TOKEN,
                       GITLAB_USERNAME, THRESHOLD_DATE_DELTA)
from issue.issue_interface import IssueInterface

from .gitlab_merge_requests import GitlabMergeRequest


class GitlabClient:

    def __http_get_request(self, url):
        REQUEST_HEADERS = {
            'Authorization': f'Bearer {GITLAB_PERSONAL_ACCESS_TOKEN}'}

        response = requests.get(
            f'{GITLAB_BASE_URL}/{url}',  headers=REQUEST_HEADERS)
        return response.json()

    def __threshold_date_since(self, delta=THRESHOLD_DATE_DELTA):
        target_date = datetime.now() - timedelta(days=delta)
        return target_date.isoformat()

    def __get_gitlab_mr_path(self):
        return f'/merge_requests?author_username={GITLAB_USERNAME}&updated_after={self.__threshold_date_since()}'

    def __accumulate_data(self, data: List[GitlabMergeRequest]):
        descriptions = defaultdict(lambda: defaultdict(set))

        for datum in data:
            ticket = datum.metadata['ticket']
            project_name = datum.metadata['project_name']
            title = datum.metadata['title']

            descriptions[ticket][project_name].add(title)

        result = []

        for ticket, details in descriptions.items():
            for project_name, titles in details.items():
                aggregated_title = ', '.join(list(titles))

                result.append(GitlabMergeRequest(mr_data=None,  metadata={'title': aggregated_title,
                                                                          'ticket': ticket, 'project_name': project_name}))

        return result

    def obtain_merge_requests(self) -> List[IssueInterface]:
        data = self.__http_get_request(self.__get_gitlab_mr_path())
        return self.__accumulate_data([GitlabMergeRequest(merge_request_data) for merge_request_data in data])
