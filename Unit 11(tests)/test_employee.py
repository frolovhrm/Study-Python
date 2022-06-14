import unittest
from exercise11_3 import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.first_test = Employee('Ivan', 'Ivanov', 5000)
        self.res = self.first_test
    def test_give_default_raise(self):
        self.assertEqual(self.first_test.full_salary + 5000, self.res)


if __name__ == '__main__':
    unittest.main()
