import my_script
import unittest

# # import pprint


# def test_get_latest_commit():
#     response = my_script.get_latest_commit()
#     # print(type(response))
#     # pprint.pprint(response)
#     latestCommit = response.json()[0]
#     print(type(latestCommit))
#     # pprint.pprint(response)
#     print(latestCommit["commit"]["committer"]["name"])
#     # assert latestCommit["commit"]["committer"]== "Raisul Islam Shehab"


# def test_get_open_issues():
#     response = my_script.get_open_issues()
#     # print(type(response))
#     latestIssue = response[0]
#     # pprint.pprint(latestIssue['repository_url'])
#     print(type(latestIssue))
#     print(latestIssue["repository_url"])
#     # assert (
#     #     latestIssue["repository_url"]
#     #     == "https://api.github.com/repos/Raisul-Islam-Shehab/LearnPython"
#     # )


# test_get_latest_commit()
# test_get_open_issues()


class TestMyScript(unittest.TestCase):
    def test_get_latest_commit(self):
        response = my_script.get_latest_commit()
        self.assertEqual(response.status_code, 200)

    def test_get_open_issues(self):
        issues = my_script.get_open_issues()

        latestIssue = issues[0]
        # print(latestCommit)
        self.assertEqual(
            latestIssue["repository_url"],
            "https://api.github.com/repos/Raisul-Islam-Shehab/LearnPython",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
