def assert_json_response(response):
    assert response.status_code == 200
    assert response.is_json
    assert response.content_type.startswith('application/json')


def test_api_resume(client):
    returned_value = client.get('/api/v1/resume')
    assert_json_response(returned_value)
    returned_value_json = returned_value.json

    assert set(returned_value_json) == {'career', 'education', 'leadership', 'repos', 'skills'}
    assert isinstance(returned_value_json['career'], list)
    assert isinstance(returned_value_json['education'], list)
    assert isinstance(returned_value_json['leadership'], list)
    assert isinstance(returned_value_json['repos'], list)
    assert isinstance(returned_value_json['skills'], dict)

    assert returned_value_json['career'] is not None
    assert returned_value_json['education'] is not None
    assert returned_value_json['leadership'] is not None
    assert returned_value_json['repos'] is not None
    assert returned_value_json['skills'] is not None


def test_api_career(client):
    returned_value = client.get('/api/v1/career')
    assert_json_response(returned_value)
    returned_value_json = returned_value.json

    assert returned_value_json is not None
    assert isinstance(returned_value_json, list)
    assert len(returned_value_json) > 0


def test_api_education(client):
    returned_value = client.get('/api/v1/education')
    assert_json_response(returned_value)
    returned_value_json = returned_value.json

    assert returned_value_json is not None
    assert isinstance(returned_value_json, list)
    assert len(returned_value_json) > 0


def test_api_leadership(client):
    returned_value = client.get('/api/v1/leadership')
    assert_json_response(returned_value)
    returned_value_json = returned_value.json

    assert returned_value_json is not None
    assert isinstance(returned_value_json, list)
    assert len(returned_value_json) > 0


def test_api_repos(client):
    returned_value = client.get('/api/v1/repos')
    assert_json_response(returned_value)
    returned_value_json = returned_value.json

    assert returned_value_json is not None
    assert isinstance(returned_value_json, list)
    assert len(returned_value_json) > 0


def test_api_skills(client):
    returned_value = client.get('/api/v1/skills')
    assert_json_response(returned_value)
    returned_value_json = returned_value.json

    assert returned_value_json is not None
    assert isinstance(returned_value_json, dict)
    assert len(returned_value_json) > 0


def test_api_github_user_falls_back_when_network_is_unavailable(client):
    returned_value = client.get('/api/v1/github/user')
    assert_json_response(returned_value)

    assert returned_value.json == {}
