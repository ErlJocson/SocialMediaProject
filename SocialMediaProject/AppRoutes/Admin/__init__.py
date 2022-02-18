from ... import app
from ...Database import manage_post, manage_users
from flask_login import login_required
from flask import render_template

@app.route('/admin/users')
@login_required
def users_table():
    return render_template('Admin/admin_users.html')

@app.route('/admin/posts')
@login_required
def users_posts():
    posts = manage_post.get_posts()
    print(posts)
    return render_template('Admin/admin_posts.html')

@app.route('/admin/comments')
@login_required
def users_comments():
    return render_template('Admin/admin_comments.html')
