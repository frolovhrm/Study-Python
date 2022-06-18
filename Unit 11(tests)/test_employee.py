import unittest
from exercise11_3 import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.pers_test = Employee('Ivan', 'Ivanov', 5000)
        self.arg = 5001

    def test_give_default_raise(self):
        self.assertEqual(self.pers_test.full_salary + 5000, self.pers_test.give_raise())


    def test_give_default_raise_arg(self):
        self.assertEqual(self.pers_test.full_salary + self.arg, self.pers_test.give_raise(self.arg))




if __name__ == '__main__':
    unittest.main()
