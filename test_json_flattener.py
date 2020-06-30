import unittest
from unittest import TestCase

from json_flattener import JsonFlattener


class TestJsonFlattener(TestCase):

    def setUp(self):
        self.json_flattener = JsonFlattener()

    def test_flatten_input_none_returns_none(self):
        # call
        result = self.json_flattener.flatten(None)

        # assert
        self.assertEqual(result, None)

    def test_flatten_input_empty_dict_returns_empty_dict(self):
        # call
        result = self.json_flattener.flatten({})

        # assert
        self.assertEqual(result, {})

    def test_flatten_input_contains_empty_dict_value_treated_as_terminal_value(self):
        # setup
        test_json_dict = {'a': 1, 'b': True, 'c': {}}
        expected_result = {'a': 1, 'b': True, 'c': {}}

        # call
        result = self.json_flattener.flatten(test_json_dict)

        # assert
        self.assertEqual(result, expected_result)

    def test_flatten_input_populated_dict_returns_flattened_dict(self):
        # setup
        test_json_dict = {'a': 1, 'b': True, 'c': {'d': 3, 'e': 'test'}}
        expected_result = {'a': 1, 'b': True, 'c.d': 3, 'c.e': 'test'}

        # call
        result = self.json_flattener.flatten(test_json_dict)

        # assert
        self.assertEqual(result, expected_result)

    def test_flatten_input_multi_level_populated_dict_returns_flattened_dict(self):
        # setup
        test_json_dict = {'a': 1, 'b': True, 'c': {'d': {'k': 7, 'g': 'hello'}, 'e': 'test'}}
        expected_result = {'a': 1, 'b': True, 'c.d.k': 7, 'c.d.g': 'hello', 'c.e': 'test'}

        # call
        result = self.json_flattener.flatten(test_json_dict)

        # assert
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
