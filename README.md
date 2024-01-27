[![PyPI version](https://badge.fury.io/py/jsonextractor.svg)](https://badge.fury.io/py/jsonextractor)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/jsonextractor)](https://pepy.tech/project/jsonextractor)

# JsonExtractor

`JsonExtractor` is a Python utility designed to extract valid JSON objects from strings. This is particularly useful for processing outputs from various sources where JSON objects may be embedded within larger text blobs.

## Installation

To install `JsonExtractor`, you can use pip:

```bash
pip install jsonextractor
```

## Usage

After installation, `JsonExtractor` can be imported and used in your Python projects to extract JSON objects from strings.

Example:

```python
from json_extractor import JsonExtractor

# Some input string that contains a JSON object
input_string = 'Some text before JSON {"key": "value"} some text after JSON.'

# Extract the valid JSON object
valid_json = JsonExtractor.extract_valid_json(input_string)

if valid_json is not None:
    print("Extracted JSON:", valid_json)
else:
    print("No valid JSON found.")
```

## Features

- Extracts the first valid JSON object found in a given string.
- Handles various formats, including JSON within markdown code blocks.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/chigwell/jsonextractor/issues).

## License

[MIT](https://choosealicense.com/licenses/mit/)
