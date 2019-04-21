"""
settings.py

Contains all the settings of the app
"""
import os
import pathlib

from dotenv import load_dotenv

# load dotenv in the base root
basedir = os.path.abspath(os.path.dirname(__file__))
dotenv_path = os.path.join(basedir, '.env')
load_dotenv(dotenv_path)

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY')

class ProductionConfig(Config):
    DB_USERNAME=os.environ['DB_USERNAME']
    DB_PASSWORD=os.environ['DB_PASSWORD']
    DB_HOST=os.environ['DB_HOST']
    DATABASE_NAME=os.environ['DATABASE_NAME']
    # mysql://username:password@server/db
    DB_URI = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:3306/{DATABASE_NAME}'
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    MYSQL_ROOT_PASSWORD = os.environ['MYSQL_ROOT_PASSWORD']


class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE = pathlib.Path(__file__).parent.joinpath('instance/tododev.db')
    DB_URI = f'sqlite:///{DATABASE}'
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
