#!/usr/bin/env python
#coding: utf-8

"""
https://leetcode.com/problems/spiral-matrix-ii/


Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = [([0] * n) for i in range(n)]
        
        DIRECTION_RIGHT = "RIGHT"
        DIRECTION_DOWN = "DOWN"
        DIRECTION_LEFT = "LEFT"
        DIRECTION_UP = "UP"
        direction = DIRECTION_RIGHT
        
        x, y, steps_count = 0, 0, 1
        max_steps_count = n * n
        
        while steps_count <= max_steps_count:
            result[x][y] = steps_count
            cache_x, cache_y = x, y
            
            if direction == DIRECTION_RIGHT:
                if y == (n - 1) or result[x][y + 1] != 0:
                    direction = DIRECTION_DOWN
                    x += 1
                else:
                    y += 1
            elif direction == DIRECTION_DOWN:
                if x == (n - 1) or result[x + 1][y] != 0:
                    direction = DIRECTION_LEFT
                    y -= 1
                else:
                    x += 1
            elif direction == DIRECTION_LEFT:
                if y == 0 or result[x][y - 1] != 0:
                    direction = DIRECTION_UP
                    x -= 1
                else:
                    y -= 1
            elif direction == DIRECTION_UP:
                if x == 0 or result[x - 1][y] != 0:
                    direction = DIRECTION_RIGHT
                    y += 1
                else:
                    x -= 1
            steps_count += 1
        
        return result

solution = Solution()
print(solution.generateMatrix(4))

