import pytest
from main import subtraction

def test_subtraction():
    assert subtraction("5", "3") == 2
    assert subtraction(-1, -1) == 0
    assert subtraction(0, 5) == -5
    assert subtraction(-5, -10) == 5

def test_subtraction_with_floats():
    assert subtraction("5.5", "2.2") == 3.3
    assert subtraction(-1.5, -0.5) == -1.0
    assert subtraction(0.0, 5.0) == -5.0
    assert subtraction(-5.5, -10.5) == 5.0

def test_subtraction_with_mixed_types():
    assert subtraction("5", "2.4") == 2.6
    assert subtraction(-1.5, 1) == -2.5
    assert subtraction(0, -3.5) == 3.5
    assert subtraction(-5, -5.5) == 0.5

def test_subtraction_with_invalid_inputs():
    with pytest.raises(TypeError):
        subtraction("a", "b")
    with pytest.raises(TypeError):
        subtraction([], [])
    with pytest.raises(TypeError):
        subtraction({}, {})
    with pytest.raises(TypeError):
        subtraction(None, None)    