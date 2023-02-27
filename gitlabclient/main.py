from collections import defaultdict
from datetime import datetime, timedelta

import requests

from constants import (GITLAB_BASE_URL, GITLAB_PERSONAL_ACCESS_TOKEN,
                       GITLAB_USERNAME, THRESHOLD_DATE_DELTA)

from .merge_requests import GitlabMergeRequest


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

    def __accumulate_data(self, data):
        descriptions = defaultdict(lambda: defaultdict(set))

        for datum in data:
            ticket = datum['ticket']
            repo_name = datum['repo_name']
            title = datum['title']

            descriptions[ticket][repo_name].add(title)

        result = []

        for ticket, details in descriptions.items():

            for repo_name, titles in details.items():
                aggregated_title = ', '.join(list(titles))

                result.append({'title': aggregated_title,
                               'ticket': ticket, 'repo_name': repo_name})

        return result

    def obtain_merge_requests(self):
        data = self.__http_get_request(self.__get_gitlab_mr_path())
        return self.__accumulate_data([GitlabMergeRequest(merge_request_data).result() for merge_request_data in data])
