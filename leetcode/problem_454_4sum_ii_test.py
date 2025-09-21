import unittest
import problem_454_4sum_ii as problem


class UnitTestData:
    def __init__(
        self,
        nums1: list[int] = [],
        nums2: list[int] = [],
        nums3: list[int] = [],
        nums4: list[int] = [],
        expected: int = 0,
    ):
        self.nums1 = nums1
        self.nums2 = nums2
        self.nums3 = nums3
        self.nums4 = nums4
        self.expected = expected


unittest_data = [
    UnitTestData(
        nums1=[1, 2],
        nums2=[-2, -1],
        nums3=[-1, 2],
        nums4=[0, 2],
        expected=2,
    ),
    UnitTestData(
        nums1=[0],
        nums2=[0],
        nums3=[0],
        nums4=[0],
        expected=1,
    ),
    UnitTestData(
        nums1=[-1, -1],
        nums2=[-1, 1],
        nums3=[-1, 1],
        nums4=[1, -1],
        expected=6,
    ),
]


class TestSolution(unittest.TestCase):
    def test_fourSumCount(self):
        s = problem.Solution()
        for item in unittest_data:
            result = s.fourSumCount(item.nums1, item.nums2, item.nums3, item.nums4)
            self.assertEqual(result, item.expected)
