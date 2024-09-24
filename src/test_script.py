import my_script
import pytest


def test_get_latest_commit():
    response = my_script.get_latest_commit()
    assert response[0]["commit"]["committer"]["name"] == "Raisul Islam Shehab"


def test_get_open_issues():
    response = my_script.get_open_issues()
    assert (
        response[0]["repository_url"]
        == "https://api.github.com/repos/Raisul-Islam-Shehab/LearnPython"
    )
