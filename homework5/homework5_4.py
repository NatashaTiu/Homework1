import unittest
from homework5.homework5_1 import ITEmployee


class TestItEmployee(unittest.TestCase):
    def setUp(self):
        self.test_it_spec = ITEmployee("Vasya Pupkin", 1985, "Engineer", 2, 2500)

    def test_name(self):
        self.assertEqual(self.test_it_spec.get_name(), "Vasya")

    def test_surname(self):
        self.assertEqual(self.test_it_spec.get_surname(), "Pupkin")

    def test_position(self):
        self.assertEqual(self.test_it_spec.checking_position(), "Junior Engineer")

    def test_raise_salary(self):
        self.assertEqual(self.test_it_spec.raise_salary(350), 2850)

    # def test_add_skills(self):
    #     res = self.test_it_spec.add_skills("smth", "smth1", "smth2")
    #     self.assertEqual(res, "smth", "smth1", "smth2")


if __name__ == "__main__":
    unittest.main()