import pytest
from src.math_operations import subtract

def test_subtract_positive_numbers():
    assert subtract(10, 4) == 6

def test_subtract_negative_numbers():
    assert subtract(-5, -2) == -3

def test_subtract_zero():
    assert subtract(0, 0) == 0

def test_subtract_positive_and_negative():
    assert subtract(7, -3) == 10

def test_subtract_floats():
    assert subtract(5.5, 2.2) == pytest.approx(3.3)

def test_subtract_large_numbers():
    assert subtract(2_000_000, 1_000_000) == 1_000_000
