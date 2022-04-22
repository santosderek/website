from os.path import exists

from website import create_app
from website.connectors.github import GitHubConnector
from website.resources import get_resource_json
from website.resume import RESUME_LOCATION

from ._shared import client


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
        assert bytes(repos['url'], 'utf-8') in returned_value.data

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


def test_get_github_user():
    """Tests whether my github user data can be retrieved"""

    returned_value = GitHubConnector().user
    assert returned_value['login'] == 'santosderek'


def test_resume_created(client):
    """Tests to check weather the application created the resume during creation."""

    # Client application gets generated as a pytest fixture
    assert exists(RESUME_LOCATION)


def test_vitality_projects(client):
    returned_value = client.get('/project/vitality')
    assert returned_value.status_code == 200
    assert b'Create, search, and view' in returned_value.data
    assert b'Youtube recommendations' in returned_value.data
    assert b'Schedule meetings' in returned_value.data
    assert b'Google Maps' in returned_value.data
    assert b'Invite and connect' in returned_value.data
    assert b'Features' in returned_value.data
    assert b'free and centralized' in returned_value.data
    assert b'Mission' in returned_value.data
    assert b'Vitality' in returned_value.data


def test_project_not_found(client):
    returned_value = client.get('/project/noproject')
    assert returned_value.status_code == 404
    assert b'Sorry! Could not find page!' in returned_value.data
