import pytest
from src.math_operations import add

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, -1, -2),
    (-5, 5, 0),
    (1.5, 2.5, 4.0),
    (1_000_000, 2_000_000, 3_000_000),
    (0, 5, 5),
    (5, 0, 5)
])
def test_add(a, b, expected):
    assert add(a, b) == expected

def test_add_typeerror():
    with pytest.raises(TypeError):
        add('a', 1)
    with pytest.raises(TypeError):
        add(1, None)
