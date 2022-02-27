from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from ...Database.manage_users import *
from ...Database.manage_post import *
from ...Database.manage_follows import *

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

@user.route('/follow-list')
@login_required
def follow():
    all_users = get_all_users()
    following = get_following(current_user.id)
    followers = get_followers(current_user.id)

    for user in all_users:
        if user[:3] in following or user[:3] in followers:
            all_users.remove(user)

    return render_template(
        "Profile/follow.html",
        title='Friends',
        all_users=all_users,
        following=following,
        followers=followers
    )

@user.route('/follow-user/<other_user>')
@login_required
def follow_user(other_user):
    follow_a_user(current_user.id, other_user)
    flash('Added to following!', 'success')
    return redirect(url_for('user.follow'))

@user.route('/unfollow-user/<other_user>')
@login_required
def unfollow_user(other_user):
    unfollow_a_user(current_user.id, other_user)
    flash("Removed from following!", 'success')
    return redirect(url_for('user.follow'))