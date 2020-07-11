import pytest

from flaskr import create_app


@pytest.fixture
def app():
    app = create_app('dev')
    return app
