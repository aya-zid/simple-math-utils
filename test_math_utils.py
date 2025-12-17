import pytest
from math_utils import add, subtract, multiply, divide

# Assume the provided functions are in a file named `math_utils.py` in the same directory.

# --- Tests for add function ---
def test_add_normal_cases():
    """Test add function with various normal inputs."""
    assert add(1, 2) == 3
    assert add(-1, -2) == -3
    assert add(0, 0) == 0
    assert add(5.5, 4.5) == 10.0
    assert add(-10, 5) == -5
    assert add(1000, 2000) == 3000

def test_add_edge_cases():
    """Test add function with edge cases like large numbers and float precision."""
    # Large numbers
    assert add(1_000_000_000, 2_000_000_000) == 3_000_000_000
    # Floating point precision (use pytest.approx for comparison)
    assert add(0.1, 0.2) == pytest.approx(0.3)
    assert add(123.4567, 789.0123) == pytest.approx(912.469)
    # Mixed large and very small numbers
    assert add(1_000_000_000.0, 0.000000001) == pytest.approx(1_000_000_000.000000001)
    assert add(-0.000001, 0.000002) == pytest.approx(0.000001)

# --- Tests for subtract function ---
def test_subtract_normal_cases():
    """Test subtract function with various normal inputs."""
    assert subtract(5, 2) == 3
    assert subtract(2, 5) == -3
    assert subtract(-5, -2) == -3
    assert subtract(0, 0) == 0
    assert subtract(10.0, 3.5) == 6.5
    assert subtract(-5, 5) == -10

def test_subtract_edge_cases():
    """Test subtract function with edge cases like large numbers and float precision."""
    # Large numbers
    assert subtract(2_000_000_000, 1_000_000_000) == 1_000_000_000
    assert subtract(1_000_000_000, 2_000_000_000) == -1_000_000_000
    # Floating point precision
    assert subtract(0.3, 0.1) == pytest.approx(0.2)
    assert subtract(100.0001, 0.0001) == pytest.approx(100.0)
    # Subtracting zero
    assert subtract(5, 0) == 5
    assert subtract(0, 5) == -5

# --- Tests for multiply function ---
def test_multiply_normal_cases():
    """Test multiply function with various normal inputs."""
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(-2, -3) == 6
    assert multiply(0, 5) == 0
    assert multiply(5, 0) == 0
    assert multiply(2.5, 2) == 5.0

def test_multiply_edge_cases():
    """Test multiply function with edge cases like multiplying by 1, large numbers, and float precision."""
    # Multiplying by 1
    assert multiply(10, 1) == 10
    assert multiply(-7, 1) == -7
    # Large numbers
    assert multiply(1_000_000, 100) == 100_000_000
    # Floating point precision
    assert multiply(0.5, 0.5) == pytest.approx(0.25)
    assert multiply(1.23, 10) == pytest.approx(12.3)
    # Multiplying by a very small number
    assert multiply(1_000_000, 0.000001) == pytest.approx(1.0)
    assert multiply(0.000001, 0.000001) == pytest.approx(1e-12)

# --- Tests for divide function ---
def test_divide_normal_cases():
    """Test divide function with various normal inputs."""
    assert divide(6, 2) == 3.0
    assert divide(10, -2) == -5.0
    assert divide(-9, -3) == 3.0
    assert divide(0, 5) == 0.0
    assert divide(7.5, 2.5) == 3.0

def test_divide_edge_cases():
    """Test divide function with edge cases like dividing by 1, by self, large numbers, and float precision."""
    # Dividing by 1
    assert divide(10, 1) == 10.0
    assert divide(-5, 1) == -5.0
    # Dividing a number by itself
    assert divide(5, 5) == 1.0
    assert divide(-10, -10) == 1.0
    # Floating point precision
    assert divide(1.0, 3.0) == pytest.approx(0.3333333333333333)
    assert divide(10.0, 4.0) == pytest.approx(2.5)
    # Large numbers
    assert divide(1_000_000, 100) == pytest.approx(10_000.0)
    assert divide(100, 1_000_000) == pytest.approx(0.0001)
    # Dividing a negative by a positive, resulting in float
    assert divide(-10, 3) == pytest.approx(-3.3333333333333335)


def test_divide_by_zero_exception():
    """Test divide function raises ValueError when division by zero occurs."""
    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        divide(10, 0)
    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        divide(0, 0) # This is still a division by zero scenario for 'b'