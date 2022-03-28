from app import myapp_obj
from flask import render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class LoginForm(FlaskForm):
	city = StringField('City Name')
	submit = SubmitField('Submit')

@myapp_obj.route('/', methods=['GET','POST'])
def home():
	city = None
	name="jimbo"
	city_names=["Paris","London","Rome","Tahiti"]
	form=LoginForm()
	if form.validate_on_submit():
		city=form.city.data
		form.city.data=''
	return render_template('home.html',name=name,city_names=city_names,form=form,city=city)

