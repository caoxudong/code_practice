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

from operator import truediv


class Solution:
    def find_path_in_2d_array(
        self,
        arr: list[list[int]] = [],
        start_point: tuple[int, int] = (),
        stop_point: tuple[int, int] = (),
    ) -> bool:

        if start_point == stop_point:
            return True

        visited: set[tuple[int, int]] = set()
        stack: list[tuple[int, int]] = []
        stack.append(start_point)

        retval = False
        while len(stack) != 0:
            cur_point = stack.pop()
            if cur_point == stop_point:
                retval = True
                break

            if cur_point in visited:
                continue

            visited.add(cur_point)

            point_up = (cur_point[0] - 1, cur_point[1])
            point_down = (cur_point[0] + 1, cur_point[1])
            point_left = (cur_point[0], cur_point[1] - 1)
            point_right = (cur_point[0], cur_point[1] + 1)
            if cur_point[0] == 0:
                point_up = None
            if cur_point[0] == len(arr) - 1:
                point_down = None
            if cur_point[1] == 0:
                point_left = None
            if cur_point[1] == len(arr[0]) - 1:
                point_right = None

            if point_up != None and arr[point_up[0]][point_up[1]] == 1:
                stack.append(point_up)
            if point_down != None and arr[point_down[0]][point_down[1]] == 1:
                stack.append(point_down)
            if point_left != None and arr[point_left[0]][point_left[1]] == 1:
                stack.append(point_left)
            if point_right != None and arr[point_right[0]][point_right[1]] == 1:
                stack.append(point_right)

        return retval
