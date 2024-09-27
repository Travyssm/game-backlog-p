from flask import render_template
from gamebacklog import app, db
from gamebacklog.models import Genre, Game

@app.route("/")
def home():
    return render_template("base.html")