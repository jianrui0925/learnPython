import unittest
from Employee import Employee

class test_Employee(unittest.TestCase):
    def setUp(self):
        self.my_employee = Employee('a','b',10000)

    def test_default_give_raise(self):
        # my_employee = Employee('a','b',10000)
        self.my_employee.give_raise()
        salary =self.my_employee.annual_salary
        self.assertEqual(salary,15000)
    def test_give_custom_raise(self):
        self.my_employee.give_raise(10000)
        salary = self.my_employee.annual_salary
        self.assertEqual(salary,20000)

if __name__ == '__main__':
    unittest.main()
        