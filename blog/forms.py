from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField ,validators , PasswordField ,TextAreaField

#creating a class for wtforms 
class SignupForm(FlaskForm):
    username=StringField("Username:",[validators.InputRequired()])
    password=PasswordField("Password:",[validators.InputRequired()])
    submit=SubmitField("create contact")

#creating a class for login 
class LoginForm(FlaskForm):
    username=StringField("Username:", [validators.InputRequired()])
    password=PasswordField("password",[validators.InputRequired()])
    submit=SubmitField("login")

#create a class for editng information


#creating a class for changing the password
class ChangePasswordForm(FlaskForm):
    old_password=PasswordField("old password : "[validators.InputRequired()])
    new_password=PasswordField("new password:",[validators.DataRequired(),validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    submit= SubmitField("change password")


class AddPostForm(FlaskForm):
    title=StringField("post title:",[validators.InputRequired()])
    body=TextAreaField("post body",[validators.InputRequired()])
    submit=SubmitField("post")
