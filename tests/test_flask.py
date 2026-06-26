from website.resume import generate_document


def test_resume_download(client, app):
    generate_document(app.config['RESUME_LOCATION'])

    returned_value = client.get('/resume')

    assert returned_value.status_code == 200
    assert returned_value.content_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    assert 'attachment' in returned_value.headers['Content-Disposition']
    assert app.config['RESUME_FILENAME'] in returned_value.headers['Content-Disposition']


def test_resume_missing_returns_404(client):
    returned_value = client.get('/resume')

    assert returned_value.status_code == 404
    assert 'Sorry! Could not find page!' in returned_value.data.decode('utf-8')


def test_frontend_routes_are_not_served_by_api_backend(client):
    assert client.get('/').status_code == 404
    assert client.get('/project/vitality').status_code == 404
    assert client.get('/github').status_code == 404
    assert client.get('/linkedin').status_code == 404
    assert client.get('/robots.txt').status_code == 404
