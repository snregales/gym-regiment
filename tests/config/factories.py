# -*- coding: utf-8 -*-
"""Factories to help in tests."""

from datetime import date
from random import randint, uniform

from factory import PostGenerationMethodCall, Sequence, SubFactory
from factory.alchemy import SQLAlchemyModelFactory

from src.account.models import Account, BioMetric
from src.config.database import db
from src.user.models import User, Voucher


class BaseFactory(SQLAlchemyModelFactory):
    """Base factory."""

    class Meta:  # pylint: disable=too-few-public-methods
        """Factory configuration."""

        abstract = True
        sqlalchemy_session = db.session


class BioMetricFactory(BaseFactory):
    """Biometric Factory."""

    height = Sequence(lambda n: uniform(1.5, 2.0))
    weight = Sequence(lambda n: uniform(50.0, 100.0))
    sex = Sequence(lambda n: randint(1, 2))

    class Meta:
        """Factory configuration."""

        model = BioMetric


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


class AccountFactory(BaseFactory):
    """Account Factory."""

    first_name = Sequence(lambda n: f"first{n}")
    last_name = Sequence(lambda n: f"last{n}")
    dob = Sequence(
        lambda n: date(randint(1950, date.today().year), randint(1, 12), randint(1, 28))
    )
    user = SubFactory(UserFactory)
    biometric = SubFactory(BioMetricFactory)

    class Meta:
        """Factory configuration."""

        model = Account
