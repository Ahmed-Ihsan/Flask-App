from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] =False 

db = SQLAlchemy(app)
'''
ch1=data.query.all()

for ch in ch1:
print(ch.name,ch.Note , ch.item_n ,ch.item_hm)'''
search_="test"
ch1=data.query.filter_by(name=search_).all()
for ch in ch1:
	print(ch.name,ch.Note , ch.item_n ,ch.item_hm)
