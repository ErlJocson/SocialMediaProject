from flask import render_template, request, flash, redirect, url_for
from SocialMediaProject import app
from flask_login import login_required, current_user
from .PostForm import *
from ...Database.manage_post import *
import datetime

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