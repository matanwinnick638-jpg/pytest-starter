# tests/test_calculator.py

import pytest
from src import calculator

# ---------- ADD ----------
def test_add_positive_numbers():
    assert calculator.add(2, 3) == 5

def test_add_negative_numbers():
    assert calculator.add(-2, -3) == -5

def test_add_zero():
    assert calculator.add(0, 5) == 5
    assert calculator.add(0, 0) == 0

# ---------- SUBTRACT ----------
def test_subtract_positive_numbers():
    assert calculator.subtract(10, 4) == 6

def test_subtract_negative_numbers():
    assert calculator.subtract(-5, -2) == -3

def test_subtract_result_negative():
    assert calculator.subtract(3, 5) == -2

# ---------- DIVIDE ----------
def test_divide_normal():
    assert calculator.divide(10, 2) == 5

def test_divide_float_result():
    assert calculator.divide(7, 2) == 3.5

def test_divide_negative():
    assert calculator.divide(-10, 2) == -5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="divide by zero"):
        calculator.divide(5, 0)
