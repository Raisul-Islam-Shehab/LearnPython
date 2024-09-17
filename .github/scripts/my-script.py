from github import Github
import os

# Authentication is defined via github.Auth
from github import Auth

token = os.getenv("GITHUB_TOKEN")

if not token:
    raise ValueError("GitHub token not found in environment variables!")

# using an access token
auth = Auth.Token(token)

# Public Web Github
g = Github(auth=auth)


def getLatestCommit(repoName):
    repo = g.get_repo(repoName)
    latestCommit = repo.get_commits()[0]
    print(f"Latest commit SHA: {latestCommit.sha}")
    print(f"Latest commit message: {latestCommit.commit.message}")


def listOfOpenIssues(repoName):
    repo = g.get_repo(repoName)
    open_issues = repo.get_issues(state="open")
    for issue in open_issues:
        print(issue)


def listPullRequests(repoName):
    repo = g.get_repo(repoName)
    pulls = repo.get_pulls(state="open", sort="created", base="main")
    for pr in pulls:
        print(pr)


getLatestCommit("Raisul-Islam-Shehab/LearnPython")
listOfOpenIssues("Raisul-Islam-Shehab/LearnPython")
listPullRequests("Raisul-Islam-Shehab/LearnPython")

g.close()
