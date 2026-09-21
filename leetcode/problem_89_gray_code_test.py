import unittest
import leetcode.problem_89_gray_code as problem


class UnitTestData:
    def __init__(self, n: int, expected: list[int]):
        self.n = n
        self.expected = expected


unittest_data = [UnitTestData(n=2, expected=[0, 1, 3, 2]), UnitTestData(n=1, expected=[0, 1])]


class TestSolution(unittest.TestCase):
    def test_leetcode_89_grayCode(self):
        for item in unittest_data:
            solution = problem.Solution()
            retval = solution.grayCode(item.n)
            self.assertListEqual(item.expected, retval)
