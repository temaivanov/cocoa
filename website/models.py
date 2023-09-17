#this database model will be using the data structure that I created to store notes
#this is how all notes and users should look like
#e.g. all of my notes and user will have to conform to the rules below

#import from the website folder, from the __init__ file
from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    #how do we associate a note to a user? we would need a connection between notes and users
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #user is an object of User class

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') #when we do a relathionship in SQLAlchemy, we reference the name of the class
