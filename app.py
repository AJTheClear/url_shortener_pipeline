from Flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is the beginning of a flask app'