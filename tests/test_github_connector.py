import pytest
import requests

from website.connectors.github import BaseConnector, GitHubConnector, StatusCodeError


class FakeResponse:
    def __init__(self, status_code=200, payload=None, json_error=None):
        self.status_code = status_code
        self.payload = payload if payload is not None else {}
        self.json_error = json_error

    def json(self):
        if self.json_error:
            raise self.json_error
        return self.payload


def test_base_connector_merges_headers_and_uses_configured_timeout(app, monkeypatch):
    captured = {}

    def fake_get(**kwargs):
        captured.update(kwargs)
        return FakeResponse(payload={'ok': True})

    monkeypatch.setattr('website.connectors.github.requests.get', fake_get)

    with app.app_context():
        returned_value = BaseConnector()._get('https://example.test', headers={'X-Test': '1'})

    assert returned_value == {'ok': True}
    assert captured['url'] == 'https://example.test'
    assert captured['headers'] == {
        'Content-Type': 'application/json',
        'X-Test': '1',
    }
    assert captured['timeout'] == app.config['GITHUB_TIMEOUT_SECONDS']
    assert BaseConnector.default_headers == {'Content-Type': 'application/json'}


def test_base_connector_raises_for_non_200(monkeypatch):
    monkeypatch.setattr(
        'website.connectors.github.requests.get',
        lambda **kwargs: FakeResponse(status_code=500, payload={'message': 'error'}),
    )

    with pytest.raises(StatusCodeError):
        BaseConnector()._get('https://example.test')


def test_github_user_returns_payload_on_success(monkeypatch):
    monkeypatch.setattr(
        'website.connectors.github.requests.get',
        lambda **kwargs: FakeResponse(payload={'login': 'santosderek'}),
    )

    assert GitHubConnector().user == {'login': 'santosderek'}


@pytest.mark.parametrize(
    'fake_get',
    [
        lambda **kwargs: FakeResponse(status_code=404),
        lambda **kwargs: (_ for _ in ()).throw(requests.Timeout('slow')),
        lambda **kwargs: FakeResponse(json_error=ValueError('bad json')),
    ],
)
def test_github_user_returns_empty_dict_on_failure(monkeypatch, fake_get):
    monkeypatch.setattr('website.connectors.github.requests.get', fake_get)

    assert GitHubConnector().user == {}
