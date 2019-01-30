from flask import Flask,abort,redirect,url_for,request,render_template

app = Flask(__name__)

@app.route('/',methods=['GET'])
@app.route('/index/',methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/interest/',methods=['GET'])
def interest():
    return render_template('interest.html')

@app.route('/animation/',methods=['GET'])
def animation():
    return render_template('animation.html')

@app.errorhandler(404)
def not_found(error):
	return render_template('error.html')
	

# cookie session

if __name__ == '__main__':
	app.run(port=80, host='0.0.0.0', debug=True)
