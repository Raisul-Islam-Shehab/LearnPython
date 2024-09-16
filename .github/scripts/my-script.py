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
    
for repo in g.get_user().get_repos():
    print(repo.name)

g.close()
