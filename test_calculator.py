import pytest
from main import calculator
from unittest.mock import patch
from io import StringIO

def test_calculator_addition():
    with patch('builtins.input', side_effect=['1', '2', '3']):
        with patch('sys.stdout', new=StringIO()) as fake_result:
            calculator()
            output = fake_result.getvalue()
            assert 'Result: 5.0' in output

def test_calculator_subtraction():
    with patch('builtins.input', side_effect=['2', '7', '4']):
        with patch('sys.stdout', new=StringIO()) as fake_result:
            calculator()
            output = fake_result.getvalue()
            assert 'Result: 3.0' in output

def test_calculator_multiplication():
    with patch('builtins.input', side_effect=['3', '2', '5']):
        with patch('sys.stdout', new=StringIO()) as fake_result:
            calculator()
            output = fake_result.getvalue()
            assert 'Result: 10.0' in output

def test_calculator_division():
    with patch('builtins.input', side_effect=['4', '6', '3']):
        with patch('sys.stdout', new=StringIO()) as fake_result:
            calculator()
            output = fake_result.getvalue()
            assert 'Result: 2.0' in output

@pytest.mark.parametrize(
        'inputs, expected_output',
        [
            (['1', '2', '3'], 'Result: 5.0'),      
            (['1', '-5', '-5.5'], 'Result: -10.5'),
            (['2', '10', '4'], 'Result: 6.0'),      
            (['3', '2', '3'], 'Result: 6.0'),      
            (['4', '6', '3'], 'Result: 2.0'),
        ]
)

def test_calculator_multiple_operations(inputs, expected_output):
    with patch('builtins.input', side_effect=inputs):
        with patch('sys.stdout', new=StringIO()) as fake_result:
            calculator()
            output = fake_result.getvalue()
            assert expected_output in output