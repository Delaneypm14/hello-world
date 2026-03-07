"""Tests for the hello module."""

import unittest
from hello import greet, add, is_palindrome, fizzbuzz, factorial


class TestGreet(unittest.TestCase):
    def test_default_greeting(self):
        self.assertEqual(greet(), "Hello, World!")

    def test_named_greeting(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")

    def test_empty_string_name(self):
        self.assertEqual(greet(""), "Hello, World!")


class TestAdd(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

    def test_zero(self):
        self.assertEqual(add(0, 0), 0)

    def test_mixed_sign(self):
        self.assertEqual(add(-1, 1), 0)

    def test_floats(self):
        self.assertAlmostEqual(add(0.1, 0.2), 0.3)


class TestIsPalindrome(unittest.TestCase):
    def test_simple_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("hello"))

    def test_mixed_case(self):
        self.assertTrue(is_palindrome("Racecar"))

    def test_palindrome_with_spaces(self):
        self.assertTrue(is_palindrome("taco cat"))

    def test_single_character(self):
        self.assertTrue(is_palindrome("a"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))


class TestFizzbuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(9), "Fizz")

    def test_buzz(self):
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(10), "Buzz")

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        self.assertEqual(fizzbuzz(30), "FizzBuzz")

    def test_number(self):
        self.assertEqual(fizzbuzz(1), "1")
        self.assertEqual(fizzbuzz(7), "7")


class TestFactorial(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_one(self):
        self.assertEqual(factorial(1), 1)

    def test_positive(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            factorial(-1)


if __name__ == "__main__":
    unittest.main()
