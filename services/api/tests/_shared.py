import pytest
from website import create_app


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
