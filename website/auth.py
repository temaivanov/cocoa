from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

#here we get do define what methods each endpoint can process. By default, they all can only process GET.
@auth.route('/signup')
def signup():
    return render_template("signup.html")

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return '<p>logout button</p>'