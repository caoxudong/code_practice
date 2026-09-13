from typing import List
import unittest
import leetcode.problem_80_remove_duplicates_from_sorted_array_II as problem


class UnitTestData:
    def __init__(self, nums: List[int], expected_num: int, expected_list: List[int]):
        self.nums = nums
        self.expected_num = expected_num
        self.expected_list = expected_list


unittest_data = [
    UnitTestData(nums=[1, 1, 1, 2, 2, 3], expected_num=5, expected_list=[1, 1, 2, 2, 3, None]),
    UnitTestData(nums=[0, 0, 1, 1, 1, 1, 2, 3, 3], expected_num=7, expected_list=[0, 0, 1, 1, 2, 3, 3, None, None]),
]

class TestSolution(unittest.TestCase):
    def test_leetcode_80_remove_duplicates(self):
        s = problem.Solution()
        for item in unittest_data:
            nums_copy = item.nums.copy()  # Create a copy to avoid modifying the original list
            retval = s.removeDuplicates(nums_copy)
            self.assertEqual(retval, item.expected_num)
            self.assertEqual(nums_copy[:retval], item.expected_list[:retval])
