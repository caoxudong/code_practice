"""
https://leetcode.com/problems/subsets/description/

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.


Example 1:
* Input: nums = [1,2,3]
* Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
* Input: nums = [0]
* Output: [[],[0]]


Constraints:
* 1 <= nums.length <= 10
* -10 <= nums[i] <= 10
* All the numbers of nums are unique.
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        retval = []

        def get_combinations(nums, k):
            res = []

            def backtrack(start, path):
                if len(path) == k:
                    res.append(path.copy())
                    return
                for i in range(start, len(nums)):
                    path.append(nums[i])
                    backtrack(i + 1, path)
                    path.pop()

            backtrack(0, [])
            return res

        nums_len = len(nums)
        for i in range(nums_len + 1):
            retval.extend(get_combinations(nums, i))
        return retval
