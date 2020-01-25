"""Test User Utils."""

from datetime import datetime, timedelta

import pytest

from src.user import KEY_LIFE
from src.user.utils import generate_reset_key, has_expired


def test_generate_reset_key_not_equal() -> None:
    """Test that no two instances of a reset key is equal."""
    assert generate_reset_key() != generate_reset_key()


def test_generate_reset_key() -> None:
    """Test if the reset key is properly generated."""
    key = generate_reset_key()
    assert len(key) == 16
    assert key.isascii()
    assert key.isupper()
    assert key.isalnum()


now = datetime.now()


@pytest.mark.parametrize(
    "date, expected",
    [
        (now, True),
        (now - timedelta(days=KEY_LIFE), False),
        (now + timedelta(days=1), False),
    ],
)
def test_has_expired(date: datetime, expected: bool) -> None:
    """Test that key satisfies all the meta atributes."""
    assert has_expired(date) == expected
