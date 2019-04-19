"""
settings.py

Contains all the settings of the app
"""
import os
import pathlib

SECRET_KEY = os.getenv('SECRET_KEY')
DATABASE = pathlib.Path(__file__).parent.joinpath('instances/todo.db')
DB_URI = f'sqlite:///{DATABASE}'
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
