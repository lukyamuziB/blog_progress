import os
from flask import Flask, render_template,request, session, redirect,url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment 
from datetime import datetime
from records import Info
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = "hbfuq781347n34fn574n1ct8945ytyc7ty"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite///" + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/' , methods = ['GET','POST'])
def hello():
    form = Info()
    name = "Unkonwn"
    std_number = None
    Course = None
    if form.validate_on_submit():
    	name = form.name.data
    	std_number = form.std_number.data
    	Course = form.Course.data
    	return redirect(url_for('hello'))
    return render_template('records_view.html', current_time = datetime.utcnow(), form = form, name = name, std_number =std_number, Course= Course)

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

@app.route('/database')
def databases():
	pass


if __name__ == '__main__':
	app.run(debug = True)