import unittest
from solution import calculate_floor


class Test(unittest.TestCase):

	def sample_test_1(self):
		self.assertEqual(2, calculate_floor('UUDU'))

	def sample_test_2(self):
		self.assertEqual(-4, calculate_floor('DDDD'))

print(calculate_floor('UUDU'),calculate_floor('DDDD'))