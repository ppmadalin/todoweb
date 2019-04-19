from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# Setup database
db = SQLAlchemy()


def create_app(**config):
    """
    Application factory
    """
    app = Flask(__name__)

    # Load config
    app.config.from_pyfile('settings.py')

    # Update config if any is given
    app.config.update(config)

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
