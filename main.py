from flask import Flask, render_template,request, session, redirect,url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment 
from datetime import datetime
from records import Info

app = Flask(__name__)
app.config['SECRET_KEY'] = "hbfuq781347n34fn574n1ct8945ytyc7ty"

bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/' ,methods = ['POST', 'GET'])
def hello():
    form = Info()
    name = "Unkonwn"
    std_number = None
    Course = None
    if form.validate_on_submit():
    	session['name'] = form.name.data
    	session['std_number'] = form.std_number.data
    	session['Course'] = form.Course.data
    	return redirect(url_for('hello'))
    return render_template('records_view.html', current_time = datetime.utcnow(), form = form, name = session.get('name'), std_number = session.get('std_number'), Course= session.get('Course'))

@app.route('/gett')
def gett():
	return '<p> So i love chinese food </p>'

@app.route('/profile/<name>')
def profile(name):
	return render_template("welcome.html", name = name, current_time = datetime.utcnow())

@app.route('/post/<int:age>')
def show_age(age):
	return "My age is %s" % age
@app.route('/mode')
def viewer():
	agent = request.headers.get('User_Agent')
	return "<h1> your user agent is: %s <h1> " % agent

if __name__ == '__main__':
	app.run(debug = True)