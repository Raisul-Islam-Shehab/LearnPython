from github import Github
import os

# Authentication is defined via github.Auth
from github import Auth

token = os.getenv("GITHUB_TOKEN")

if not token:
    raise ValueError("GitHub token not found in environment variables!")
    
# using an access token
auth = Auth.Token(token=token)

# Public Web Github
g = Github(auth=auth)
    
repo = g.get_repo("Raisul-Islam-Shehab/LearnPython")
print(repo.name)

branches = list(repo.get_branches())
print(branches)

main_branch = repo.get_branch(branch="main")
print(main_branch.commit)

g.close()
