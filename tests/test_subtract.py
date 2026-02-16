import pytest
from src.math_operations import subtract

def test_subtract_positive_numbers():
    assert subtract(5, 2) == 3
    assert subtract(20, 10) == 10

def test_subtract_negative_numbers():
    assert subtract(-1, -2) == 1
    assert subtract(-10, 5) == -15

def test_subtract_zero():
    assert subtract(0, 0) == 0
    assert subtract(0, 5) == -5
    assert subtract(5, 0) == 5

def test_subtract_floats():
    assert subtract(2.5, 1.5) == 1.0
    assert subtract(-1.1, 1.1) == -2.2

def test_subtract_large_numbers():
    assert subtract(2_000_000_000, 1_000_000_000) == 1_000_000_000
