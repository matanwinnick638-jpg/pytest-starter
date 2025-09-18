import pytest
from src import calculator

def test_add():
    assert calculator.add(2, 3) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="divide by zero"):
        calculator.divide(1, 0)
