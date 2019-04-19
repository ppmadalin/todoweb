"""
views.py

Contains all the views related to user app
"""
from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import url_for
from werkzeug.security import generate_password_hash

from application import db
from user.models import User
from user.forms import RegisterForm


user_app = Blueprint('user_app', __name__)


@user_app.route('/register', methods=('GET', 'POST'))
def register():
    """
    Register page
    """
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = User(
            form.full_name.data,
            form.email.data,
            hashed_password,
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.login'))
    return render_template('user/register.html', form=form)


@user_app.route('/login')
def login():
    """
    Login page
    """
    return '<h1>Login</h1>'


@user_app.route('/logout')
def logout():
    """
    Logout page
    """
    return '<h1>Logout</h1>'
