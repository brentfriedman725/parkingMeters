from flask import Flask
from flask import Flask, session, request, redirect
from dotenv import load_dotenv
load_dotenv()
import os
import psycopg2

app = Flask(__name__)
from routes import openSpots
app.config['SECRET_KEY'] = os.urandom(64)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = './.flask_session/'





@app.route('/')
def index():
    return f'<h2><a>Home</a></h2>'



app.run(port=8080, debug=False, threaded=True)
