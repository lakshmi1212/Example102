import pytest
from src.math_operations import subtract

def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2

def test_subtract_negative_numbers():
    assert subtract(-1, -1) == 0

def test_subtract_zero():
    assert subtract(0, 0) == 0

def test_subtract_positive_and_negative():
    assert subtract(-5, 10) == -15
    assert subtract(10, -5) == 15

def test_subtract_floats():
    assert subtract(5.5, 3.2) == pytest.approx(2.3)

def test_subtract_large_numbers():
    assert subtract(2000000, 1000000) == 1000000
