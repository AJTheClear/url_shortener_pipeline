import pytest
import os
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'GITHUB_ACTION_DATABASE_URL',
        "postgresql://jason2:jason2@localhost:5432/test_url_shortener"
        )

    with app.app_context():
        yield app.test_client()


def test_example(client):
    assert app.config['TESTING'] is True
    assert app.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get(
        'GITHUB_ACTION_DATABASE_URL'
        )
