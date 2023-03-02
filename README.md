# Weekly report email automation

[![License](https://img.shields.io/github/license/get-icon/geticon)](https://github.com/get-icon/geticon/blob/master/LICENSE 'License')

This program automates the process of sending a weekly report email to a specified recipient (usually your direct reporting line).

The report contains data from GitLab and Jira about completed merge requests and open tasks, respectively. A pie chart is also generated to display the current status of Jira tasks.

<img src="https://github.com/get-icon/geticon/raw/master/icons/gitlab.svg" alt="React" width="21px" height="21px">
<img src="https://github.com/get-icon/geticon/raw/master/icons/jira.svg" alt="React" width="21px" height="21px">
<img src="https://github.com/get-icon/geticon/raw/master/icons/google-gmail.svg" alt="React" width="21px" height="21px">
<img src="https://github.com/get-icon/geticon/raw/master/icons/python.svg" alt="React" width="21px" height="21px">

## Setup

1. Clone the repository

`git clone https://github.com/jonesnapoleon/weekly-report-automation`

2. Set up your credentials.

- Create your [GitLab personal access token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html)
- Create your [Jira personal access token](https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html)
- Create your [Gmail app passwords](https://support.google.com/accounts/answer/185833?hl=en#zippy=%2Cwhy-you-may-need-an-app-password)
- Copy the content of `.env.example` to `.env`, and configure the credentials accordingly.

3. Install the dependencies

It's recommended to install via docker.

```bash
docker build -t weekly-report-email .
docker run weekly-report-email
```

Alternatively, you can install it directly (or with Python virtual environment of your choice).

`pip install -r requirements.txt`

## License

This project is licensed under the MIT License. See LICENSE for more information.
