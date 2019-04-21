"""
views.py

Contains all the views related to todo app
"""
from flask import Blueprint
from flask import render_template
from flask import session
from flask import redirect
from flask import url_for
from flask import flash
from flask import request

from application import db
from .forms import AddTaskForm
from .models import Task
from user.models import User
from user.decorators import login_required


todo_app = Blueprint('todo_app', __name__)


@todo_app.route('/')
@login_required
def index():
    """
    Index page
    """
    page = int(request.values.get('page', '1'))
    user = User.query.get(1)
    tasks = Task.query.filter_by(owner=user).paginate(page, 5, False)

    return render_template('todo/index.html', tasks=tasks )

@todo_app.route('/add-task', methods=('GET', 'POST'))
@login_required
def add_task():
    """
    Task page
    """
    form = AddTaskForm()
    if form.validate_on_submit():
        user = User.query.get(session['id'])
        task = Task(
            user,
            form.description.data,
            form.start_date.data,
            form.end_date.data,
        )

        db.session.add(task)
        db.session.commit()
        flash('Task was added successfully')
        return redirect(url_for('.index'))
    return render_template('todo/add_task.html', form=form)

