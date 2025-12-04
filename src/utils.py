import json

def safe_parse_json(s: str):
    try:
        return json.loads(s)
    except Exception as e:
        print(f"JSON parsing error: {e}")
        return None