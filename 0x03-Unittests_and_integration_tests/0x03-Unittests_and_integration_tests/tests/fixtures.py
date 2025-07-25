#!/usr/bin/env python3
"""Fixtures module"""

TEST_PAYLOAD = (
    {"repos_url": "https://api.github.com/orgs/test/repos"},
    [{"name": "repo1", "license": {"key": "apache-2.0"}},
     {"name": "repo2", "license": {"key": "bsd-3-clause"}}]
)
