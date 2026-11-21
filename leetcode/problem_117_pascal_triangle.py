"""
https://leetcode.com/problems/pascals-triangle/


You are given an integer numRows.

Return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it and the first and last number on each row must be equal to 1, as shown below:

Example 1:
* Input: numRows = 5
* Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:

* Input: numRows = 1
* Output: [[1]]

Constraints:
* 1 <= numRows <= 30
"""


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        retval = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = retval[i - 1][j - 1] + retval[i - 1][j]
            retval.append(row)
        return retval
