# -*- coding: utf-8 -*-
"""Defines fixtures available to all tests."""

import logging

import pytest
from flask import Flask
from webtest import TestApp

from src.app import create_app
from src.config.database import DB

from tests.config.factories import UserFactory

@pytest.fixture
def app():
    """Create application for the tests."""
    _app: Flask = create_app(config_object="tests.config.settings")
    _app.logger.setLevel(logging.CRITICAL)
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture
def testapp(app: Flask) -> TestApp:  # pylint: disable=redefined-outer-name
    """
    Create Webtest app.

    :param app :type Flask: WGSI application to be use for testing purposes
    """
    return TestApp(app)

@pytest.fixture
def db(app):  # pylint: disable=redefined-outer-name
    """Create database for the tests."""
    DB.app = app
    with app.app_context():
        DB.create_all()

    yield DB

    # Explicitly close DB connection
    DB.session.close()
    DB.drop_all()


@pytest.fixture
def user(db) -> UserFactory:  # pylint: disable=redefined-outer-name
    """Create user for the tests."""
    _user = UserFactory(password="myprecious")
    db.session.commit()
    return _user