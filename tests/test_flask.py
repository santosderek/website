import pytest
from flask import request, url_for
from website import create_app
from website import get_resource_json


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    def setup():
        """ Code run after client has been used """
        teardown()

    def teardown():
        """ Code run after client has been used """
        pass

    with app.test_client() as client:
        with app.app_context():
            setup()
            yield client
            teardown()


def test_github(client):
    """Testing that the page redirects to github"""
    returned_value = client.get('/github')
    assert returned_value.status_code == 302
    assert returned_value.location == 'https://github.com/santosderek'


def test_linkedin(client):
    """Testing that the page redirects to linkedin"""
    returned_value = client.get('/linkedin')
    assert returned_value.status_code == 302
    assert returned_value.location == 'https://www.linkedin.com/in/santosderek/'


def test_home(client):
    """Testing that the page renders"""
    returned_value = client.get('/')
    assert returned_value.status_code == 200

    for client in get_resource_json('career.json'):
        assert bytes(client['title'], 'utf-8') in returned_value.data

    for education in get_resource_json('education.json'):
        assert bytes(education['title'], 'utf-8') in returned_value.data

    for repos in get_resource_json('repos.json'):
        assert bytes(repos['title'], 'utf-8') in returned_value.data

    for technology in get_resource_json('skills.json')['technologies']:
        assert bytes(technology[0], 'utf-8') in returned_value.data

    for technology in get_resource_json('skills.json')['tools']:
        assert bytes(technology[0], 'utf-8') in returned_value.data


def test_get_resource_json():
    """Testing to see if the json file gets loaded"""

    returned_value = get_resource_json('career.json')
    assert len(returned_value) > 0

    returned_value = get_resource_json('education.json')
    assert len(returned_value) > 0

    returned_value = get_resource_json('repos.json')
    assert len(returned_value) > 0

    returned_value = get_resource_json('skills.json')
    assert len(returned_value) > 0
