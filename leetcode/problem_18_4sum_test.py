import unittest
import problem_18_4sum as problem
from functools import cmp_to_key


class TestSolution(unittest.TestCase):
    def test_fourSum(self):
        s = problem.Solution()

        class UnitTestData:
            def __init__(
                self,
                input: list[int] = [],
                target: int = 0,
                expected: list[list[int]] = [],
            ):
                self.input = input
                self.target = target
                self.expected = expected

        def sort_list(result: list[list[int]]) -> list[list[int]]:
            retval = []
            for ret_ele in result:
                retval.append(sorted(ret_ele))
            retval.sort()
            return retval

        unittest_data = [
            UnitTestData(
                input=[1, 0, -1, 0, -2, 2],
                target=0,
                expected=[[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]],
            ),
            UnitTestData(
                input=[2, 2, 2, 2, 2],
                target=8,
                expected=[[2, 2, 2, 2]],
            ),
            UnitTestData(
                input=[-5, 5, 4, -3, 0, 0, 4, -2],
                target=4,
                expected=[[-5, 0, 4, 5], [-3, -2, 4, 5]],
            ),
            UnitTestData(
                input=[1, 0, -1, 0, -2, 2],
                target=0,
                expected=[[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]],
            ),
            UnitTestData(
                input=[-3, -2, -1, 0, 0, 1, 2, 3],
                target=0,
                expected=[
                    [-3, -2, 2, 3],
                    [-3, -1, 1, 3],
                    [-3, 0, 0, 3],
                    [-3, 0, 1, 2],
                    [-2, -1, 0, 3],
                    [-2, -1, 1, 2],
                    [-2, 0, 0, 2],
                    [-1, 0, 0, 1],
                ],
            ),
        ]

        for item in unittest_data:
            result = s.fourSum(item.input, item.target)
            self.assertListEqual(sort_list(result), sort_list(item.expected))
