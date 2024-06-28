#!/usr/bin/env python3
"""
Write the first unit test for utils.access_nested_map.
Create a TestAccessNestedMap class that inherits from unittest.TestCase.
Implement the TestAccessNestedMap.test_access_nested_map method to test that
the method returns what it is supposed to.
Decorate the method with @parameterized.expand to test the function for
following inputs:
nested_map={"a": 1}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a", "b")
For each of these inputs, test with assertEqual that the function returns the
expected result.
The body of the test method should not be longer than 2 lines.
"""
import unittest
from utils import access_nested_map, get_json
from parameterized import parameterized
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """
    Unit tests for the access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test that access_nested_map return the expected result for given inputs
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b'),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        Test that access_nested_map raises the expected exception for
        given inputs.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(context.exception))


class TestGetJson(unittest.TestCase):
    """
    Unit tests for the get_json function.
    """
    @patch('requests.get')
    def test_get_json(self, mock_get):
        """
        Test that get_json returns the expected result.
        Mocks the requests.get method to return a test_payload.
        Verifies that the function correctly handles different URLs.
        """
        test_payload = {"payload": True}
        mock_get.return_value.json.return_value = test_payload

        urls = ["http://example.com", "http://holberton.io"]
        for url in urls:
            result = get_json(url)
            self.assertEqual(result, test_payload)
            mock_get.assert_called_with(url)


if __name__ == "__main__":
    unittest.main()
