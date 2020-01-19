"""Factory object tests module."""

import datetime as dt

import pytest

from .config.factories import ResetKeyFactory, UserFactory, VoucherFactory
from .user import PASSWORD


@pytest.mark.usefixtures("db")
class TestFactory:
    """Factory tests."""

    def test_user_factory(self, db) -> None:
        """
        Test user factory.

        :param db :type pytest.fixture
        """
        user = UserFactory(voucher__password=PASSWORD)
        db.session.commit()
        assert bool(user.email)
        assert bool(user.created_at)
        assert user.created_at.date() == dt.datetime.now().date()
        assert not user.is_admin
        assert user.is_active

    def test_voucher_factory(self, db) -> None:
        """
        Test voucher factory.

        :param db :type pytest.fixture
        """
        voucher = VoucherFactory(password=PASSWORD)
        db.session.commit()
        assert bool(voucher.password)
        assert voucher.check_password(PASSWORD)
        assert bool(voucher.password_last_set)
        assert voucher.password_last_set.date() == dt.datetime.now().date()
        assert not bool(voucher.reset_key)
        assert not bool(voucher.key_generated_date)

    def test_reset_key_factory(self, db) -> None:
        """
        Test Reset Key Factory.

        :param db :type pytest.fixture
        """
        reset = ResetKeyFactory()
        db.session.commit()
        assert bool(reset.reset_key)
        assert bool(reset.key_generated_date)
        assert reset.key_generated_date.date() == dt.datetime.now().date()
        assert bool(reset.password)
        assert reset.check_password("example")
