#!/usr/bin/env python3
"""
utils unit tests
"""
from unittest import TestCase, mock, unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    checks return of method `Nested Map`
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_path, path, expected):
        """ test nested map access """
        self.assertEqual(access_nested_map(nested_path, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_path, path):
        """ test exception """
        with self.assertRaises(KeyError):
            access_nested_map(nested_path, path)


class TestGetJson(unittest.TestCase):
    """
    testing getting json function
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """
        test json method
        """
        mock = Mock()
        mock.json.return_value = payload
        with patch("requests.get", return_value=mock):
            self.assertEqual(get_json(url), payload)
            mock.json.assert_called_once()


class TestMemoize(TestCase):
    """ Class for testing memoization """

    def test_memoize(self):
        """ Tests memoize function """

        class TestClass:
            """ Test class """

            def a_method(self):
                """ Method to always return 42 """
                return 42

            @memoize
            def a_property(self):
                """ Returns memoized property """
                return self.a_method()

        test_class = TestClass()
        with patch.object(test_class, 'a_method') as mock:
            mock.return_value = 42

            test_class.a_property
            test_class.a_property
            mock.assert_called_once()


if __name__ == '__main__':
    unittest.main()
