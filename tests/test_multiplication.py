import pytest
from main import multiplication

def test_multiplication():
    assert multiplication("5", "3") == 15
    assert multiplication(-1, -1) == 1
    assert multiplication(0, 5) == 0
    assert multiplication(-5, -10) == 50

def test_multiplication_with_floats():
    assert multiplication("5.5", "2") == 11.0
    assert multiplication(-1.5, -0.5) == 0.75
    assert multiplication(0.0, 5.0) == 0.0
    assert multiplication(-5.5, -10.5) == 57.75

def test_multiplication_with_mixed_types():
    assert multiplication("5", "2.4") == 12.0
    assert multiplication(-1.5, 1) == -1.5
    assert multiplication(0, -3.5) == 0.0
    assert multiplication(-5, -5.5) == 27.5

def test_multiplication_with_invalid_inputs():
    with pytest.raises(TypeError):
        multiplication("a", "b")
    with pytest.raises(TypeError):
        multiplication(None, None)
    with pytest.raises(TypeError):
        multiplication([], [])
    with pytest.raises(TypeError):
        multiplication({}, {})