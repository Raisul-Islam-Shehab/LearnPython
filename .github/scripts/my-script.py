from github import Github

# Authentication is defined via github.Auth
from github import Auth

# using an access token
auth = Auth.Token("GITHUB_TOKEN")

# Public Web Github
g = Github(auth=auth)
    
repo = g.get_repo("Raisul-Islam-Shehab/LearnPython")
print(repo.name)

branches = list(repo.get_branches())
print(branches)

main_branch = repo.get_branch(branch="main")
print(main_branch.commit)
