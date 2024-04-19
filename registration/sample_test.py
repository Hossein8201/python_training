import unittest
import sys
sys.path.append('../Initial_project')
from source import check_registration_rules


class TestAll(unittest.TestCase):

    def test_valid_inputs(self):
        output = check_registration_rules(username='password', sadegh='He3@lsa', quera='kLS45@l$')
        self.assertListEqual(['username', 'sadegh'], output)

    def test_invalid_inputs(self):
        output = check_registration_rules(saeed='1234567', ab='afj$L12')
        self.assertListEqual([], output)


if __name__ == '__main__':
    unittest.main()
