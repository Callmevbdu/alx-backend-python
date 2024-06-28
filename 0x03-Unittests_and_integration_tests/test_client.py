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
from unittest.mock import patch, PropertyMock, Mock
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD
import json


class TestGithubOrgClient(unittest.TestCase):
    """Test suite for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, input, mock):
        """Test that GithubOrgClient.org returns the correct value."""
        test_class = GithubOrgClient(input)
        test_class.org()
        mock.assert_called_once_with(f'https://api.github.com/orgs/{input}')

    def test_public_repos_url(self):
        """Test GithubOrgClient._public_repos_url."""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            payload = {"repos_url": "World"}
            mock.return_value = payload
            test_class = GithubOrgClient('test')
            result = test_class._public_repos_url
            self.assertEqual(result, payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """Test GithubOrgClient.public_repos."""
        json_payload = [{"name": "Google"}, {"name": "Twitter"}]
        mock_json.return_value = json_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public:

            mock_public.return_value = "hello/world"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            check = [i["name"] for i in json_payload]
            self.assertEqual(result, check)

            mock_public.assert_called_once()
            mock_json.assert_called_once()

    @patch('client.GithubOrgClient.org', return_value={})
    @patch('client.GithubOrgClient._public_repos_url', return_value="https://api.github.com/orgs/google/repos")  # noqa
    def test_has_license(self, mock_repos_url, mock_org):
        """Test GithubOrgClient.has_license."""
        org_client = GithubOrgClient("example_org")

        repo1 = {"license": {"key": "my_license"}}
        self.assertTrue(org_client.has_license(repo1, "my_license"))

        repo2 = {"license": {"key": "other_license"}}
        self.assertFalse(org_client.has_license(repo2, "my_license"))


if __name__ == "__main__":
    unittest.main()
