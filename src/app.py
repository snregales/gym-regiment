# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
import logging
import sys

from flask import Flask

from src import graphql
from src.config.commands import lint, test


def create_app(config_object: str = "src.config.settings") -> Flask:
    """
    Create application factory.

    this is further explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/

    :param config_object :type str :default src.config.settings
    :return :type Flask: the flask web application
    """
    app = Flask(__name__.split(".")[0])
    app.config.from_object(config_object)
    configure_logger(app)
    register_commands(app)
    register_blueprints(app)
    return app


def register_blueprints(app: Flask) -> bool:
    """
    Register Flask blueprints.

    :param app :type Flask: Flask application to register blueprints to
    :return :type bool: True if commands are loaded properly
    """
    app.register_blueprint(graphql.views.BP)
    return True


def register_commands(app: Flask) -> bool:
    """
    Register Click commands to given Flask app.

    :param app :type Flask: Flask application to register extensions to
    :return :type bool: True if commands are loaded properly
    """
    app.cli.add_command(test)
    app.cli.add_command(lint)
    return True


def configure_logger(app: Flask) -> bool:
    """
    Configure logging for the incoming flask app.

    :param app :type Flask: Flask application to register extensions to
    :return :type bool: True if configuration is setup properly
    """
    handler = logging.StreamHandler(sys.stdout)
    if not app.logger.handlers:
        app.logger.addHandler(handler)
    return True
