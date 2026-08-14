"""
https://leetcode.com/problems/permutations-ii/description/


Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:
* Input: nums = [1,1,2]
* Output:
    [
        [1,1,2],
        [1,2,1],
        [2,1,1]
    ]

Example 2:
* Input: nums = [1,2,3]
* Output:
    [
        [1,2,3],
        [1,3,2],
        [2,1,3],
        [2,3,1],
        [3,1,2],
        [3,2,1]
    ]

Constraints:
* 1 <= nums.length <= 8
* -10 <= nums[i] <= 10
"""

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        stack = [([], nums.copy())]
        while stack:
            path, remain = stack.pop()
            if not remain:
                if path not in res:
                    res.append(path)
                continue
            for i in reversed(range(len(remain))):
                new_path = path + [remain[i]]
                new_remain = remain[:i] + remain[i + 1 :]
                stack.append((new_path, new_remain))
        return res
