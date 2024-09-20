import requests
import os
import json

token = os.getenv("GITHUB_TOKEN")

url = "https://api.github.com/repos/Raisul-Islam-Shehab/LearnPython"

headers = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
    "Authorization": f"Bearer {token}",
}




# def getLatestCommit():
#     response = requests.get(f"{url}/commits", headers=headers)
#     # commits = response.json()
#     # latestCommit = commits[0]
#     # # print(latestCommit['commit']['author']['name'])
    
#     # commits_pretty = json.dumps(latestCommit, indent=4)
#     # print(commits_pretty)
    
#     # return latestCommit
#     # print(type(response.status_code))
#     return response


def getOpenIssues():
    page = 1
    response = requests.get(f"{url}/issues", headers=headers)
    issues = response.json()
    # commits_pretty = json.dumps(issues, indent=4) // returns sting that represents JSON
    # print(commits_pretty)
    # print(issues[0]['title'])
    # print(issues[0]['state'])
    return issues
    

    
getLatestCommit()
# getOpenIssues()


