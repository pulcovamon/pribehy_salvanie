from salvanie_package import app, db
from flask import render_template, redirect, url_for, flash
from salvanie_package.models import Character, Skill, Ancestry, Player, SkillCharacterRelationship
from salvanie_package.forms import RegisterForm, LoginForm
from flask_login import login_user, logout_user, login_required

@app.route("/")
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route("/pravidla")
def rules_page():
    return render_template('rules.html')

@app.route("/postavy")
def characters_page():
    return render_template('characters.html')

@app.route("/realiesveta")
def world_page():
    return render_template('world.html')

@app.route("/probehleakce")
def previous_page():
    return render_template('previous.html')

@app.route("/fotogalerie")
def images_page():
    return render_template('images.html')

@app.route("/navody")
def manuals_page():
    return render_template('manuals.html')

@app.route("/pristiakce")
def following_page():
    return render_template('following.html')