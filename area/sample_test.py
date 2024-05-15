import unittest
import sys
sys.path.append('../Initial_project')
from solution import get_func

class ScoreListTest(unittest.TestCase):

    def _check(self, ls, ins, ls_j):
        ls_judge = ls_j
        ls_user = get_func(ls)
        self.assertEqual(len(ls_judge), len(ls_user))
        ind = 0
        for j, u in zip(ls_judge, ls_user):
            self.assertAlmostEqual(j, u(*ins[ind]), delta=1e-5)
            ind = ind + 1

    def test_circle(self):
        self._check(['circle', 'circle', 'circle'], [(12,), (4,), (5.5,)], [452.3893421169302, 50.26548245743669, 95.03317777109125])


    def test_triangle(self):
        self._check(['triangle', 'triangle', 'triangle'], [(12,43), (4.5,3), (5.5,13)], [258.0, 6.75, 35.75])
        
        
        
if __name__ == '__main__':
    unittest.main()