
import pytest

from app import greet, add, subtract


def test_greet():
    assert greet("Anurag") == "Hello, Anurag!"


def test_greet_empty_name():
    with pytest.raises(ValueError):
        greet("")


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(8, 3) == 5
