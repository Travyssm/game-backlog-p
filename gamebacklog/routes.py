from flask import render_template, request, redirect, url_for, session
from flask_login import login_user, logout_user, current_user, login_required
from gamebacklog import app, db, bcrypt
from gamebacklog.models import Genre, Game, User

@app.route("/")
def home():
    if current_user.is_authenticated:
        return render_template("dashboard.html")
    else:
        return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("signup.html")
    elif request.method == "POST":
        existing_user = User.query.filter(
            User.username == request.form.get("username").lower()).all()

        if existing_user:
            return redirect(url_for("register"), error="User already here!")


        username = request.form.get("username")
        password = request.form.get("password")

        pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(username=username, password=pw_hash)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for("home"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()

        if bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("home"))
        else:
            return render_template("login.html")

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route("/games")
def games():
    games = list(Game.query.order_by(Game.id).all())
    return render_template("games.html", games=games)

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

@app.route("/edit_game/<int:game_id>", methods=["GET", "POST"])
def edit_game(game_id):
    game = Game.query.get_or_404(game_id)
    genres = list(Genre.query.order_by(Genre.genre_name).all())
    if request.method == "POST":
        game.game_name = request.form.get("game_name")
        game.game_description = request.form.get("game_description")
        game.is_favourite = bool(True if request.form.get("is_favourite") else False)
        game.release_date = request.form.get("release_date")
        game.genre_id = request.form.get("genre_id")
        db.session.commit()
    return render_template("edit_game.html", game=game, genres=genres)

@app.route("/delete_game/<int:game_id>")
def delete_game(game_id):
    game = Game.query.get_or_404(game_id)
    db.session.delete(game)
    db.session.commit()
    return redirect(url_for("games"))