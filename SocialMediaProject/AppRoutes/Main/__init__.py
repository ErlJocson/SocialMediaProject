from flask import render_template, request, flash, redirect, url_for
from SocialMediaProject import app
from flask_login import login_required, current_user
from .PostForm import *
from ...Database.manage_post import *
from ...Database.manage_users import check_if_email_exist


@app.route('/', methods=["GET", "POST"])
@login_required
def index():
    post_form = PostForm()
    posts = get_posts()

    if request.method == "POST":
        content = post_form.content.data
        add_post(
            {
                "content":content,
                "user_id":current_user.id
            }
        )
        flash('New post uploaded!', 'success')
        return redirect(url_for('index'))

    return render_template(
        'index.html',
        title="Home",
        post_form=post_form,
        posts=posts
    )

@app.route('/details')
@login_required
def details():
    details = check_if_email_exist(current_user.email)
    return render_template(
        'account_details.html',
        title='Account',
        details=details
    )

@app.route('/add_likes/<post_id>', methods=["POST"])
@login_required
def add_likes(post_id):
    if request.method == "POST":
        add_a_like(post_id)
    return {'msg':True}