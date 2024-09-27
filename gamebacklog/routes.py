from flask import render_template, request, redirect, url_for
from gamebacklog import app, db
from gamebacklog.models import Genre, Game

@app.route("/")
def home():
    return render_template("games.html")


@app.route("/genres")
def genres():
    genres = list(Genre.query.order_by(Genre.genre_name).all())
    return render_template("genres.html", genres=genres)

@app.route("/add_genre", methods=["GET", "POST"])
def add_genre():
    if request.method == "POST":
        genre = Genre(genre_name=request.form.get("genre_name"))
        db.session.add(genre)
        db.session.commit()
        return redirect(url_for("genres"))
    return render_template("add_genre.html")
