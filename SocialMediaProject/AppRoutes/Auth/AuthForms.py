from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, EqualTo

class LoginForm(FlaskForm):
    email    = EmailField('Email: ', validators=[DataRequired()])
    password = PasswordField('Password: ', validators=[DataRequired()]) 
    submit   = SubmitField('Login')

class RegisterForm(FlaskForm):
    email            = EmailField('Email: ', validators=[DataRequired()])
    first_name       =  StringField('First name: ', validators=[DataRequired()])
    middle_name      =  StringField('Middle name: ')
    last_name        =  StringField('Last name: ', validators=[DataRequired()])
    password         = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password:', validators=[DataRequired(), EqualTo('password')])
    submit           = SubmitField('Create account')