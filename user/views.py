"""
views.py

Contains all the views related to user app
"""
from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import url_for
from flask import request
from flask import session
from flask import flash
from werkzeug.security import generate_password_hash

from application import db
from user.models import User
from user.forms import RegisterForm
from user.forms import LoginForm


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


@user_app.route('/login', methods=('GET', 'POST'))
def login():
    """
    Login page
    """
    form = LoginForm()
    error = None

    if request.method == 'GET' and request.args.get('next'):
        session['next'] = request.args.get('next', None)

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        session['id'] = user.id
        session['full_name'] = user.full_name
        if 'next' in session:
            next = session.get('next')
            session.pop('next')
            return redirect(next)
        else:
            return redirect(url_for('todo_app.index'))

    return render_template('user/login.html', form=form, error=error)



@user_app.route('/logout')
def logout():
    """
    Logout page
    """
    session.pop('id')
    session.pop('full_name')
    flash('User loggerd out')
    return redirect(url_for('.login'))
