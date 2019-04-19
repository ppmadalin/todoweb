"""
views.py

Contains all the views related to todo app
"""
from flask import Blueprint
from flask import render_template
from .models import Task


todo_app = Blueprint('todo_app', __name__)


@todo_app.route('/')
def index():
    """
    Index page
    """
    return render_template('todo/index.html', title='test')

@todo_app.route('/task')
def task():
    """
    Task page
    """
    return '<h1>Task</h1>'
