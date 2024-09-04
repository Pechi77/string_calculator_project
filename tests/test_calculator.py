import unittest
from string_calculator.calculator import StringCalculator



class TestStringCalculator(unittest.TestCase):
    def test_empty_string(self):
        calc = StringCalculator()
        self.assertEqual(calc.add(''), 0)
    
    def test_single_number(self):
        calc = StringCalculator()
        self.assertEqual(calc.add('1'), 1)
    
    def test_two_numbers(self):
        calc = StringCalculator()
        self.assertEqual(calc.add('1,2'), 3)
    
    def test_another_number(self):
        calc = StringCalculator()
        self.assertEqual(calc.add('1,4'), 5)
    
    def test_multiple_numbers(self):
        calc = StringCalculator()
        self.assertEqual(calc.add('1,2,3,4'), 10)

    def test_different_delimiters(self):
        calc = StringCalculator()
        self.assertEqual(calc.add("//;\n1;2"), 3)
        self.assertEqual(calc.add("//|\n1|2|3"), 6)
        self.assertEqual(calc.add("//-\n10-20-30"), 60)
    

    def test_add_negative_number_throws_exception(self):
        calculator = StringCalculator()
        with self.assertRaises(ValueError) as context:
            calculator.add("1,-2,3")
        
        self.assertEqual(str(context.exception), "negatives not allowed: -2")
    
    def test_multiple_negative_numbers(self):
        calc = StringCalculator()
        with self.assertRaises(ValueError) as context:
            calc.add("1,-2,-3,4,-5")
        self.assertEqual(str(context.exception), "negatives not allowed: -2, -3, -5")
    

    def test_get_called_count(self):
        calc = StringCalculator()
        self.assertEqual(calc.get_called_count(), 0)
        calc.add("1,2")
        self.assertEqual(calc.get_called_count(), 1)
        calc.add("3,4,5")
        self.assertEqual(calc.get_called_count(), 2)
        with self.assertRaises(ValueError) as context:
            calc.add("1,-2,-3,4,-5")
        self.assertEqual(calc.get_called_count(), 3)
    

    def test_ignore_numbers_greater_than_1000(self):
        calc = StringCalculator()
        self.assertEqual(calc.add("2,1001"), 2)
        self.assertEqual(calc.add("1000,2000,3000"), 1000)
        self.assertEqual(calc.add("1,2,1001,1002,3"), 6)
        self.assertEqual(calc.add("1000"), 1000)
        self.assertEqual(calc.add("1001,1002,1003,1004"), 0)
    

    def test_multiple_delimiters(self):
        calc = StringCalculator()
        self.assertEqual(calc.add("//*%\n1*2%3"), 6)