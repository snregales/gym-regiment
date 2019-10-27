import pytest

from src.example import (
    example, runner)

def test_example():
    assert example() == "Hello, I'm the example"

def test_runner():
    assert runner() == "Hello, I'm the exampleHello, I'm the exampleHello, I'm the example"
