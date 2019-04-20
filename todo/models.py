"""
models.py

Contains all the models related to tasks
"""
import datetime
from application import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    description = db.Column(db.String(80), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False,
                           default=datetime.date.today())
    end_date = db.Column(db.DateTime)
    status = db.Column(db.Boolean)

    owner = db.relationship('User',
                            backref=db.backref('task', lazy='dynamic'))

    def __init__(self, user, description, start_date, end_date, status=False):
        self.owner = user
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.status = status


    def __repr__(self):
        return f'<Task {self.description}>'
