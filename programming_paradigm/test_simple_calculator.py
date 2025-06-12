#!/usr/bin/env python3
"""
Unit Tests for SimpleCalculator Class

This module contains comprehensive unit tests for the SimpleCalculator class,
testing all arithmetic operations with various scenarios including edge cases.
"""

import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Test cases for the SimpleCalculator class."""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method with various scenarios."""
        # Test positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 15), 25)
        
        # Test with zero
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(0, 0), 0)
        
        # Test negative numbers
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(-10, 5), -5)
        
        # Test floating point numbers
        self.assertEqual(self.calc.add(2.5, 3.7), 6.2)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=7)
        
        # Test large numbers
        self.assertEqual(self.calc.add(1000000, 2000000), 3000000)

    def test_subtraction(self):
        """Test the subtraction method with various scenarios."""
        # Test positive numbers
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(20, 8), 12)
        
        # Test with zero
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        
        # Test negative numbers
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(-5, 3), -8)
        self.assertEqual(self.calc.subtract(5, -3), 8)
        
        # Test floating point numbers
        self.assertEqual(self.calc.subtract(5.5, 2.3), 3.2)
        self.assertAlmostEqual(self.calc.subtract(0.3, 0.1), 0.2, places=7)
        
        # Test same numbers (result should be zero)
        self.assertEqual(self.calc.subtract(7, 7), 0)
        self.assertEqual(self.calc.subtract(-7, -7), 0)

    def test_multiplication(self):
        """Test the multiplication method with various scenarios."""
        # Test positive numbers
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(7, 8), 56)
        
        # Test with zero
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)
        
        # Test with one
        self.assertEqual(self.calc.multiply(5, 1), 5)
        self.assertEqual(self.calc.multiply(1, 5), 5)
        
        # Test negative numbers
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        self.assertEqual(self.calc.multiply(3, -4), -12)
        self.assertEqual(self.calc.multiply(-3, -4), 12)
        
        # Test floating point numbers
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)
        self.assertAlmostEqual(self.calc.multiply(0.1, 0.3), 0.03, places=7)
        
        # Test large numbers
        self.assertEqual(self.calc.multiply(1000, 1000), 1000000)

    def test_division(self):
        """Test the division method with various scenarios."""
        # Test normal division
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(15, 3), 5.0)
        self.assertEqual(self.calc.divide(20, 4), 5.0)
        
        # Test division resulting in float
        self.assertEqual(self.calc.divide(10, 3), 10/3)
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.3333333333333333, places=7)
        
        # Test division with negative numbers
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(10, -2), -5.0)
        self.assertEqual(self.calc.divide(-10, -2), 5.0)
        
        # Test division with floating point numbers
        self.assertEqual(self.calc.divide(7.5, 2.5), 3.0)
        self.assertAlmostEqual(self.calc.divide(1.0, 3.0), 0.3333333333333333, places=7)
        
        # Test division by one
        self.assertEqual(self.calc.divide(5, 1), 5.0)
        self.assertEqual(self.calc.divide(-5, 1), -5.0)
        
        # Test zero divided by number
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        self.assertEqual(self.calc.divide(0, -5), 0.0)

    def test_division_by_zero(self):
        """Test division by zero returns None."""
        # Test division by zero with positive numerator
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(1, 0))
        
        # Test division by zero with negative numerator
        self.assertIsNone(self.calc.divide(-10, 0))
        self.assertIsNone(self.calc.divide(-1, 0))
        
        # Test division by zero with zero numerator
        self.assertIsNone(self.calc.divide(0, 0))
        
        # Test division by zero with floating point numerator
        self.assertIsNone(self.calc.divide(5.5, 0))
        self.assertIsNone(self.calc.divide(0.0, 0))

    def test_edge_cases(self):
        """Test edge cases and boundary conditions."""
        # Test very large numbers
        large_num = 10**10
        self.assertEqual(self.calc.add(large_num, large_num), 2 * large_num)
        self.assertEqual(self.calc.subtract(large_num, large_num), 0)
        
        # Test very small numbers
        small_num = 0.000001
        self.assertAlmostEqual(self.calc.add(small_num, small_num), 2 * small_num, places=7)
        
        # Test precision with floating point arithmetic
        result = self.calc.add(0.1, 0.1)
        result = self.calc.add(result, 0.1)
        self.assertAlmostEqual(result, 0.3, places=7)

    def test_method_return_types(self):
        """Test that methods return expected data types."""
        # Addition should return numeric type
        result = self.calc.add(1, 2)
        self.assertIsInstance(result, (int, float))
        
        # Subtraction should return numeric type
        result = self.calc.subtract(5, 3)
        self.assertIsInstance(result, (int, float))
        
        # Multiplication should return numeric type
        result = self.calc.multiply(2, 3)
        self.assertIsInstance(result, (int, float))
        
        # Division should return float or None
        result = self.calc.divide(6, 2)
        self.assertIsInstance(result, (float, type(None)))
        
        # Division by zero should return None
        result = self.calc.divide(1, 0)
        self.assertIsNone(result)


if __name__ == '__main__':
    # Run the tests
    unittest.main(verbosity=2)
