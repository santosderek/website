import json

def get_resource_json(filename: str):
    "Return the contents of a resource JSON file."
    with open(f'website/resources/{filename}', 'r') as current_file:
        return json.loads(current_file.read())