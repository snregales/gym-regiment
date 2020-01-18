import pytest
from datetime import datetime, timedelta
from src.user.utils import generate_reset_key, is_key_valid
from src.user import KEY_LIFE

def test_generate_reset_key_not_equal():
    assert generate_reset_key() != generate_reset_key()


def test_generate_reset_key():
    key = generate_reset_key()
    assert len(key) == 16
    assert key.isascii()
    assert key.isupper()
    assert key.isalnum()

now = datetime.now()
@pytest.mark.parametrize('date, expected', [
    (now, True),
    (now - timedelta(days=KEY_LIFE), False),
    (now + timedelta(days=1), False)
])
def test_is_key_valid(date: datetime, expected: bool):
    assert is_key_valid(date) == expected