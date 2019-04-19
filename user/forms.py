"""
forms.py

Contains register and login form for user app
"""
from flask_wtf import FlaskForm
from wtforms import validators
from wtforms import StringField
from wtforms import PasswordField
from wtforms import ValidationError
from wtforms.fields.html5 import EmailField

from user.models import User


class RegisterForm(FlaskForm):
    full_name = StringField('Full Name', [validators.InputRequired()])
    email = EmailField('Email Address', [validators.InputRequired(),
                                         validators.Email()])
    password = PasswordField('New Password', [validators.Required(),
                                              validators.Length(min=4, max=80)])
    confirm = PasswordField('Repeat Password',
                            [ validators.EqualTo('password', message='Passwords must match'), ])

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email already in use, please use a different one.')
