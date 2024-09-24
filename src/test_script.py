import my_script
import pprint


def test_get_latest_commit():
    response = my_script.get_latest_commit()
    latestCommit = response[0]
    # pprint.pprint(response)
    # print(latestCommit['commit'])
    assert latestCommit["commit"]["committer"]["name"] == "Raisul Islam Shehab"


def test_get_open_issues():
    response = my_script.get_open_issues()
    latestIssue = response[0]
    # pprint.pprint(latestIssue['repository_url'])
    assert (
        latestIssue["repository_url"]
        == "https://api.github.com/repos/Raisul-Islam-Shehab/LearnPython"
    )

# test_get_latest_commit()
# test_get_open_issues()