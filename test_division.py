import pytest
from main import division

def test_division():
    assert division("10", "2") == 5
    assert division(-10, -2) == 5
    assert division(0, 5) == 0
    assert division(-10, 2) == -5

def test_division_with_floats():
    assert division("5.5", "2.2") == 2.5
    assert division(-1.5, -0.5) == 3.0
    assert division(0.0, 5.0) == 0.0
    assert division(-5.5, 2.2) == -2.5

def test_division_with_mixed_types():
    assert division("5", "2.5") == 2.0
    assert division(-1.5, 1) == -1.5
    assert division(0, -3.5) == 0.0
    assert division(-5, 2.5) == -2.0

def test_division_by_zero():
    with pytest.raises(ValueError):
        division("10", "0")
    with pytest.raises(ValueError):
        division(-10, 0)
    with pytest.raises(ValueError):
        division(0, 0)

def division_with_invalid_inputs():
    with pytest.raises(TypeError):
        division("a", "b")
    with pytest.raises(TypeError):
        division(None, None)
    with pytest.raises(TypeError):
        division([], [])
    with pytest.raises(TypeError):
        division({}, {})