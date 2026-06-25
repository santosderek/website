from pathlib import Path

import pytest
import requests

from website import create_app
from website.resume import RESUME_FILENAME


@pytest.fixture
def app(tmp_path, monkeypatch):
    def block_network(*args, **kwargs):
        raise requests.RequestException("Network access is disabled in tests")

    monkeypatch.setattr('website.connectors.github.requests.get', block_network)

    resume_location = tmp_path / 'resume' / RESUME_FILENAME
    app = create_app({
        'TESTING': True,
        'GENERATE_RESUME_ON_STARTUP': False,
        'RESUME_LOCATION': str(resume_location),
        'GITHUB_TIMEOUT_SECONDS': 0.01,
    })

    return app


@pytest.fixture
def client(app):
    with app.test_client() as client:
        with app.app_context():
            yield client
