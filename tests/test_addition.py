import pytest
from main import addition

def test_addition():
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0
    assert addition(-5, -5) == -10

def test_addition_with_floats():
    assert addition(2.5, 3.5) == 6.0
    assert addition(-1.5, 1.5) == 0.0
    assert addition(0.0, 0.0) == 0.0
    assert addition(-5.5, -5.5) == -11.0

def test_addition_with_mixed_types():
    assert addition(2, 3.5) == 5.5
    assert addition(-1.5, 1) == -0.5
    assert addition(0, 0.0) == 0.0
    assert addition(-5, -5.5) == -10.5

def test_addition_without_numbers():
    with pytest.raises(TypeError):
        addition("a", "b")
    with pytest.raises(TypeError):
        addition(None, None)
    with pytest.raises(TypeError):
        addition([], [])