from app import app, db

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/urls.db'  # Ensure this is set

with app.app_context():  # Create an application context
    db.create_all()  # Create all tables
