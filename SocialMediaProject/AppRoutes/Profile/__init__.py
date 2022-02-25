from flask import Blueprint, render_template
from flask_login import login_required, current_user
from ...Database.manage_users import *
from ...Database.manage_post import *

user = Blueprint('user', __name__)

@user.route('/')
@login_required
def profile():
    details = check_if_email_exist(current_user.email)
    posts = get_user_post(current_user.id)
    return render_template(
        'Profile/profile.html',
        title='Account',
        details=details,
        posts = posts
    )

@user.route('/friend-list')
@login_required
def friend_list():
    return render_template(
        "Profile/friends.html",
        title='Friends'
    )