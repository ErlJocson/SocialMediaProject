from flask import render_template, request, flash, redirect, url_for
from ... import app, load_user
from .AuthForms import *
from SocialMediaProject.Database.manage import *
from flask_login import login_user, logout_user

@app.route('/login', methods=["POST", "GET"])
def login():
    login_form = LoginForm()
    if request.method == "POST":
        email = login_form.email.data
        password = login_form.password.data
        user_to_login = check_if_email_exist(email)

        if not user_to_login:
            flash('Email does not exist!', 'danger')
            return redirect(url_for('login'))

        if not user_to_login[-1] == password:
            flash('Wrong password!', 'danger')
            return redirect(url_for('login'))

        login_user(load_user(user_to_login[0]))
        flash(f'Welcome back {user_to_login[1]}!', 'success')
        return redirect(url_for('index'))

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
            return redirect(url_for('register'))

        if password != confirm_password:
            flash('Passwords does not match!', 'danger')
            return redirect(url_for('register'))
        
        new_user_id = adding_new_users(
            {
                "email":email,
                "first_name":first_name,
                "middle_name":middle_name,
                "last_name":last_name,
                "password":password
            }
        )

        login_user(load_user(new_user_id))
        flash(f'Welcome {first_name}!', 'success')
        return redirect(url_for('index'))

    return render_template(
        'Authentication/register.html',
        title="Register",
        register_form=register_form
    )

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))