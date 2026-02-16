import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from math_operations import add
import pytest

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_add_mixed_sign_numbers():
    assert add(-2, 3) == 1

def test_add_zero():
    assert add(0, 0) == 0
    assert add(5, 0) == 5
    assert add(0, 5) == 5

def test_add_floats():
    assert add(2.5, 3.1) == pytest.approx(5.6)

def test_add_large_numbers():
    assert add(10**10, 10**10) == 2 * 10**10
