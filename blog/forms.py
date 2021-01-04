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

#create a class for editng information
class EditForm(FlaskForm):
    first_name=StringField("First name :",[validators.InputRequired()])
    last_name=StringField("Last name :", [validators.InputRequired()])
    biography=TextAreaField("Biography :")
    edit = SubmitField("Edit")

#creating a class for changing the password
class ChangePasswordForm(FlaskForm):
    old_password=PasswordField("old password : "[validators.InputRequired()])
    new_password=PasswordField("new password:" [validators.InputRequired()])
    submit= SubmitField("change password")


class AddPostForm(FlaskForm):
    title=StringField("post title:",[validators.InputRequired()])
    body=TextAreaField("post body",[validators.InputRequired()])
    submit=SubmitField("post")
