#making the website folder a python package by adding the __init__.py into the directory
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    from .auth import auth
    from .views import views

    #indicate the entry point to each blueprint
    app.register_blueprint(auth, url_prefix = '/auth')
    app.register_blueprint(views, url_prefix = '/')


    return app