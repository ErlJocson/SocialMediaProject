from flask import render_template, request, flash
from ... import app
from .AuthForms import *

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

        if password != confirm_password:
            flash('Passwords does not match!')
            return render_template(
                'Authentication/register.html',
                title="Register",
                register_form=register_form
            )
        
        # add a validation for email
        # then add the new user
    return render_template(
        'Authentication/register.html',
        title="Register",
        register_form=register_form
    )