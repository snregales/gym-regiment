# -*- coding: utf-8 -*-
"""Factories to help in tests."""
from factory import PostGenerationMethodCall, Sequence
from factory.alchemy import SQLAlchemyModelFactory

from src.config.database import db
from src.user.models import User


class BaseFactory(SQLAlchemyModelFactory):
    """Base factory."""

    class Meta:  # pylint: disable=too-few-public-methods
        """Factory configuration."""

        abstract = True
        sqlalchemy_session = db.session


class UserFactory(BaseFactory):
    """User factory."""

    # username = Sequence(lambda n: f"user{n}")
    email = Sequence(lambda n: f"user{n}@example.com")
    password = PostGenerationMethodCall("set_password", "example")
    is_active = True

    class Meta:  # pylint: disable=too-few-public-methods
        """Factory configuration."""

        model = User
