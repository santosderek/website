import json
import requests

GITHUB_REPO_LIST_URL = 'https://api.github.com/users/santosderek/repos?page={number}'
GITHUB_USER_URL = 'https://api.github.com/users/santosderek'


class GithubRequestError(Exception):
    pass


def get_github_user():
    """Requests from the GITHUB API my user data and returns as JSON(Dict)"""
    returned_value = requests.get(GITHUB_USER_URL)

    if returned_value.status_code != 200:
        raise GithubRequestError("Error Code != 200")

    return returned_value.json()


def get_resource_json(filename: str):
    "Return the contents of a resource JSON file."
    with open(f'website/resources/{filename}', 'r') as current_file:
        data = json.loads(current_file.read())
        return data