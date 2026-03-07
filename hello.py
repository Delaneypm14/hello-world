"""Hello World module with utility functions."""


def greet(name=None):
    """Return a greeting message."""
    if name:
        return f"Hello, {name}!"
    return "Hello, World!"


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def is_palindrome(text):
    """Check if a string is a palindrome (case-insensitive)."""
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def fizzbuzz(n):
    """Return FizzBuzz result for a given number."""
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


def factorial(n):
    """Return the factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    return n * factorial(n - 1)
