from flask import Flask,render_template
#app is the flask class object
#__name__ represents the current module
#route function used to naviagte from one function to another function
# update the data whenever change occurs in the file.automatically updated on browser
'''host="127.0.0.12",debug=True,port=True'''
app=Flask(__name__)
'''
@app.route('/home')
#variables with app routing

def index():
    return "<h1> WELCOME TO PYTHON tulasi</h1>"
@app.route('/index1/<name>')
def index1(name):
    return "<h1> THIS IS SONU </h1>" +name
@app.route('/integer/<int:age>')
def integer(age):
    return "THIS IS INTEGER %d" %age
@app.route('/floatvalue/<float:marks>')
def float(marks):
    return "this is float %f" %float
index1("sonu")




#function mapping

def student():
    return "This is student page"
def admin():
    return "this is admin page"
@app.route('/user/<name>')
def home(name):
    if name== 'admin':
        return admin()
    else:
        if name == 'student':
            return student()
'''


@app.route('/login/<int:name>')
def login(name):
    return render_template('login1.html',n=name)
if __name__== '__main__':
    app.run(debug=True)
	


	

