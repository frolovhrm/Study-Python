import unittest
from exercise11_3 import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.first_test = Employee('Ivan', 'Ivanov', 5000)
        self.arg = 5001

    def test_give_default_raise(self):
        self.assertEqual(self.first_test.full_salary + 5000, self.first_test.give_raise())



if __name__ == '__main__':
    unittest.main()
