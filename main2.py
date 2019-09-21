from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)
@app.route('/upload')
def upload():
	return render_template('upload.html')

@app.route('/success',methods=['POST','GET'])
def success():
	if request.method== 'POST':
		f=request.files['image']
		f.save(f.filename)
		return render_template('success.html',name=f.filename)
	else:
		return "please check code"

if __name__== '__main__':
    app.run(debug=True)