from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField ,validators , PasswordField

#creating a class for wtforms 
class SignupForm(FlaskForm):
    username=StringField("Username:",[validators.InputRequired()])
    password=PasswordField("Password:",[validators.InputRequired()])
    submit=SubmitField("create contact")

    #creating a class for wtforms 
class LoginForm(FlaskForm):
    pass

