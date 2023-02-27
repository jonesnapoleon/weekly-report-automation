import re
from collections import defaultdict
from datetime import datetime, timedelta

import requests

from constants import (GITLAB_BASE_URL, GITLAB_PERSONAL_ACCESS_TOKEN,
                       GITLAB_USERNAME, THRESHOLD_DATE_DELTA)


def threshold_date_since(delta: int) -> str:
    target_date = datetime.now() - timedelta(days=delta)
    return target_date.isoformat()


def http_get_request(url):
    REQUEST_HEADERS = {
        'Authorization': f'Bearer {GITLAB_PERSONAL_ACCESS_TOKEN}'}

    response = requests.get(
        f'{GITLAB_BASE_URL}/{url}',  headers=REQUEST_HEADERS)
    return response.json()


def get_project_name(url):
    try:
        repo_path = url.split('/-/merge_request')[0]
        project_slug = repo_path.split('/')[-1]
        return ' '.join([slug.upper() for slug in project_slug.split('-')])
    except:
        return url


def get_ticket(merge_request_data):
    heading = merge_request_data['title']

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


def get_title(merge_request_data, repo_name):
    heading = merge_request_data['title']

    try:
        if 'chore' in heading and 'release' in heading:
            return f'Release {repo_name}'

        full_title = heading.split(']')[-1]
        title_elements = full_title.split(':')

        if len(title_elements) == 1:
            return title_elements[0].strip()

        return ':'.join(title_elements[1:]).strip()

    except:
        return heading


def get_repo_name(merge_request_data):
    try:
        return get_project_name(merge_request_data['web_url'])
    except:
        return ''


def extract_merge_request_object(merge_request_data):
    ticket = get_ticket(merge_request_data)
    repo_name = get_repo_name(merge_request_data)
    title = get_title(merge_request_data, repo_name)

    return {'ticket': ticket, 'title': title, 'repo_name': repo_name}


def process_mr_objects(data):
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


def obtain_merge_requests():
    path = f'/merge_requests?author_username={GITLAB_USERNAME}&updated_after={threshold_date_since(THRESHOLD_DATE_DELTA)}'
    data = http_get_request(path)

    extracted_mrs = [extract_merge_request_object(
        merge_request_data) for merge_request_data in data]

    return process_mr_objects(extracted_mrs)
