#!/usr/bin/env python
#coding: utf-8

"""
https://leetcode.com/problems/spiral-matrix/


Given a matrix of m * n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

You should return [1,2,3,6,9,8,7,4,5].
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        if n == 0:
            return []

        DIRECTION_RIGHT = "RIGHT"
        DIRECTION_DOWN = "DOWN"
        DIRECTION_LEFT = "LEFT"
        DIRECTION_UP = "UP"
        direction = DIRECTION_RIGHT
        
        result = []
        path_flag = [([0] * n) for i in range(m)]
        x, y, steps_count = 0, 0, 0
        max_steps_count = m * n
        
        while steps_count < max_steps_count:
            path_flag[x][y] = 1
            cache_x, cache_y = x, y
            result.append(matrix[cache_x][cache_y])
            
            if direction == DIRECTION_RIGHT:
                if y == (n - 1) or path_flag[x][y + 1] == 1:
                    direction = DIRECTION_DOWN
                    x += 1
                else:
                    y += 1
            elif direction == DIRECTION_DOWN:
                if x == (m - 1) or path_flag[x + 1][y] == 1:
                    direction = DIRECTION_LEFT
                    y -= 1
                else:
                    x += 1
            elif direction == DIRECTION_LEFT:
                if y == 0 or path_flag[x][y - 1] == 1:
                    direction = DIRECTION_UP
                    x -= 1
                else:
                    y -= 1
            elif direction == DIRECTION_UP:
                if x == 0 or path_flag[x - 1][y] == 1:
                    direction = DIRECTION_RIGHT
                    y += 1
                else:
                    x -= 1
            steps_count += 1
        
        return result

solution = Solution()
print(solution.spiralOrder([[3],[2]]))
