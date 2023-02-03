from flask import Flask
from flask import render_template
from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/pravidla/")
def pravidla():
    return render_template('pravidla.html')

@app.route("/postavy")
def postavy():
    return render_template('postavy.html')

@app.route("/realiesveta")
def svet():
    return render_template('svet.html')

@app.route("/probehleakce")
def probehle():
    return render_template('probehle.html')

@app.route("/fotogalerie")
def foto():
    return render_template('fotogalerie.html')

@app.route("/navody")
def navody():
    return render_template('navody.html')

@app.route("/pristiakce")
def pristi():
    return render_template('pristi.html')


app.run(debug=True)