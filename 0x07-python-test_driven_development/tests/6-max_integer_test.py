#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases to be evaluated"""

    def test_module_docstring(self):
        """Test for module docstring"""
        m = __import__('6-max_integer').__doc__
        self.assertTrue(len(m) > 1)

    def test_function_docstring(self):
        """Test for function docstring"""
        f = __import__('6-max_integer').max_integer.__doc__
        self.assertTrue(len(f) > 1)

    def test_positive(self):
        """Tests for lists containing positive numbers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([5, 2, 3, 4]), 5)
        self.assertEqual(max_integer([1.10, 2.20, 6.60, 4.2]), 6.60)
        self.assertEqual(max_integer([0, 0, 0, 0.000]), 0)

    def test_negative(self):
        """Tests for lists containing negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -22, -3.44, -4.111]), -1)
        self.assertEqual(max_integer([-1, -2, -3, -0]), 0)

    def test_empty(self):
        """Test for passing an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        """Test for passing only 1 element in the list"""
        self.assertEqual(max_integer([5]), 5)

    def test_no_args(self):
        """Test for passing no arguments"""
        self.assertEqual(max_integer(), None)

    def test_none(self):
        """Test for passing None as an argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_int(self):
        """Test for list with non-int type elements"""
        list = [2, 5, "goat", True, 45]
        with self.assertRaises(TypeError):
            max_integer(list)


if __name__ == "__main__":
    unittest.main()
