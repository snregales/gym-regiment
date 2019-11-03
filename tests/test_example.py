"""
test_example.py
"""

import pytest

from src.example import name

@pytest.mark.parametrize("first, last, expected", [
    ("Sharlon", "Regales", "Hello, I'm Sharlon Regales"),
    ("Sharlon", None, "Hello, I'm Sharlon")
])
def test_example(first: str, last: str, expected: str) -> None:
    """
    Test two cases for the name fuction in src/example.py
    case one is given both first and last name,
    case two is given first name only
    Arguments:
        first {str} -- first anme
        last {str} -- last name
        expected {str} -- expected return string
    Returns:
        None
    """
    assert name(first=first, last=last) == expected
