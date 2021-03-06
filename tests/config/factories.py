# -*- coding: utf-8 -*-
"""Factories to help in tests."""
from factory import PostGenerationMethodCall, Sequence, SubFactory
from factory.alchemy import SQLAlchemyModelFactory

from src.config.database import db
from src.user.models import User, Voucher


class BaseFactory(SQLAlchemyModelFactory):
    """Base factory."""

    class Meta:  # pylint: disable=too-few-public-methods
        """Factory configuration."""

        abstract = True
        sqlalchemy_session = db.session


class VoucherFactory(BaseFactory):
    """Voucher factory."""

    password = PostGenerationMethodCall("set_password", "example")

    class Meta:
        """Factory configuration."""

        model = Voucher


class ResetKeyFactory(VoucherFactory):
    """Voucher's reset key Factory."""

    reset_key = PostGenerationMethodCall("set_reset_key")


class UserFactory(BaseFactory):
    """User factory."""

    # username = Sequence(lambda n: f"user{n}")
    email = Sequence(lambda n: f"user{n}@example.com")
    # password = "example"
    voucher = SubFactory(VoucherFactory)
    is_active = True

    class Meta:  # pylint: disable=too-few-public-methods
        """Factory configuration."""

        model = User
