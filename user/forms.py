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
from werkzeug.security import check_password_hash

from user.models import User


class LoginForm(FlaskForm):
    email = StringField('Email',
                        [validators.InputRequired(),
                         validators.Email()])
    password = PasswordField('New Password',
                             [validators.Required(),
                              validators.Length(min=4, max=80)])

    def validate(self):
        rv = FlaskForm.validate(self)
        if not rv:
            return False

        user = User.query.filter_by(email=self.email.data).first()

        if user:
            if not check_password_hash(user.password, self.password.data):
                self.password.errors.append('Incorrect email or password')
                return False
            return True
        else:
            self.password.errors.append('Incorrect email or password')
            return False

class RegisterForm(FlaskForm):
    full_name = StringField('Full Name', [validators.InputRequired()])
    email = EmailField('Email Address',
                       [validators.InputRequired(),
                        validators.Email()])
    password = PasswordField('New Password',
                             [validators.Required(),
                              validators.Length(min=4, max=80)])
    confirm = PasswordField('Repeat Password',
                            [validators.EqualTo('password', message='Passwords must match')])

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email already in use, please use a different one.')
