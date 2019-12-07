# -*- coding: utf-8 -*-
"""
Extensions module.

Each extension is initialized in the app factory located in app.py.
"""
from flask_bcrypt import Bcrypt
from flask_caching import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_graphql_auth import GraphQLAuth
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

BCRYPT = Bcrypt()
CSRF = CSRFProtect()
LOGIN = LoginManager()
DB = SQLAlchemy()
MIGRATE = Migrate()
CACHE = Cache()
DEBUG = DebugToolbarExtension()
AUTH = GraphQLAuth()
