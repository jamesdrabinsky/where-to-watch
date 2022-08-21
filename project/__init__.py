from flask import Flask, render_template
from flask_assets import Bundle, Environment

from logging.handlers import RotatingFileHandler
import logging
from flask.logging import default_handler
import os

# ----------------------------
# Application Factory Function
# ----------------------------


def create_app():
    # Create Flask application
    app = Flask(__name__)

    # Configure the Flask application
    # config_type = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    # app.config.from_object(config_type)

    register_blueprints(app)
    # configure_logging(app)
    # register_app_callbacks(app)
    # register_error_pages(app)
    register_css_assets(app)
    return app


def register_blueprints(app):
    # Import blueprints
    from project.shows import shows_blueprint
    # from project.users import users_blueprint

    # Since the application instance is now created, register each Blueprint
    # with the Flask application instance (app)
    app.register_blueprint(shows_blueprint)
    # app.register_blueprint(users_blueprint, url_prefix='/users')


def register_css_assets(app):
    assets = Environment(app)
    css = Bundle("src/main.css", output="dist/main.css")
    assets.register("css", css)
    css.build()

