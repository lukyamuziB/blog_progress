from flask import flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/gett')
def gett():
	return '<p> So i love chinese food </p>'

@app.route('/profile/<name>')
def profile(name):
	return render_template("welcome.html", name = name)

@app.route('/post/<int:age>')
def show_age(age):
	return "My age is %s" % age

if __name__ == '__main__':
	app.run(debug = True)