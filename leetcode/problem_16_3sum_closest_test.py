import unittest
import leetcode.problem_16_3sum_closest as problem_16_3sum_closest


class TestSolution(unittest.TestCase):
    def test_threeSumClosest(self):
        s = problem_16_3sum_closest.Solution()
        self.assertEqual(s.threeSumClosest([-1, 2, 1, -4], 1), 2)
        self.assertEqual(s.threeSumClosest([0, 0, 0], 1), 0)
        self.assertEqual(s.threeSumClosest([4, 0, 5, -5, 3, 3, 0, -4, -5], -2), -2)
