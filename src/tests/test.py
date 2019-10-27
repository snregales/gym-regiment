import pytest

from src.example import (
    example, runner)

def test_example():
    assert example() == "Hello, I'm the example"
