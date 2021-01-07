from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField ,validators , PasswordField ,TextAreaField

#creating a class for wtforms 
class SignupForm(FlaskForm):
    username=StringField("Username:",[validators.InputRequired()])
    password=PasswordField("new password:",[validators.DataRequired()])
    submit=SubmitField("create contact")

#creating a class for login 
class LoginForm(FlaskForm):
    username=StringField("Username:", [validators.InputRequired()])
    password=PasswordField("password",[validators.InputRequired()])
    submit=SubmitField("login")

#create a class for editng information
class Edit(FlaskForm):
    first_name=StringField("First name : ",[validators.InputRequired()])
    last_name=StringField("Last_name:",[validators.InputRequired()])
    biography=TextAreaField("Biography",[validators.InputRequired()])
    edit=SubmitField("Edit user")

#creating a class for changing the password
class ChangePassword(FlaskForm):
    current_password=PasswordField("curent password:",[validators.InputRequired()])
    new_password = PasswordField('New Password', [validators.InputRequired(), validators.EqualTo('confirm', message='Passwords must match')])
    confirm  = PasswordField('Repeat Password')

class AddPostForm(FlaskForm):
    title=StringField("post title:",[validators.InputRequired()])
    body=TextAreaField("post body",[validators.InputRequired()])
    submit=SubmitField("post")
