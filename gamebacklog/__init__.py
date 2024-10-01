import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

from gamebacklog.models import User

@login_manager.user_loader
def load_user(uid):
    return User.query.get(uid)

bcrypt = Bcrypt(app)


from gamebacklog import routes