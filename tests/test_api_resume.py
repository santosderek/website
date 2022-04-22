from ._shared import client


def test_api_resume(client):
    returned_value = client.get('/api/v1/resume')
    returned_value_json = returned_value.json

    assert len(returned_value_json) > 0
    assert 'career' in returned_value_json
    assert 'education' in returned_value_json
    assert 'leadership' in returned_value_json
    assert 'repos' in returned_value_json
    assert 'skills' in returned_value_json

    assert returned_value_json['career'] is not None
    assert returned_value_json['education'] is not None
    assert returned_value_json['leadership'] is not None
    assert returned_value_json['repos'] is not None
    assert returned_value_json['skills'] is not None


def test_api_career(client):
    returned_value = client.get('/api/v1/career')
    returned_value_json = returned_value.json

    assert returned_value_json is not None
    assert isinstance(returned_value_json, list)
    assert len(returned_value_json) > 0


def test_api_education(client):
    returned_value = client.get('/api/v1/education')
    returned_value_json = returned_value.json

    assert returned_value_json is not None
    assert isinstance(returned_value_json, list)
    assert len(returned_value_json) > 0


def test_api_leadership(client):
    returned_value = client.get('/api/v1/leadership')
    returned_value_json = returned_value.json

    assert returned_value_json is not None
    assert isinstance(returned_value_json, list)
    assert len(returned_value_json) > 0


def test_api_repos(client):
    returned_value = client.get('/api/v1/repos')
    returned_value_json = returned_value.json

    assert returned_value_json is not None
    assert isinstance(returned_value_json, list)
    assert len(returned_value_json) > 0


def test_api_skills(client):
    returned_value = client.get('/api/v1/skills')
    returned_value_json = returned_value.json

    assert returned_value_json is not None
    assert isinstance(returned_value_json, dict)
    assert len(returned_value_json) > 0
