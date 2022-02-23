from ...Database import manage_post, manage_users, manage_comments
from flask_login import login_required
from flask import render_template, Blueprint

admin = Blueprint('admin', __name__)

@admin.route('/users')
@login_required
def users_table():
    users = manage_users.get_all_users()
    return render_template(
        'Admin/admin_users.html',
        title="Users",
        users=users
    )

@admin.route('/posts')
@login_required
def users_posts():
    posts = manage_post.admin_get_posts()
    return render_template(
        'Admin/admin_posts.html',
        title='Posts',
        posts=posts
    )

@admin.route('/comments')
@login_required
def users_comments():
    comments = manage_comments.get_all_comments()
    return render_template(
        'Admin/admin_comments.html',
        title="Comments",
        comments=comments
    )
