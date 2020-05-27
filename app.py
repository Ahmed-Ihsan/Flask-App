from flask import Flask , render_template , redirect ,url_for , request
from flask_sqlalchemy import SQLAlchemy
from models import *


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] =False 
db = SQLAlchemy(app)

@app.route('/')
def login():
	return render_template('page1.html')

@app.route('/app' , methods =['POST','GET'])
def login2():
  try:
  	name_f=request.form['name']
  	passWord=request.form['Password']
  	try:
  		Ch=User.query.filter_by(name=name_f).first()
  		if Ch.password == passWord:
  			data_=data.query.all()
  			return render_template('page3.html',data1=data_)
  		else:
  			return render_template('page1.html', error_login="The Password Error")
  	except Exception as e :
  			print(e)
  			return render_template('page1.html', error_login="Something Error")
  except Exception as e:
  	print(e)
  	data_=data.query.all()
  	return render_template('page3.html',data1=data_)
  	

@app.route('/add' , methods =['POST','GET'])
def Add():
	return render_template('page2.html')

@app.route('/add_' , methods =['POST','GET'])
def Add2():
	name_=request.form['name']
	Note_=request.form['note']
	n_n=request.form['it_n']
	it_=request.form['it_m']
	try:
		add=data(name=name_ , Note=Note_ , item_n=n_n ,item_hm=it_)
		db.session.add(add)
		db.create_all()
		db.session.commit()
		return render_template('page2.html')
	except Exception as e:
 		print(e)
 		return render_template('page2.html',error="error")
	
@app.route('/dataf' , methods =['POST','GET'])
def data_f():
	try:
		search_=request.form['Search']
		Ch=data.query.filter_by(name=search_).first()
		return render_template('page4.html',data2=Ch)
	except Exception as e:
		print(e)
		data_=data.query.all()
		return render_template('page3.html',data1=data_)


@app.route('/all' , methods =['POST','GET'])
def all():
	data_=data.query.all()
	return render_template('page5.html',data3=data_)

if __name__ == '__main__': 
	app.run(debug = True) 	 