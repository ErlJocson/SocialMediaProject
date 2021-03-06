from flask import render_template, request, flash, redirect, url_for, Blueprint
from flask_login import login_required, current_user
from .PostForm import *
from ...Database.manage_post import *
from ...Database.manage_users import *
from ...Database.manage_comments import *

main = Blueprint('main', __name__)

@main.route('/', methods=["GET", "POST"])
@login_required
def index():
    post_form = PostForm()
    posts = []
    for post in get_posts():
        posts.append(post + get_likes(post[0]))
    
    if request.method == "POST":
        content = post_form.content.data
        add_post(
            {
                "content":content,
                "user_id":current_user.id
            }
        )
        flash('New post uploaded!', 'success')
        return redirect(url_for('main.index'))
        
    return render_template(
        'index.html',
        title="Home",
        post_form=post_form,
        posts=posts
    )

@main.route('/post/<int:post_id>', methods=['GET', 'POST'])
@login_required
def post(post_id):
    comment_form = CommentForm()
    current_post = get_post_by_id(post_id)
    comments = get_all_comments()
    if request.method == "POST":
        content = comment_form.content.data
        add_a_comment(
            {
                "post_id":post_id,
                "user_id":current_user.id,
                "content":content,
            }
        )
        flash('New comment added!', 'success')
        return redirect(url_for("main.post", post_id=post_id))
    return render_template(
        'post.html',
        title='Post',
        current_post = current_post,
        comment_form = comment_form,
        comments = comments
    )

@main.route('/add-like/<post_id>')
@login_required
def like_post(post_id):
    if check_if_already_liked(post_id, current_user.id):
        add_a_like(current_user.id, post_id)
        flash('Post liked!', 'success')
        return redirect(url_for('main.index'))
    remove_like(post_id, current_user.id)
    flash('You removed the like!', 'danger')
    return redirect(url_for('main.index'))

@main.route('/delete-post/<post_id>')
@login_required
def delete_post(post_id):
    remove_post(post_id)
    flash('Post deleted!', 'success')
    return redirect(url_for('user.profile'))

@main.route('/delete-comment/<comment_id>')
@login_required
def delete_comment(comment_id):
    delete_user_comment(comment_id)
    flash('Comment deleted!', 'success')
    return redirect(url_for('main.index'))