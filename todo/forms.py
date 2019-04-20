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
   description = StringField('Description', [validators.InputRequired()])
   start_date = DateField('Start date')
   end_date = DateField('End date')


