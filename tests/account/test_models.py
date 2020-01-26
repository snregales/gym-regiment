"""Account Models Test Module."""

import pytest

from datetime import date
from sqlalchemy.exc import IntegrityError

from src.account.models import Account, BioMetric
from tests.config.factories import AccountFactory, BioMetricFactory

@pytest.mark.usefixture("db")
class TestAccount:
    """Account tests."""

    def _account(self, db) -> Account:
        account = AccountFactory()
        db.session.commit()
        return account

    def test_get_by_id(self, db) -> None:
        account = self._account(db)
        retrieve = Account.get_by_id(account.id)
        assert account == retrieve

    def test_user_not_nullable(self, db):
        account = Account(
            first_name="first", 
            last_name="last", 
            dob=date(1993,9,28))
        assert not account.user
        assert not account.user_id
        with pytest.raises(IntegrityError) as Ie:
            account.save()


@pytest.mark.usefixture("db")
class TestBiometric:
    """Biometric tests."""

    @property
    def _biometric(self) -> BioMetric:
        biometric = BioMetric(weight=85.0, height=1.85, sex=1)
        biometric.save()
        return biometric

    def test_retreive_impirical_properties(self, db) -> None:
        biometric = self._biometric
        assert round(biometric.weight_in_pounds, 2) == 187.39
        assert round(biometric.height_in_feet, 2) == 6.07

    def test_retreive_metrics(self, db):
        biometric = self._biometric
        assert round(biometric.bmi, 1) == 24.8

    def test_account_is_nullable(self, db) -> None:
        biometric = self._biometric
        assert not biometric.has_account
        assert biometric.age == -1