from ... import app
from ...Database import manage_post, manage_users, manage_comments
from flask_login import login_required
from flask import render_template

@app.route('/admin/users')
@login_required
def users_table():
    users = manage_users.get_all_users()
    return render_template(
        'Admin/admin_users.html',
        title="Users",
        users=users
    )

@app.route('/admin/posts')
@login_required
def users_posts():
    posts = manage_post.get_posts()
    return render_template(
        'Admin/admin_posts.html',
        title='Posts',
        posts=posts
    )

@app.route('/admin/comments')
@login_required
def users_comments():
    comments = manage_comments.get_all_comments()
    return render_template(
        'Admin/admin_comments.html',
        title="Comments",
        comments=comments
    )
