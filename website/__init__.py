#making the 'website' folder a python package by adding the __init__.py into the directory
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

#create == innitiate ==  a new database

db = SQLAlchemy()
DB_NAME = "artem2.db"

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    #app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///artem1.db"

    db.init_app(app)

    from .auth import auth
    from .views import views

    #indicate the entry point to each blueprint
    app.register_blueprint(auth, url_prefix = '/auth')
    app.register_blueprint(views, url_prefix = '/')

    from .models import User, Note
    create_database(app)

    return app

def create_database(app):
    if not os.path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print("DB CREATED")