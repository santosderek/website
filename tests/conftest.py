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
    spa_dist_dir = tmp_path / 'spa'
    spa_dist_dir.mkdir()
    (spa_dist_dir / 'index.html').write_text(
        '<!doctype html><html><head><title>Derek Santos</title></head>'
        '<body><div id="root">React App Shell</div></body></html>',
        encoding='utf-8',
    )

    app = create_app({
        'TESTING': True,
        'GENERATE_RESUME_ON_STARTUP': False,
        'RESUME_LOCATION': str(resume_location),
        'GITHUB_TIMEOUT_SECONDS': 0.01,
        'SPA_DIST_DIR': str(spa_dist_dir),
    })

    return app


@pytest.fixture
def client(app):
    with app.test_client() as client:
        with app.app_context():
            yield client
