
import requests

class StatusCodeError(Exception):
    """
    If a `Requests` status code is unexpected, raise this error.
    """
    pass

class BaseConnector():

    headers = {
        'Content-Type': 'application/json'
    }

    def _get(self, url: str, headers: dict = None, raw_response: bool = False, **kwargs):

        if headers is not None:
            self.headers.update(headers)
        
        response = requests.get(url=url, headers=headers, **kwargs)

        if response.status_code != 200:
            raise StatusCodeError('Was not able to get user information.')

        return response if raw_response else response.json() 



class GitHubConnector(BaseConnector):
    github_repo_list_url = 'https://api.github.com/users/santosderek/repos?page={number}'
    github_user_url = 'https://api.github.com/users/santosderek'

    @property
    def user(self):
        try:
            return self._get(self.github_user_url)
        except StatusCodeError:
            return {}

