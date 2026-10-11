
def greet(name):
    """Return a greeting for the supplied namesS."""
    if not name:
        raise ValueError("Name cannot be empty")
    return f"Hello, {name}!"


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b


def multiply(a, b):
    return a * b