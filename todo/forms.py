"""
forms.py

Contains add new task form
"""
from flask import session
from flask_wtf import FlaskForm
from wtforms import validators
from wtforms import StringField
from wtforms.fields.html5 import DateField
from wtforms import BooleanField


class AddTaskForm(FlaskForm):
   description = StringField('Description', [validators.InputRequired(),
                                             validators.Length(min=5, max=80)])
   start_date = DateField('Start date')
   end_date = DateField('End date')


