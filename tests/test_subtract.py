import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from math_operations import subtract
import pytest

def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2

def test_subtract_negative_numbers():
    assert subtract(-5, -3) == -2

def test_subtract_mixed_sign_numbers():
    assert subtract(-5, 3) == -8
    assert subtract(5, -3) == 8

def test_subtract_zero():
    assert subtract(0, 0) == 0
    assert subtract(5, 0) == 5
    assert subtract(0, 5) == -5

def test_subtract_floats():
    assert subtract(5.5, 2.2) == pytest.approx(3.3)

def test_subtract_large_numbers():
    assert subtract(10**10, 10**9) == 9 * 10**9
