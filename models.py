from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] =False 
db = SQLAlchemy(app)

__tablename__= "data_base"
class data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False, nullable=False)
    Note= db.Column(db.String, unique=False, nullable=True)
    item_n = db.Column(db.Integer, unique=False, nullable=False)
    item_hm = db.Column(db.Integer, unique=False, nullable=False)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, unique=True, nullable=False)
	password = db.Column(db.String, unique=True, nullable=False)

if __name__ == '__main__':
	Review_add=User(name='password' , password='name')
	db.session.add(Review_add)
	db.create_all()
	db.session.commit()
