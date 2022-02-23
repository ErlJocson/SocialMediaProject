from flask import Flask
from flask_login import LoginManager

app = Flask(__name__, template_folder="templates", static_folder="static")

app.config['SECRET_KEY'] = 'secret_key'
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = "Please login to access the page."
login_manager.login_message_category = 'success'

from .AppRoutes import Main, Auth, Admin
app.register_blueprint(Main.main, url_prefix='/')
app.register_blueprint(Admin.admin, url_prefix='/admin')
app.register_blueprint(Auth.auth, url_prefix='/authentication')