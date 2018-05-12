import unittest
from motif import non_contiguous_motif
from hourly_employee import HourlyEmployee
from salaried_employee import SalariedEmployee

class FinalExamTest(unittest.TestCase):

    def test_non_contiguous_motif(self):
        list1 = ['A', 'C','G','T','A','C','G','T','G','A','C','G']
        str1 = 'GTA'

        self.assertEqual(3,8,10, non_contiguous_motif(str1, list1))

    def test_HourlyEmployee_calculate(self):
        
        self.assertEqual(800, HourlyEmployee.calculate(10, 80))

    def test_SalariedEmployee_calculate(self):
        
        self.assertEqual(10000, SalariedEmployee.calculate(260000))

unittest.main(verbosity=2)
