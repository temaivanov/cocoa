from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/signup')
def signup():
    return '<p>signup form</p>'

@auth.route('/login')
def login():
    return '<p>login form</p>'

@auth.route('/logout')
def logout():
    return '<p>logout button</p>'