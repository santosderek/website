import requests
from flask import current_app, has_app_context

from website.settings import GITHUB_TIMEOUT_SECONDS


class StatusCodeError(Exception):
    """
    If a `Requests` status code is unexpected, raise this error.
    """
    pass


class BaseConnector:
    default_headers = {
        'Content-Type': 'application/json'
    }

    @staticmethod
    def _timeout():
        if has_app_context():
            return current_app.config.get('GITHUB_TIMEOUT_SECONDS', GITHUB_TIMEOUT_SECONDS)
        return GITHUB_TIMEOUT_SECONDS

    def _get(self, url: str, headers: dict = None, raw_response: bool = False, **kwargs):
        request_headers = {**self.default_headers, **(headers or {})}
        kwargs.setdefault('timeout', self._timeout())

        response = requests.get(url=url, headers=request_headers, **kwargs)

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
        except (StatusCodeError, requests.RequestException, ValueError):
            return {}
