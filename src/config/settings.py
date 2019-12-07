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

PROJECT_ROOT: str = os.path.join(
    os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir), os.pardir
)
TEST_PATH: str = os.path.join(PROJECT_ROOT, "tests")
FLASK_ENV: str = ENV.str("FLASK_ENV", default="production")
DEBUG: bool = FLASK_ENV == "development"  # if flask environment is development set debug to True
SQLALCHEMY_DATABASE_URI = ENV.str("DATABASE_URL")
SECRET_KEY = ENV.str("SECRET_KEY")
BCRYPT_LOG_ROUNDS = ENV.int("BCRYPT_LOG_ROUNDS", default=13)
DEBUG_TB_ENABLED = DEBUG
DEBUG_TB_INTERCEPT_REDIRECTS: bool = False
CACHE_TYPE: str = "simple"  # Can be "memcached", "redis", etc.
SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
WEBPACK_MANIFEST_PATH: str = "webpack/manifest.json"
JWT_SECRET_KEY: str = ENV.str(
    "JWT_SECRET_KEY", default=SECRET_KEY
)  # If this is not set, we use the flask SECRET_KEY value instead.
REFRESH_EXP_LENGTH: int = ENV.int("REFRESH_EXP_LENGTH", default=30)
ACCESS_EXP_LENGTH: int = ENV.int("ACCESS_EXP_LENGTH", default=10)
