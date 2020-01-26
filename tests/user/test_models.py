# -*- coding: utf-8 -*-
"""Model unit tests."""
import datetime as dt

import pytest

from src.user.models import Role, User, Voucher
from tests.config.factories import UserFactory

from . import PASSWORD


@pytest.mark.usefixtures("db")
class TestUser:
    """User tests."""

    @property
    def _foo_user(self) -> User:
        """Creates and saves foo@bar user."""

        user = User(email="foo@bar.com")
        user.save()
        return user

    def test_get_by_id(self) -> None:
        """Get user by ID."""
        user = self._foo_user
        retrieved = User.get_by_id(user.id)
        assert retrieved == user

    # def test_email_is_unique(self):
    #     user = User(email="foo@bar.com")

    def test_created_at_defaults_to_datetime(self) -> None:
        """Test creation date."""
        user = self._foo_user
        assert bool(user.created_at)
        assert isinstance(user.created_at, dt.datetime)

    def test_vouch_is_nullable(self) -> None:
        """Test null password."""
        user = self._foo_user
        assert user.voucher is None

    def test_check_password(self) -> None:
        """Check password."""
        user = self._foo_user
        user.voucher = Voucher(password=PASSWORD)
        assert not bool(user.voucher.reset_key)
        assert not bool(user.voucher.key_generated_date)
        assert user.has_password
        check_pass = user.voucher.check_password
        assert check_pass(PASSWORD)
        assert bool(user.voucher.password_last_set)
        assert user.voucher.password_last_set.date() == dt.datetime.now().date()
        assert not check_pass("barfoobaz")

    def test_reset_key(self) -> None:
        """Check reset key."""
        user = self._foo_user
        user.voucher = Voucher()
        user.voucher.set_reset_key()
        assert not user.has_password
        assert not bool(user.voucher.password_last_set)
        assert bool(user.voucher.reset_key)
        assert bool(user.voucher.key_generated_date)
        assert user.voucher.key_generated_date.date() == dt.datetime.now().date()

    # def test_full_name(self) -> None:
    # """User full name."""
    # user = UserFactory(first_name="Foo", last_name="Bar")
    # assert user.full_name == "Foo Bar"

    def test_roles(self) -> None:
        """Add a role to a user."""
        role = Role(name="admin")
        role.save()
        user = UserFactory()
        user.roles.append(role)
        user.save()
        assert role in user.roles
