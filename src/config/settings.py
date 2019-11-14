# -*- coding: utf-8 -*-
"""Application configuration.

Most configuration is set via environment variables.

For local development, use a .env file to set
environment variables.
"""
import os

from environs import Env

ENV = Env()
ENV.read_env()

PROJECT_ROOT = os.path.join(
    os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir), os.pardir
)
TEST_PATH = os.path.join(PROJECT_ROOT, "tests")
FLASK_ENV = ENV.str("FLASK_ENV", default="production")
DEBUG = FLASK_ENV == "development" # if flask environment is development set debug to True
SQLALCHEMY_DATABASE_URI = ENV.str("DATABASE_URL")
SECRET_KEY = ENV.str("SECRET_KEY")
BCRYPT_LOG_ROUNDS = ENV.int("BCRYPT_LOG_ROUNDS", default=13)
DEBUG_TB_ENABLED = DEBUG
DEBUG_TB_INTERCEPT_REDIRECTS = False
CACHE_TYPE = "simple"  # Can be "memcached", "redis", etc.
SQLALCHEMY_TRACK_MODIFICATIONS = False
WEBPACK_MANIFEST_PATH = "webpack/manifest.json"