import unittest
import leetcode.problem_88_merge_sorted_array as problem


class UnitTestData:
    def __init__(self, nums1: list[int], m: int, nums2: list[int], n: int, expected: list[int]):
        self.nums1 = nums1
        self.m = m
        self.nums2 = nums2
        self.n = n
        self.expected = expected


unittest_data = [
    UnitTestData(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3, expected=[1, 2, 2, 3, 5, 6]),
    UnitTestData(nums1=[1], m=1, nums2=[], n=0, expected=[1]),
    UnitTestData(nums1=[0], m=0, nums2=[1], n=1, expected=[1]),
    UnitTestData(nums1=[2, 0], m=1, nums2=[1], n=1, expected=[1, 2]),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_88_merge(self):
        for item in unittest_data:
            solution = problem.Solution()
            solution.merge(item.nums1, item.m, item.nums2, item.n)
            self.assertEqual(item.nums1, item.expected)
