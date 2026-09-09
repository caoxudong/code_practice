"""
https://leetcode.com/problems/search-a-2d-matrix/description/

You are given an m x n integer matrix matrix with the following two properties:
* Each row is sorted in non-decreasing order.
* The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
* Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
* Output: true

Example 2:
* Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
* Output: false

Constraints:
* m == matrix.length
* n == matrix[i].length
* 1 <= m, n <= 100
* -10^4 <= matrix[i][j], target <= 10^4
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix[0]) - 1

        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target:
                return True
            elif target > matrix[i][j]:
                i += 1
            else:
                j -= 1

        return False
