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
        ]

        for input_str, expected in test_cases:
            result = JsonExtractor.extract_valid_json(input_str)
            self.assertEqual(result, expected, f"Failed for input: {input_str}")

if __name__ == '__main__':
    unittest.main()
