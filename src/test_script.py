import my_script
# import pprint

def test_get_latest_commit():
    response = my_script.get_latest_commit()
    # print(type(response))
    # pprint.pprint(response)
    latestCommit = response.json()[0]
    # print(type(latestCommit))
    # pprint.pprint(response)
    # print(latestCommit['commit']["committer"]["name"])
    assert latestCommit["commit"]["committer"]["name"] == "Raisul Islam Shehab"


# def test_get_open_issues():
#     response = my_script.get_open_issues()
#     print(type(response))
#     latestIssue = response[0]
#     # pprint.pprint(latestIssue['repository_url'])
#     print(latestIssue['repository_url'])
#     print(type(latestIssue))
#     assert (
#         latestIssue["repository_url"]
#         == "https://api.github.com/repos/Raisul-Islam-Shehab/LearnPython"
#     )


# test_get_latest_commit()
# test_get_open_issues()
