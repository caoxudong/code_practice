import unittest
import leetcode.problem_26_remove_duplicates_from_sorted_array as problem


class UnitTestData:
    def __init__(
        self, nums: list[int] = [], expected_nums: list[int] = [], expected_cnt: int = 0
    ):
        self.nums = nums
        self.expected_nums = expected_nums
        self.expected_cnt = expected_cnt


unittest_data = [
    UnitTestData(nums=[1, 1, 2], expected_nums=[1, 2, 0], expected_cnt=2),
    UnitTestData(
        nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
        expected_nums=[0, 1, 2, 3, 4, 0, 0, 0, 0, 0],
        expected_cnt=5,
    ),
    UnitTestData(
        nums=[-1, 0, 0, 0, 0, 3, 3],
        expected_nums=[-1, 0, 3, 0, 0, 0, 0],
        expected_cnt=3,
    ),
]


def assertNumsEqual(
    result: list[int] = [], expected_cnt: int = 0, expected_nums: list[int] = []
):
    len_result = len(result)
    len_expected = len(expected_nums)

    if len_expected != len_result:
        raise AssertionError(
            "AssertionError, result is {}, expected is {}".format(result, expected_nums)
        )

    for i in range(expected_cnt):
        if result[i] != expected_nums[i]:
            raise AssertionError(
                "AssertionError, result is {}, expected is {}".format(
                    result, expected_nums
                )
            )


class TestSolution(unittest.TestCase):
    def test_removeDuplicates(self):
        s = problem.Solution()
        for item in unittest_data:
            result = s.removeDuplicates(item.nums)
            self.assertEqual(result, item.expected_cnt)
            assertNumsEqual(item.nums, item.expected_cnt, item.expected_nums)
