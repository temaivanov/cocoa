#this database model will be using the data structured that I created to store notes
#this is how all notes and users should look like
from website import db
from flask_login import UserMixin

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(100000))
    date = db.Column(db.DateTime(timezone = True), default =func.now())
    #how do we associate a note to a user? we would need a connection between notes and users
    user_id = db.Coulmn(db.Integer, db.ForeignKey('user.id')) #user is an object of User class

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') #when we do a relathionship in SQLAlchemy, we reference the name of the class
