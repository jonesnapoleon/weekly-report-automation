

class HTMLSection:

    def __init__(self, data, title='', type=None):
        self.data = data
        self.title = title
        self.type = type

    def __get_jira_ticket_rich_format(self, ticket):
        if not ticket:
            return ticket

        JIRA_BROWSE_PATH = "https://jira.shopee.io/browse/"
        ticket_url = f'{JIRA_BROWSE_PATH}{ticket}'
        return f'[<a href={ticket_url}>{ticket}</a>]'

    def __generate_ticket_description(self, item):
        if self.type == 'HAVE_DONE':
            jira_ticket = self.__get_jira_ticket_rich_format(item['ticket'])
            jira_title = item['title']
            jira_repo_name = item['repo_name']
            return f'{jira_ticket} <b>{jira_repo_name}</b>: {jira_title} '

        if self.type == 'TO_DO':
            jira_ticket = self.__get_jira_ticket_rich_format(item['issue_key'])
            jira_title = item['task_summary']
            jira_status = item['task_status']
            return f'{jira_ticket} <b>{jira_status}</b>: {jira_title} '

    def process(self):
        rows = []

        for ticket in self.data:
            rows.append(
                f'<li>{self.__generate_ticket_description(ticket)}</li>')

        return self.title + '<br/>' + '<ul>' + ''.join(rows) + '</ul>'
