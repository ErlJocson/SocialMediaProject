from flask import render_template
from ... import app
from .AuthForms import *

@app.route('/login', methods=["POST", "GET"])
def login():
    login_form = LoginForm()
    return render_template(
        'Authentication/login.html',
        title='Login',
        login_form=login_form
    )

@app.route('/register', methods=["POST", "GET"])
def register():
    register_form = RegisterForm()
    return render_template(
        'Authentication/register.html',
        title="Register",
        register_form=register_form
    )