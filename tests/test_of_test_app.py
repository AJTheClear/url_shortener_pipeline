# import pytest
# import os
# from app import app


# @pytest.fixture
# def client():
#     app.config['TESTING'] = True
#     app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
#         'GITHUB_ACTION_DATABASE_URL',
#         # "postgresql://jason2:jason2@localhost:5432/test_url_shortener"
#         "pp"
#         )

#     with app.app_context():
#         yield app.test_client()


# def test_example(client):
#     assert app.config['TESTING'] is True
#     assert app.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get(
#         'GITHUB_ACTION_DATABASE_URL'
#         )
#     assert app.config['SQLALCHEMY_DATABASE_URI'] != (
#         "postgresql://jason2:jason2@localhost:5432/test_url_shortener"
#         )


# def test_stats_page(client):
#     """Test statistics page"""
#     assert app.config['TESTING'] is True
#     assert app.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get(
#         'GITHUB_ACTION_DATABASE_URL'
#         )
#     assert app.config['SQLALCHEMY_DATABASE_URI'] != (
#         "postgresql://jason2:jason2@localhost:5432/test_url_shortener"
#         )
#     rv = client.get('/stats')
#     assert rv.status_code == 200
#     assert b'URLShortener Statistics' in rv.data
