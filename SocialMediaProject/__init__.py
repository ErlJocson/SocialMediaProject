from flask import Flask
from flask_admin import Admin
from flask_login import LoginManager

app = Flask(__name__, template_folder="template", static_folder="static")
admin = Admin(app, name='Social Media', template_mode='bootstrap3')

app.config['SECRET_KEY'] = 'secret_key'
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = "Please login to access the page."
login_manager.login_message_category = 'success'

from .AppRoutes import Main, Auth, Posting