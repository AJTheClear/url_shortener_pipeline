import pytest
from app import app, db, URL

@pytest.fixture
def client():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['TESTING'] = True
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        
        with app.app_context():
            db.drop_all()

def test_index_get(client):
    """Test GET request to index page"""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Welcome to URLShortener' in rv.data

def test_create_short_url(client):
    """Test creating a new short URL"""
    data = {'url': 'https://www.example.com'}
    rv = client.post('/', data=data)
    assert rv.status_code == 200
    
    with app.app_context():
        url = URL.query.filter_by(original_url='https://www.example.com').first()
        assert url is not None
        assert url.original_url == 'https://www.example.com'
        assert len(url.short_url) == 6

def test_duplicate_url(client):
    """Test creating same URL twice"""
    data = {'url': 'https://www.example.com'}
    
    # First submission
    rv1 = client.post('/', data=data)
    with app.app_context():
        url1 = URL.query.filter_by(original_url='https://www.example.com').first()
    
    # Second submission
    rv2 = client.post('/', data=data)
    with app.app_context():
        url2 = URL.query.filter_by(original_url='https://www.example.com').first()
    
    assert url1.short_url == url2.short_url

def test_redirect(client):
    """Test URL redirection"""
    with app.app_context():
        # First create a URL
        data = {'url': 'https://www.example.com'}
        client.post('/', data=data)
        
        # Get the URL object
        url = URL.query.filter_by(original_url='https://www.example.com').first()
        
        # Test redirection
        rv = client.get(f'/{url.short_url}')
        assert rv.status_code == 302
        assert rv.headers['Location'] == 'https://www.example.com'
        
        # Test click counter
        url = URL.query.filter_by(original_url='https://www.example.com').first()
        assert url.clicks == 1

def test_stats_page(client):
    """Test statistics page"""
    rv = client.get('/stats')
    assert rv.status_code == 200
    assert b'URLShortener Statistics' in rv.data
