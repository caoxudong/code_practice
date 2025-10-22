"""
determin whether there is a path in 2d array which connects two point in the array.

e.g.
array is like:
[
    [0, 1, 0, 0, 0]
    [0, 1, 1, 0, 0]
    [0, 0, 1, 1, 0]
    [0, 0, 0, 1, 0]
    [0, 0, 1, 1, 0]
]
in this array, `0` means point not available, `1` means point awailable.
input, start point(0, 1), stop point(4, 3). In this array, path exsited.
"""


class Solution:
    def find_path_in_2d_array(
        self,
        arr: list[list[int]] = [],
        start_point: tuple[int, int] = (),
        stop_point: tuple[int, int] = (),
    ) -> bool:
        return False
