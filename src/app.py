# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
import logging
import sys

from flask import Flask, redirect, url_for
from flask_graphql import GraphQLView

from src.config.commands import lint, test
from src.config.extensions import AUTH, BCRYPT, DB, MIGRATE  # Database extensions
from src.config.schema import SCHEMA
from src.user.models import User


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
    register_graphql(app)
    register_extensions(app)
    register_shellcontext(app)
    return app


def register_graphql(app: Flask) -> bool:
    """
    Register graphql to the flask application.

    this includes view, schema with all register schemas
    and make index route redirect to /graphql route

    :param app :type Flask: Flask application to add graphql view to
    :return :type bool: is all extensions registered
    """
    app.add_url_rule(
        "/", view_func=lambda: redirect(url_for("graphql"))
    )  # register and redirect index route to graphql
    app.add_url_rule(
        "/graphql",
        view_func=GraphQLView.as_view("graphql", schema=SCHEMA, graphiql=True),
    )  # register graphql
    return True


def register_extensions(app: Flask) -> bool:
    """
    Register extenstion for flask to the flask application.

    :param app :type Flask: Flask application to register blueprints to
    :return :type bool: is all extensions registered
    """
    DB.init_app(app)
    MIGRATE.init_app(app, DB)
    BCRYPT.init_app(app)
    AUTH.init_app(app)
    return True


def register_shellcontext(app: Flask) -> bool:
    """
    Register shell context objects.

    :param app :type Flask: Flask application to register blueprints to
    :return :type bool: is all contexts registered
    """

    app.shell_context_processor(lambda: {"db": DB, "User": User})
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
