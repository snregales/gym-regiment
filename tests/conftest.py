# -*- coding: utf-8 -*-
"""Defines fixtures available to all tests."""

import logging

import pytest
from webtest import TestApp
from flask import Flask

from src.app import create_app


@pytest.fixture
def app():
    """Create application for the tests."""
    _app: Flask = create_app(config_object="tests.settings")
    _app.logger.setLevel(logging.CRITICAL)
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture
def testapp(app) -> TestApp:  # pylint: disable=redefined-outer-name
    """Create Webtest app."""
    return TestApp(app)
