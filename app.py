from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('static/index.html')

@app.route("/pravidla/")
def homepage():
    return render_template('static/index.html')

@app.route("/")
def homepage():
    return render_template('static/index.html')

@app.route("/")
def homepage():
    return render_template('static/index.html')