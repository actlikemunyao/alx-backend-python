#!/usr/bin/env python3
"""Unit and Integration tests for client.py"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD

class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    def test_org(self, org_name):
        with patch("client.get_json") as mock_get_json:
            url = f"https://api.github.com/orgs/{org_name}"
            client = GithubOrgClient(org_name)
            client.org()
            mock_get_json.assert_called_once_with(url)

    def test_public_repos_url(self):
        with patch("client.GithubOrgClient.org", new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "https://api.github.com/orgs/test/repos"}
            client = GithubOrgClient("test")
            self.assertEqual(client._public_repos_url, "https://api.github.com/orgs/test/repos")

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        mock_get_json.return_value = [{"name": "repo1"}, {"name": "repo2"}]
        with patch("client.GithubOrgClient._public_repos_url", new_callable=PropertyMock) as mock_url:
            mock_url.return_value = "mocked_url"
            client = GithubOrgClient("test")
            self.assertEqual(client.public_repos(), ["repo1", "repo2"])
            mock_get_json.assert_called_once_with("mocked_url")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        self.assertEqual(GithubOrgClient.has_license(repo, license_key), expected)

@parameterized_class([
    {"org_payload": TEST_PAYLOAD[0],
     "repos_payload": TEST_PAYLOAD[1],
     "expected_repos": ["repo1", "repo2"],
     "apache2_repos": ["repo1"]}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests"""

    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch("requests.get")
        mock_get = cls.get_patcher.start()
        mock_get.side_effect = [
            unittest.mock.Mock(**{"json.return_value": cls.org_payload}),
            unittest.mock.Mock(**{"json.return_value": cls.repos_payload}),
        ]

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def test_public_repos(self):
        client = GithubOrgClient("test")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        client = GithubOrgClient("test")
        self.assertEqual(client.public_repos("apache-2.0"), self.apache2_repos)
