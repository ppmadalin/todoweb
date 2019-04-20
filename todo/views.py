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


from application import db
from .forms import AddTaskForm
from .models import Task
from user.models import User
from user.decorators import login_required


todo_app = Blueprint('todo_app', __name__)


@todo_app.route('/')
def index():
    """
    Index page
    """
    tasks = Task.query.all()

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

