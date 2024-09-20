from my_script import getLatestCommit
# import pytest
import unittest

class TestMyScript(unittest.TestCase):
    def test_status(self):
        response = getLatestCommit()
        self.assertEqual(response.status_code, 200)
    
    def test_committer(self):
        response = getLatestCommit()
        commits = response.json()
        latestCommit = commits[0]
        # print(latestCommit)
        self.assertEqual(latestCommit['commit']['committer']['name'], "Raisul Islam Shehab")
    
    # def test_addition(self):
    #     self.assertEqual(my_script.addition(2,3), 5)


if __name__ == "__main__":
    unittest.main(verbosity=2)

# def test_addition():
#     assert my_script.addition(2,3) == 5

# python -m coverage run -m unittest
# python -m coverage report