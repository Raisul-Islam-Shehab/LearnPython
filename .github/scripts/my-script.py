from github import Github
import os

# Authentication is defined via github.Auth
from github import Auth

token = os.getenv("GH_TOKEN")
# using an access token
auth = Auth.Token(token)

# Public Web Github
g = Github(auth=auth)
    
for repo in g.get_user().get_repos():
    print(repo.name)

g.close()
