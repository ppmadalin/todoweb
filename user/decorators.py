from functools import wraps
from flask import session, flash, redirect, url_for, request


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('id') == None:
            flash('Please login')
            return redirect(url_for('user_app.login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


