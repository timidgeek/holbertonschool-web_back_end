#!/usr/bin/env python3
"""
utils unit tests
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


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
