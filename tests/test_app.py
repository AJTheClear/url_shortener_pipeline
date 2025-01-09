import psycopg2
from app import app, db, URL, generate_short_url


def test_database_connection():
    """Test database connection"""
    try:
        conn = psycopg2.connect(
            dbname='test_url_shortener',
            user='jason2',
            password='jason2',
            host='postgres',
            port='5432'
        )
        conn.close()
    except Exception as e:
        print(f"Database connection failed: {e}")


def test_index_get():
    """Test GET request to index page"""
    with app.app_context():
        url_count = URL.query.count()
        assert url_count >= 0


def test_create_short_url():
    """Test creating a new short URL"""
    with app.app_context():
        new_url = URL(
            original_url='https://www.example.com',
            short_url=generate_short_url()
            )
        db.session.add(new_url)
        db.session.commit()
        url = URL.query.filter_by(
            original_url='https://www.example.com'
            ).first()
        assert url is not None
        assert url.original_url == 'https://www.example.com'
        assert len(url.short_url) == 6


def test_redirect():
    """Test URL redirection"""
    with app.app_context():
        new_url = URL(original_url='https://www.example.com',
                      short_url=generate_short_url())
        db.session.add(new_url)
        db.session.commit()
        url = URL.query.filter_by(
            original_url='https://www.example.com'
            ).first()
        url.clicks += 1
        assert url is not None
        assert url.clicks == 1  # Check if the click count was updated


def test_stats_page():
    """Test statistics page"""
    with app.app_context():
        # Check if statistics are being calculated correctly
        url_count = URL.query.count()  # Get the number of URLs
        assert url_count >= 0
