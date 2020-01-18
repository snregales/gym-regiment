# -*- coding: utf-8 -*-
"""Model unit tests."""
import datetime as dt

import pytest

from src.user.models import Role, User, Vouch
from tests.config.factories import UserFactory, VouchFactory

from . import PASSWORD


@pytest.mark.usefixtures("db")
class TestUser:
    """User tests."""

    def test_get_by_id(self) -> None:
        """Get user by ID."""
        user = User("foo@bar.com")
        user.save()

        retrieved = User.get_by_id(user.id)
        assert retrieved == user

    def test_created_at_defaults_to_datetime(self) -> None:
        """Test creation date."""
        user = User(email="foo@bar.com")
        user.save()
        assert bool(user.created_at)
        assert isinstance(user.created_at, dt.datetime)

    def test_vouch_is_nullable(self) -> None:
        """Test null password."""
        user = User(email="foo@bar.com")
        user.save()
        assert user.vouch is None

    def test_factory(self, db) -> None:
        """
        Test user factory.

        :param db :type fixture
        """
        user = UserFactory(vouch__password=PASSWORD)
        # user.vouch = VouchFactory(password=password)
        db.session.commit()
        assert bool(user.email)
        assert bool(user.created_at)
        assert not user.is_admin
        assert user.is_active
        assert user.vouch.check_password(PASSWORD)

    def test_check_password(self) -> None:
        """Check password."""
        user = User.create(email="foo@bar.com")
        user.vouch = Vouch(password=PASSWORD)
        assert user.has_password
        check_pass = user.vouch.check_password
        assert check_pass(PASSWORD)
        assert not check_pass("barfoobaz")

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
