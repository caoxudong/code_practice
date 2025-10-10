import unittest
import others.max_sub_array as problem


class UnitTestData:
    def __init__(
        self, nums: list[int] = [], expected: list[int] = [], expected_num: int = 0
    ):
        self.nums = nums
        self.expected = expected
        self.expected_num = 18


unittest_data = [
    UnitTestData(
        nums=[5, -3, 2, 7, -5, 3, 9, -3],
        expected=[5, -3, 2, 7, -5, 3, 9],
        expected_num=18,
    ),
]


class TestSolution(unittest.TestCase):
    def test_max_sub_array(self):
        s = problem.Solution()
        for item in unittest_data:
            result = s.max_sub_array(item.nums)
            self.assertListEqual(result, item.expected)
