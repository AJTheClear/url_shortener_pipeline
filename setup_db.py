from app import app, db
from flask import Flask
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
url = 'sqlite:///' + os.path.join(basedir, 'instance', 'urls.db')
app.config['SQLALCHEMY_DATABASE_URI'] = url

with app.app_context():
    db.create_all()