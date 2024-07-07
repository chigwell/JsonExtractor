import json

class JsonExtractor:
    @staticmethod
    def extract_valid_json(input_str):
        stack = []
        start_index = None

        for i, char in enumerate(input_str):
            if char == '{' or char == '[':
                stack.append(char)
                if len(stack) == 1:
                    # Mark the start of a potential JSON object or array
                    start_index = i
            elif char == '}' or char == ']':
                if stack:
                    if (char == '}' and stack[-1] == '{') or (char == ']' and stack[-1] == '['):
                        stack.pop()
                    if len(stack) == 0 and start_index is not None:
                        # Attempt to parse when we find a closing brace or bracket that matches the outermost opening brace or bracket
                        try:
                            json_obj = json.loads(input_str[start_index:i + 1])
                            return json_obj  # Return the first successfully parsed JSON object or array
                        except json.JSONDecodeError:
                            # Reset start_index if parsing fails
                            start_index = None

        # If no valid JSON found
        return None
