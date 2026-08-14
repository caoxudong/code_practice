"""
https://leetcode.com/problems/permutations/description/


Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
* Input: nums = [1,2,3]
* Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
* Input: nums = [0,1]
* Output: [[0,1],[1,0]]

Example 3:
* Input: nums = [1]
* Output: [[1]]

Constraints:
* 1 <= nums.length <= 6
* -10 <= nums[i] <= 10
* All the integers of nums are unique.
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def inner_permute(inner_nums: List[int]) -> List[List[int]]:
            if len(inner_nums) == 1:
                return [inner_nums]
            else:
                nums_head = inner_nums[0]
                nums_tails = inner_nums[1:]
                inner_permute_retval = inner_permute(nums_tails)
                retval = []
                for tmp_list in inner_permute_retval:
                    for i in range(len(tmp_list)):
                        new_list = tmp_list.copy()
                        new_list.insert(i, nums_head)
                        retval.append(new_list)
                    new_list = tmp_list.copy()
                    new_list.append(nums_head)
                    retval.append(new_list)
                return retval

        return inner_permute(nums)
