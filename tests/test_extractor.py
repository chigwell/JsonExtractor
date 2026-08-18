import json
import unittest
from json_extractor.extractor import JsonExtractor

class TestJsonExtractor(unittest.TestCase):
    def generate_recursive_json(self, depth):
        if depth == 0:
            return {}
        return {"key": self.generate_recursive_json(depth - 1)}

    def test_extract_valid_json(self):
        recursive_json = self.generate_recursive_json(10)
        recursive_json_str = "dfssf"+json.dumps(recursive_json)
        test_cases = [
            ('Response: some text\n {"resp": "valid"} and some text', {"resp": "valid"}),
            ('``` {"key": "value"} ```', {"key": "value"}),
            ('```json\n {"json": "object"} \n```', {"json": "object"}),
            ('```json\n '
             '{"json": "string1\\nstring2"} \n```', {"json": "string1\nstring2"}),
            ('```code {} ```', {}),
            ('``` {} ``` dfsf', {}),
            ('fsdfs fdfsd \n gdfgd fgf ``` {} ``` dfsf'
             'fdsdf ', {}),
            ('some invalid response', None),
            (recursive_json_str, recursive_json),
            ("""
            ```json
            {
                "json": "object"
            }
            ```
            """, {"json": "object"}),
            ('```json[\n {"key": "value1"}, {"key": "value2"} \n]```',
             [{"key": "value1"}, {"key": "value2"}]),
            ('Some text\n```json[\n{"json": "object1"},\n{"json": "object2"}\n]``` more text',
             [{"json": "object1"}, {"json": "object2"}]),
            ('Array with nested objects\n```json[\n {"key": {"nested_key": "nested_value"}}, {"key": "value2"} \n]```',
             [{"key": {"nested_key": "nested_value"}}, {"key": "value2"}]),
        ]

        for input_str, expected in test_cases:
            result = JsonExtractor.extract_valid_json(input_str)
            self.assertEqual(result, expected, f"Failed for input: {input_str}")

    def test_extract_valid_json_batch_mode(self):
        batch_test_cases = [
            ('Text {"a":1} text [{"b":2}, 3]', [{"a": 1}, [{"b": 2}, 3]]),
            ('{"a":1}{"b":2}', [{"a": 1}, {"b": 2}]),
            ('No JSON here', []),
            ('Some text {"x": "y"} and more {"z": 1}', [{"x": "y"}, {"z": 1}]),
            ('``` {"key": "value"} ``` {"key2": "value2"}', [{"key": "value"}, {"key2": "value2"}]),
            ('one {"a": 1} two {"b": 2} three {"c": 3}', [{"a": 1}, {"b": 2}, {"c": 3}]),
            ('[{"a": 1}, {"b": 2}]', [[{"a": 1}, {"b": 2}]]),
        ]
        for input_str, expected in batch_test_cases:
            result = JsonExtractor.extract_valid_json(input_str, batch_mode=True)
            self.assertEqual(result, expected, f"Failed for input: {input_str}")

    def test_extract_valid_json_default_ignores_batch(self):
        input_str = 'Text {"a":1} text {"b":2}'
        self.assertEqual(JsonExtractor.extract_valid_json(input_str), {"a": 1})
        self.assertEqual(
            JsonExtractor.extract_valid_json(input_str, batch_mode=False),
            {"a": 1}
        )

    def test_extract_valid_json_large_batch_input(self):
        input_str = 'log ' * 2000 + '{"a": 1}' + 'mid ' * 2000 + '{"b": 2}'
        self.assertGreater(len(input_str), 10000)
        result = JsonExtractor.extract_valid_json(input_str, batch_mode=True)
        self.assertEqual(result, [{"a": 1}, {"b": 2}])

if __name__ == '__main__':
    unittest.main()
