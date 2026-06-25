from website import create_app
from website.resume import RESUME_FILENAME


def test_spa_routes_return_503_when_frontend_build_is_missing(tmp_path):
    app = create_app({
        'TESTING': True,
        'GENERATE_RESUME_ON_STARTUP': False,
        'RESUME_LOCATION': str(tmp_path / 'resume' / RESUME_FILENAME),
        'SPA_DIST_DIR': str(tmp_path / 'missing-spa'),
    })

    with app.test_client() as client:
        returned_value = client.get('/')

    assert returned_value.status_code == 503
