import pathlib
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
BASEDIR = pathlib.Path(__file__).parent


class Config:
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{BASEDIR / 'db.sqlite3'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "$%^&*kjh$%^&*&TYJ"


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
api = Api(app)
