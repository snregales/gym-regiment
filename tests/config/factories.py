# -*- coding: utf-8 -*-
"""Factories to help in tests."""
from factory import PostGenerationMethodCall, Sequence, SubFactory
from factory.alchemy import SQLAlchemyModelFactory

from src.config.database import db
from src.user.models import User, Vouch


class BaseFactory(SQLAlchemyModelFactory):
    """Base factory."""

    class Meta:  # pylint: disable=too-few-public-methods
        """Factory configuration."""

        abstract = True
        sqlalchemy_session = db.session

class VouchFactory(BaseFactory):
    """Vouch factory."""

    password = PostGenerationMethodCall("set_password", "example")

    class Meta:
        """Factory configuration."""

        model = Vouch


class UserFactory(BaseFactory):
    """User factory."""

    # username = Sequence(lambda n: f"user{n}")
    email = Sequence(lambda n: f"user{n}@example.com")
    # password = "example"
    vouch = SubFactory(VouchFactory)
    is_active = True

    class Meta:  # pylint: disable=too-few-public-methods
        """Factory configuration."""

        model = User
