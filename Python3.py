import requests

jira_url = "https://your-jira-instance-url/rest/auth/1/session"
jira_login_data = {
    "username": "your-username",
    "password": "your-password"
    "username": "b5cdc1aa-195c-4c3b-848c-65b081374826",
    "password": "6GlIwFy2Gpj1/T6dLcW+ZBDu+gA="
}
jira_response = requests.post(jira_url, json=jira_login_data)

if jira_response.status_code == 200:
    auth_headers = {
        "Cookie": jira_response.headers['Set-Cookie'],
    }
else:
    print(f"Login failed (HTTP status code: {jira_response.status_code})")


new_issue_url = "https://scbtechx.atlassian.net/rest/api/3/issue/"
new_issue_data = {
    "fields": {
        "project": {
            "key": "YOUR_PROJECT_KEY"
        },
        "summary": "Issue Summary",
        "description": "Issue Description",
        "issuetype": {
            "name": "Task"  # ปรับเป็นประเภทการ์ดที่คุณต้องการ
        }
    }
}

create_issue_response = requests.post(new_issue_url, json=new_issue_data, headers=auth_headers)

if create_issue_response.status_code == 201:
    print("Issue created successfully!")
else:
    print(f"Failed to create issue (HTTP status code: {create_issue_response.status_code})")


prismakey
https://scbtechx.atlassian.net


 Amazon Linux 2 Benchmark
v2.0.0