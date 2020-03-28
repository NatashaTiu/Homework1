import unittest
from homework5.homework5_functions_to_test import check_isIntercalary, check_is_triangle, check_type_triangle

class TestIsYearLeap(unittest.TestCase):
    def test_leap_year(self):
        year = 2000
        res = check_isIntercalary(year)
        self.assertTrue(res, "True")


class TestIsTriangle(unittest.TestCase):
    def test_is_triangle(self):
        a = 3
        b = 4
        c = 5
        res = check_is_triangle(a, b, c)
        self.assertTrue(res, "True")


class TestTypeOfTriangle(unittest.TestCase):
    def test_type(self):
        a = 4
        b = 4
        c = 5
        res = check_type_triangle(a, b, c)
        self.assertTrue(res, "Equilateral triangle.")

if __name__ == "__main__":
    unittest.main()