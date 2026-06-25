from pathlib import Path

from website.resume import generate_document


def test_robots(client):
    returned_value = client.get('/robots.txt')

    robots_file = Path(__file__).resolve().parents[1] / 'website/static/txt/robots.txt'
    assert robots_file.exists()
    with robots_file.open('r', encoding='utf-8') as current_file:
        assert returned_value.data.decode('utf-8') == current_file.read()


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


def test_home_serves_react_app_shell(client):
    """Testing that the home route serves the React app shell."""
    returned_value = client.get('/')

    assert returned_value.status_code == 200
    assert 'React App Shell' in returned_value.data.decode('utf-8')


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


def test_project_page_renders(client):
    returned_value = client.get('/project/project')
    assert returned_value.status_code == 200
    assert 'React App Shell' in returned_value.data.decode('utf-8')


def test_santosderek_projects(client):
    returned_value = client.get('/project/santosderek')
    assert returned_value.status_code == 200
    assert 'React App Shell' in returned_value.data.decode('utf-8')


def test_vitality_projects(client):
    returned_value = client.get('/project/vitality')
    assert returned_value.status_code == 200
    assert 'React App Shell' in returned_value.data.decode('utf-8')


def test_project_not_found(client):
    returned_value = client.get('/project/noproject')
    assert returned_value.status_code == 404
    assert 'Sorry! Could not find page!' in returned_value.data.decode('utf-8')


def test_project_traversal_not_found(client):
    returned_value = client.get('/project/..%2Fbase')
    assert returned_value.status_code == 404
