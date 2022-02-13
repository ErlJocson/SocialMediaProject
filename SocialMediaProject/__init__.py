from flask import Flask
from flask_admin import Admin
from flask_login import LoginManager
from flask_login import UserMixin
from .Database.manage import get_db_connection

app = Flask(__name__, template_folder="templates", static_folder="static")
admin = Admin(app, name='Social Media', template_mode='bootstrap3')

app.config['SECRET_KEY'] = 'secret_key'
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = "Please login to access the page."
login_manager.login_message_category = 'success'

class User(UserMixin):
    def __init__(self, id, first_name, last_name, middle_name, email, password):
         self.id = id
         self.first_name = first_name
         self.last_name = last_name
         self.middle_name = middle_name
         self.email = email
         self.password = password
         self.authenticated = False

    def is_active(self):
         return self.is_active()

    def is_anonymous(self):
         return False

    def is_authenticated(self):
         return self.authenticated

    def is_active(self):
         return True

    def get_id(self):
         return self.id

@login_manager.user_loader
def load_user(user_id):
   conn = get_db_connection()
   curs = conn.cursor()
   curs.execute("SELECT * FROM users WHERE id=?",[user_id])
   user = curs.fetchone()
   if user is None:
      return None
   else:
      return User(user[0], user[1], user[2], user[3], user[4], user[5])

from .AppRoutes import Main, Auth, Posting