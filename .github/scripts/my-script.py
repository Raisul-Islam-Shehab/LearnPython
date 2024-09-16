from github import Github

# Authentication is defined via github.Auth
from github import Auth

# using an access token
auth = Auth.Token("GITHUB_TOKEN")

# Public Web Github
g = Github(auth=auth)
    
for repo in g.get_user().get_repos():
    print(repo.name)

g.close()
