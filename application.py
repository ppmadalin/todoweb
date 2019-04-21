"""
application.py

Aplication factory and entry point
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# Setup database
db = SQLAlchemy()


def create_app(development=True):
    """
    Application factory
    """
    app = Flask(__name__)

    # Load config
    if development:
        app.config.from_object('settings.DevelopmentConfig')
    else:
        app.config.from_object('settings.ProductionConfig')

    # Initialize database
    db.init_app(app)
    migrate = Migrate(app, db)

    # Import blueprints
    from todo.views import todo_app
    from user.views import user_app

    # Register blueprints
    app.register_blueprint(todo_app)
    app.register_blueprint(user_app)

    return app
