import json

class JsonExtractor:
    @staticmethod
    def extract_valid_json(input_str, batch_mode=False):
        decoder = json.JSONDecoder()
        results = []
        i = 0
        length = len(input_str)

        while i < length:
            if input_str[i] == '{' or input_str[i] == '[':
                try:
                    json_obj, end_index = decoder.raw_decode(input_str, i)
                except ValueError:
                    i += 1
                    continue

                if batch_mode:
                    results.append(json_obj)
                else:
                    return json_obj

                i = end_index
            else:
                i += 1

        # If no valid JSON found
        return None
