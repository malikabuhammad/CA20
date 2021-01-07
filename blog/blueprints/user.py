import sqlite3
from flask import Blueprint, render_template, request, redirect
from blog.db import get_db
from ..forms import SignupForm,ChangePassword,Edit

# define our blueprint
user_bp = Blueprint('user', __name__)


@user_bp.route('/add/user', methods=['GET', 'POST'])
def add_user():

    #create an instance of the form
    signup_form=SignupForm()
    #  add user blueprint
    
    if signup_form.validate_on_submit():
        #read the username from the form 
        username=signup_form.username.data

        password=signup_form.password.data
        # get the DB connection
        db = get_db()

        # insert user into DB
        try:
            print(f"trying to add {username}:{password}")
            # execute our insert SQL statement
            db.execute("INSERT INTO user (username, password) VALUES (?, ?);", (username, password))

            # write changes to DB
            db.commit()
            
            return redirect("/users")

        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            return redirect("/404")
    return render_template('user/index.html',form=signup_form)
@user_bp.route('/change', methods=['GET', 'POST'])
def change_password():
    #create inctence form changepasword class
    change_password=ChangePassword()
    if change_password.validate_on_submit():
        current_password=change_password.old_password.data
        new_password=change_password.new_password.data
        # get the DB conection
        db=get_db()


@user_bp.route('/edit/user', methods=['GET', 'POST'])
@login_required
def edit_user():
    #creating an instance
    edit=Edit()
    if edit.validate_on_submit():
        first_name=edit.first_name.data
        last_name=edit.last_name.data
        bio=edit.biography.data
        
        db=get_db()

        try:
            db.execute("INSERT INTO user (first_name,last_name,biography) VALUES (?, ?,?);", (first_name, last_name,biography))




@user_bp.route('/users')
def get_users():
    # get the DB connection
    db = get_db()

    # get all users from the db
    users = db.execute('select * from user').fetchall()

    # render 'list.html' blueprint with users
    return render_template('user/list.html', users=users)
