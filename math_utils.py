def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """
    Return the division of a by b.
    Raises ValueError if b is zero.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b
