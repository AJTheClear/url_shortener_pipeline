from app import app, db

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/urls.db'

with app.app_context():
    db.create_all()
