import pytest
from src.math_operations import subtract

@pytest.mark.parametrize("a,b,expected", [
    (5, 3, 2),
    (0, 0, 0),
    (-1, -1, 0),
    (-5, -3, -2),
    (2.5, 1.5, 1.0),
    (1e10, 1e5, 9999900000.0),
])
def test_subtract_basic(a, b, expected):
    assert subtract(a, b) == expected

def test_subtract_type_error():
    with pytest.raises(TypeError):
        subtract("a", 1)
    with pytest.raises(TypeError):
        subtract(1, "b")
    with pytest.raises(TypeError):
        subtract("a", "b")
