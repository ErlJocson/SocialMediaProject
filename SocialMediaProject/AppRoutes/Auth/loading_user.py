from flask_login import UserMixin
from ...Database.manage_users import get_db_connection
from SocialMediaProject import login_manager

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