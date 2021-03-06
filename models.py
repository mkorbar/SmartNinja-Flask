import os
from sqla_wrapper import SQLAlchemy

# this connects to a database either on Heroku or on localhost
db = SQLAlchemy(os.getenv("DATABASE_URL", "sqlite:///localhost.sqlite"))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    secret_number = db.Column(db.Integer)
    passwd = db.Column(db.String)
    session_token = db.Column(db.String)
