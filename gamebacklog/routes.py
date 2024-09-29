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


@app.route("/edit_genre/<int:genre_id>", methods=["GET", "POST"])
def edit_genre(genre_id):
    genre = Genre.query.get_or_404(genre_id)
    if request.method == "POST":
        genre.genre_name = request.form.get("genre_name")
        db.session.commit()
        return redirect(url_for("genres"))
    return render_template("edit_genre.html", genre=genre)


@app.route("/delete_genre/<int:genre_id>")
def delete_genre(genre_id):
    genre = Genre.query.get_or_404(genre_id)
    db.session.delete(genre)
    db.session.commit()
    return redirect(url_for("genres"))


@app.route("/add_game", methods=["GET", "POST"])
def add_game():
    genres = list(Genre.query.order_by(Genre.genre_name).all())
    if request.method == "POST":
        game = Game(
        game_name=request.form.get("game_name"),
        game_description=request.form.get("game_description"),
        is_favourite=bool(True if request.form.get("is_favourite") else False),
        release_date=request.form.get("release_date"),
        genre_id=request.form.get("genre_id")
        )
        db.session.add(game)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_game.html", genres=genres)