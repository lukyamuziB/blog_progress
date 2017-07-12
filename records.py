from flask_wtf import Form 
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class Info(Form):
	name = StringField("input stuudent's name", validators = [Required()])
	std_number = StringField("Input Student Course", validators = [Required()])
	Course = StringField("input Course", validators = [Required()])
	submit = SubmitField('submit')

