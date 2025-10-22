import unittest
import others.find_path_in_2d_array as problem


class UnitTestData:
    def __init__(
        self,
        arr: list[list[int]] = [],
        start_point: tuple[int, int] = (),
        stop_point: tuple[int, int] = (),
        expected: bool = False,
    ):
        self.arr = arr
        self.start_point = start_point
        self.stop_point = stop_point
        self.expected = expected


unittest_data = [
    UnitTestData(
        arr=[
            [0, 1, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 1, 1, 0],
        ],
        start_point=(0, 1),
        stop_point=(4, 3),
        expected=True,
    ),
    UnitTestData(
        arr=[
            [0, 1, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 1, 1, 0],
        ],
        start_point=(2, 4),
        stop_point=(4, 2),
        expected=False,
    ),
]


class TestSolution(unittest.TestCase):
    def test_find_path_in_2d_array(self):
        s = problem.Solution()
        for item in unittest_data:
            result = s.find_path_in_2d_array(
                item.arr, item.start_point, item.stop_point
            )
            self.assertEqual(result, item.expected)
