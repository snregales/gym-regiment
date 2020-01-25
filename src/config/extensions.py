# -*- coding: utf-8 -*-
"""
Extensions module.

Each extension is initialized in the app factory located in app.py.
"""
from flask_bcrypt import Bcrypt
from flask_debugtoolbar import DebugToolbarExtension
from flask_graphql_auth import GraphQLAuth
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

bcrypt = Bcrypt()
csrf = CSRFProtect()
db = SQLAlchemy()
migrate = Migrate()
debug = DebugToolbarExtension()
auth = GraphQLAuth()
