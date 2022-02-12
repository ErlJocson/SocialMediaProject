from flask import Flask
from flask_admin import Admin

app = Flask(__name__, template_folder="template", static_folder="static")
admin = Admin(app, name='Social Media', template_mode='bootstrap3')

app.config['SECRET_KEY'] = 'secret_key'
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

from .AppRoutes import Main, Auth, Posting