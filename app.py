from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
import random
import string

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/urls.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    original_url = db.Column(db.String, nullable=False)
    short_url = db.Column(db.String, unique=True, nullable=False)

def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        original_url = request.form['url']
        
        existing_url = URL.query.filter_by(original_url=original_url).first()
        if existing_url:
            short_url = f"http://127.0.0.1:5000/{existing_url.short_url}"
            return render_template('index.html', short_url=short_url)
        
        new_url = URL(
            original_url=original_url,
            short_url=generate_short_url()
        )
        
        try:
            db.session.add(new_url)
            db.session.commit()
            short_url = f"http://127.0.0.1:5000/{new_url.short_url}"
            return render_template('index.html', short_url=short_url)
        except:
            db.session.rollback()
            return "Възникна грешка при добавянето на URL"
            
    return render_template('index.html')

@app.route('/<short_url>')
def redirect_to_url(short_url):
    url_object = URL.query.filter_by(short_url=short_url).first_or_404()
    
    return redirect(url_object.original_url)

@app.route('/stats')
def stats():
    urls = URL.query.all()
    return render_template('stats.html', urls=urls)

if __name__ == "__main__":
    app.run(debug=True)