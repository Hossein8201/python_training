import unittest
import sys
sys.path.append('../Initial_project')
from source import Foo


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.f = Foo()

    def test_1(self):
        self.assertEqual(self.f.x, 0)

    def test_2(self):
        self.f.x = 9
        self.assertEqual(self.f.x, 9)
        self.f.x = 0
        self.assertEqual(self.f.x, 0)
        self.f.x = 1
        self.assertEqual(self.f.x, 1)
        

if __name__ == '__main__':
    unittest.main()