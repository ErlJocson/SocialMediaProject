from flask import render_template, request, flash, redirect, url_for
from ... import app
from .AuthForms import *
from SocialMediaProject.Database.manage import *

@app.route('/login', methods=["POST", "GET"])
def login():
    login_form = LoginForm()
    if request.method == "POST":
        email = login_form.email.data
        password = login_form.password.data
        # check if user exist
    return render_template(
        'Authentication/login.html',
        title='Login',
        login_form=login_form
    )

@app.route('/register', methods=["POST", "GET"])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        email = register_form.email.data
        first_name = register_form.first_name.data
        middle_name = register_form.middle_name.data
        last_name = register_form.last_name.data
        password = register_form.password.data
        confirm_password = register_form.confirm_password.data
        
        if check_if_email_exist(email):
            flash("Email is already used!", "danger")
            return render_template(
                'Authentication/register.html',
                title="Register",
                register_form=register_form
            )

        if password != confirm_password:
            flash('Passwords does not match!', 'danger')
            return render_template(
                'Authentication/register.html',
                title="Register",
                register_form=register_form
            )
        
        adding_new_users(
            {
                "email":email,
                "first_name":first_name,
                "middle_name":middle_name,
                "last_name":last_name,
                "password":password
            }
        )
        # login the new user
        return redirect(url_for('index'))
    return render_template(
        'Authentication/register.html',
        title="Register",
        register_form=register_form
    )