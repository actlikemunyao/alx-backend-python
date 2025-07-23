#!/usr/bin/env python3
"""
Unittests for access_nested_map
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map
class TestAccessNestedMap(unittest.TestCase):
    """Test cases for utils.access_nested_map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test valid nested paths"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])#!/usr/bin/env python3
"""
Unit tests for utils.get_json
"""
import unittest
from unittest.mock import patch, Mock
from utils import get_json
from parameterized import parameterized


class TestGetJson(unittest.TestCase):
    """Test cases for get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Test get_json returns correct payload from mocked requests.get"""
        with patch("utils.requests.get") as mock_get:
            # Configure the mock
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            # Call the function
            result = get_json(test_url)

            # Assert the correct behavior
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)

    def test_access_nested_map_exception(self, nested_map, path):
        """Test exceptions on invalid paths"""
        with self.assertRaises(KeyError) as ctx:
            access_nested_map(nested_map, path)
        self.assertEqual(str(ctx.exception), repr(path[-1]))
        @parameterized.expand([
    ("http://example.com", {"payload": True}),
    ("http://holberton.io", {"payload": False}),
])
def test_get_json(self, test_url, test_payload):

 - [Got]
1

(2 chars long)

[Expected]
0

(2 chars long)
