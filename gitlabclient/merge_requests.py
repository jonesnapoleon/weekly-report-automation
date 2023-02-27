import re


class GitlabMergeRequest:

    def __init__(self, data):
        self.merge_request_data = data

    def result(self):
        return self.__extract_merge_request_object()

    def __extract_merge_request_object(self):
        ticket = self.__get_ticket()
        repo_name = self.__get_repo_name()
        title = self.__get_title()

        return {'ticket': ticket, 'title': title, 'repo_name': repo_name}

    def __get_project_name(self):
        try:
            url = self.merge_request_data['web_url']
            repo_path = url.split('/-/merge_request')[0]
            project_slug = repo_path.split('/')[-1]
            return ' '.join([slug.upper() for slug in project_slug.split('-')])
        except:
            return url

    def __get_ticket(self):
        heading = self.merge_request_data['title']

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

    def __get_title(self):
        heading = self.merge_request_data['title']

        try:
            if 'chore' in heading and 'release' in heading:
                return f'Release {self.__get_repo_name()}'

            full_title = heading.split(']')[-1]
            title_elements = full_title.split(':')

            if len(title_elements) == 1:
                return title_elements[0].strip()

            return ':'.join(title_elements[1:]).strip()

        except:
            return heading

    def __get_repo_name(self):
        try:
            return self.__get_project_name()
        except:
            return ''
