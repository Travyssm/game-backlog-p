import os
from flask import Flask, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

from gamebacklog.models import User

@login_manager.user_loader
def load_user(uid):
    return User.query.get(uid)

@login_manager.unauthorized_handler
def unauthorized_callback():
    flash("Login required to visit dashboard!")
    return redirect(url_for("home"))

bcrypt = Bcrypt(app)


from gamebacklog import routes