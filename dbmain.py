from flask import Flask,redirect,url_for,render_template,request,flash
from flask_mail import Mail,Message
from random import randint
from db import Register,Base,User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_login import LoginManager,current_user,login_user,logout_user,login_required



app = Flask(__name__)
app.secret_key='sa'
engine=create_engine('sqlite:///register.db',connect_args={'check_same_thread':False},echo=True)
Base.metadata.bind=engine
DBsession=sessionmaker(bind=engine)
session=DBsession()


login_manager = LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'

@login_manager.user_loader
def load_user(user_id):
	return session.query(User).get(int(user_id))


@app.route('/show')
def showData():
	register1=session.query(Register).all()
	return render_template('show.html',reg=register1)
	
	
@app.route('/add',methods=['POST','GET'])	
def addData():
	if request.method == 'POST':
		newData=Register(name=request.form['name'],email=request.form['email'],des=request.form['des'])
		session.add(newData)
		session.commit()
		flash("New data is added")
		return redirect(url_for('showData'))
	else:
		return render_template('add.html')

@app.route('/edit/<int:register_id>',methods=['POST','GET'])	
def editData(register_id):
	editeddata=session.query(Register).filter_by(id=register_id).one()
	if request.method == 'POST':
		editeddata.id=request.form['id']
		editeddata.name=request.form['name']
		editeddata.email=request.form['email']
		editeddata.des=request.form['des']
		session.add(editeddata)
		session.commit()
		flash("New data is updated Succesfully")
		return redirect(url_for('showData'))
	else:
		return render_template('edit.html',register=editeddata)
		
@app.route('/delete/<int:register_id>',methods=['POST','GET'])		
def deleteData(register_id):
	deleteddata=session.query(Register).filter_by(id=register_id).one()
	if request.method == 'POST':
		session.delete(deleteddata)
		session.commit()
		flash("data is deleted succesfully")
		return redirect(url_for('showData'))
	else:
		return render_template('delete.html',register=deleteddata)

@app.route('/register',methods=['POST','GET'])
def registerData():
	if request.method == 'POST':
		regdata=User(name=request.form['name'])
		email=request.form['email']
		password=request.form['password']
		session.add(regdata)
		session.commit()
		return redirect(url_for('index'))
	else:
		return render_template('register.html')
		
@app.route('/index',methods=['POST','GET'])
def index():
	return render_template('index.html')
		

@app.route('/login',methods=['POST','GET'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('showData'))
	try:
		if request.method=='POST':
			user=session.query(User).filter_by(
				email=request.form['email'],
				password=request.form['password']).first()
			if user:
				login_user(user)
				return redirect(url_for('showData'))
			else:
			    flash('Login failed')
		else:
			return render_template('login.html')
	except Exception as e:
		flash("login failed")
	else:
		return render_template('login.html')
			
@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

if __name__=='__main__':
	app.run(debug=True)
	
	
	