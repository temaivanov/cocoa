#making the website folder a python package by adding the __init__.py into the directory
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#create a new database

db = SQLAlchemy()
DB_NAME = "artemdb.db"

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///aretmdb.db'
    db.init_app(app)

    from .auth import auth
    from .views import views

    #indicate the entry point to each blueprint
    app.register_blueprint(auth, url_prefix = '/auth')
    app.register_blueprint(views, url_prefix = '/')


    return app