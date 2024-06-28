#!/usr/bin/env python3
"""
In a new test_client.py file, declare the
TestGithubOrgClient(unittest.TestCase) class and implement the test_org method.
This method should test that GithubOrgClient.org returns the correct value.
Use @patch as a decorator to make sure get_json is called once with the
expected argument but make sure it is not executed.
Use @parameterized.expand as a decorator to parametrize the test with a couple
of org examples to pass to GithubOrgClient, in this order:
    * google
    * abc
Of course, no external HTTP calls should be made.
"""
import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Test suite for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json', return_value="example.com")
    def test_org(self, org, get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        org_client = GithubOrgClient(org)
        self.assertEqual(org_client.org, get_json.return_value)
        get_json.assert_called_once()


if __name__ == "__main__":
    unittest.main()
