from flask import render_template
from SocialMediaProject import app
from flask_login import login_required
from .PostForm import *

@app.route('/', methods=["GET", "POST"])
@login_required
def index():
    post_form = PostForm()
    return render_template(
        'index.html',
        title="Home",
        post_form=post_form
    )