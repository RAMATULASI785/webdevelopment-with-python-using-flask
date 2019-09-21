from flask import Flask,redirect,url_for,render_template,request,flash
from flask_mail import Mail,Message
from random import randint

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='kovvuriramatulasi@gmail.com'
app.config['MAIL_PASSWORD']='HARITHA123'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True



mail=Mail(app)
otp =randint(000000,999999)
app.secret_key='ss'

@app.route('/email')
def email():
	return render_template('email.html')
	
@app.route('/email_verify',methods=['POST','GET'])
def email_verify():
	email= request.form['mail']
	msg = Message('OTP FOR VERIFICATION',sender='kovvuriramatulasi@gmail.com',recipients=[email])
	msg.body=str(otp)
	mail.send(msg)
	return render_template('verify.html')
	
@app.route('/validation',methods=['POST','GET'])
def validation():
	user_otp = request.form['otpvalue']
	if otp == int(user_otp):
		return "OTP VERIFICATION IS DONE"
	else:
		return "Invalid otp"
if __name__=='__main__':
	app.run(debug=True)