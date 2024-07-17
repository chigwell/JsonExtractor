import ujson as json

class JsonExtractor:
    @staticmethod
    def extract_valid_json(input_str):
        stack = []
        start_index = None

        for i, char in enumerate(input_str):
            if char in '{[':
                stack.append(char)
                if len(stack) == 1:
                    start_index = i
            elif char in '}]':
                if stack and ((char == '}' and stack[-1] == '{') or (char == ']' and stack[-1] == '[')):
                    stack.pop()
                    if not stack and start_index is not None:
                        try:
                            return json.loads(input_str[start_index:i + 1])
                        except json.JSONDecodeError:
                            start_index = None

        return None
