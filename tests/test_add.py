import pytest
from src.math_operations import add

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_add_zero():
    assert add(0, 0) == 0

def test_add_positive_and_negative():
    assert add(-2, 3) == 1

def test_add_floats():
    assert add(2.5, 3.2) == pytest.approx(5.7)

def test_add_int_and_float():
    assert add(2, 3.5) == pytest.approx(5.5)

def test_add_type_error():
    with pytest.raises(TypeError):
        add('2', 3)
    with pytest.raises(TypeError):
        add(2, None)
