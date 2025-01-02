from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import random
import string

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    original_url = db.Column(db.String, nullable=False)
    short_url = db.Column(db.String, unique=True, nullable=False)

def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route('/', methods=['POST', 'GET'])
def index():
    short_url = None
    if request.method == 'POST':
        original_url = request.form['url']
        
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
            
    return render_template('index.html', short_url=short_url)

@app.route('/<short_url>')
def redirect_to_url(short_url):
    # Намираме URL обекта по краткия URL
    url_object = URL.query.filter_by(short_url=short_url).first_or_404()
    
    # Пренасочваме към оригиналния URL
    return redirect(url_object.original_url)

if __name__ == "__main__":
    app.run(debug=True)