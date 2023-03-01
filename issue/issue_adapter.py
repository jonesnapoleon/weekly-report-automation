class IssueEmailAdapter:
    def __init__(self, ticket, strong_text, description):
        self.ticket = ticket
        self.strong_text = strong_text
        self.description = description

    def __get_jira_ticket_rich_format(self, ticket):
        if not ticket:
            return ticket

        JIRA_BROWSE_PATH = "https://jira.shopee.io/browse/"
        ticket_url = f'{JIRA_BROWSE_PATH}{ticket}'
        return f'[<a href={ticket_url}>{ticket}</a>]'

    @property
    def html_repr(self):
        return f'{self.__get_jira_ticket_rich_format(self.ticket)} <b>{self.strong_text}</b>: {self.description} '

    @property
    def text_repr(self):
        return f'[{self.ticket}] {self.strong_text}: {self.description}'
