#!/usr/bin/env python3
"""
Unittests for access_nested_map
"test_url="http://example.com", test_payload={"payload": True}
test_url="http://holberton.io", test_payload={"payload": False}""
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
#!/usr/bin/env python3
"""
Unit tests for utils module
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test valid access"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test access that raises KeyError"""
        with self.assertRaises(KeyError) as ctx:
            access_nested_map(nested_map, path)
        self.assertEqual(str(ctx.exception), repr(path[-1]))


class TestGetJson(unittest.TestCase):
    """Test get_json"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Mock requests.get to test get_json"""
        with patch("utils.requests.get") as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            result = get_json(test_url)
 - [Got]
1

(2 chars long)

[Expected]
0

(2 chars long)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)
 -  - [Got]
IndentationError: unexpected unindent

(38 chars long)

[Expected]
OK

(3 chars long) - [Got]
IndentationError: unexpected unindent

(38 chars long)

[Expected]
OK

(3 chars long) - [Got]
IndentationError: unexpected unindent

(38 chars long)

[Expected]
OK

(3 chars long) - [Got]
IndentationError: unexpected unindent

(38 chars long)

[Expected]
OK

(3 chars long)

 - [Got]
1

(2 chars long)

[Expected]
0

(2 chars long)
