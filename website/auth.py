from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

#here we get do define what methods each endpoint can process. By default, they all can only process GET.
@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #here I introduced the flash messages from flask. Here =flash= is just an intention, and this conent will not go eve into the console.
        #to render the text of a notifiaction, describe the template and conditions of a notification in the base HTML
        if len(email) < 7:
            flash('Email address must contain at least 7 characters', category = 'error')
        elif len(firstName) < 1:
            flash('The firstname should be at least one character', category = 'error')
        elif len(password1) < 5:
            flash('Password length should be at least 5 characters', category = 'error')    
        elif password1 != password2:
            flash('Passwords do not match' , category = 'error')
        else: 
            flash('Success!', category = 'success')
    
    return render_template("signup.html")

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return '<p>logout button</p>'