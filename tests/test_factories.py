"""Factory object tests module."""

import datetime as dt

import pytest

from .config.factories import (
    AccountFactory,
    BioMetricFactory,
    ResetKeyFactory,
    UserFactory,
    VoucherFactory,
)
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

    def test_biometric_factory(self, db) -> None:
        """
        Test Biometric Factory.

        :param db :type pytest.fixture
        """
        biometric = BioMetricFactory()
        db.session.commit()
        assert bool(biometric.height)
        assert 1.5 <= biometric.height <= 2.0
        assert bool(biometric.weight)
        assert 50.0 <= biometric.weight <= 100.0
        assert bool(biometric.sex)

    def test_account_factory(self, db) -> None:
        """
        Test Account Factory.

        :param db :type pytest.fixture
        """
        account = AccountFactory()
        assert bool(account.first_name)
        assert bool(account.last_name)
        assert bool(account.dob)
        assert dt.date(1950, 1, 1) <= account.dob <= dt.date.today()
        assert bool(account.biometric)
