import unittest
import leetcode.problem_27_remove_element as problem


class UnitTestData:
    def __init__(
        self,
        nums: list[int] = [],
        val: int = 0,
        expected_nums: list[int] = [],
        expected_cnt: int = 0,
    ):
        self.nums = nums
        self.val = val
        self.expected_nums = expected_nums
        self.expected_cnt = expected_cnt


unittest_data = [
    UnitTestData(
        nums=[0, 1, 2, 2, 3, 0, 4, 2],
        val=2,
        expected_nums=[0, 1, 4, 0, 3, 0, 0, 0],
        expected_cnt=5,
    ),
    UnitTestData(
        nums=[3, 2, 2, 3],
        val=3,
        expected_nums=[2, 2, 0, 0],
        expected_cnt=2,
    ),
]


def assertNumsEqualWithoutOrder(
    result: list[int] = [], expected_cnt: int = 0, expected_nums: list[int] = []
):
    len_result = len(result)
    len_expected = len(expected_nums)

    if len_expected != len_result:
        raise AssertionError(
            "AssertionError, result is {}, expected is {}".format(result, expected_nums)
        )

    result_set: set = set()
    expected_set: set = set()

    for i in range(expected_cnt):
        result_set.add(result[i])
        expected_set.add(expected_nums[i])

    if result_set != expected_set:
        raise AssertionError(
            "AssertionError, result is {}, expected is {}".format(result, expected_nums)
        )


class TestSolution(unittest.TestCase):
    def test_removeElement(self):
        s = problem.Solution()
        for item in unittest_data:
            result = s.removeElement(item.nums, item.val)
            self.assertEqual(result, item.expected_cnt)
            assertNumsEqualWithoutOrder(
                item.nums, item.expected_cnt, item.expected_nums
            )
