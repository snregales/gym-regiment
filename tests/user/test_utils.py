import pytest

from src.user.utils import generate_reset_key


def test_generate_reset_key_not_equal():
    assert generate_reset_key() != generate_reset_key()


def test_generate_reset_key():
    key = generate_reset_key()
    assert len(key) == 16
    assert key.isascii()
    assert key.isupper()
    assert key.isalnum()
