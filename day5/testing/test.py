import unittest
import salary
import divideByZero
class testSalary(unittest.TestCase):
    def test_salary(self):
        result = salary.salary(1000)
        self.assertEqual(result, 1000)
class TestDivide(unittest.TestCase):

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divideByZero.divide_by_zero(10)
unittest.main()