"""
https://leetcode.com/problems/4sum/

Given an array `nums` of `n` integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

* 0 <= a, b, c, d < n
* a, b, c, and d are distinct.
* nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.


Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

Constraints:
* 1 <= nums.length <= 200
* -109 <= nums[i] <= 109
* -109 <= target <= 109
"""


class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        len_nums = len(nums)
        if len_nums < 4:
            return []

        retval = []
        for i in range(len_nums):
            for j in range(i + 1, len_nums):
                rest_value = target - nums[i] - nums[j]
                left = j + 1
                right = len_nums - 1
                while left < right:
                    sum_left_right_value = nums[left] + nums[right]
                    if rest_value == sum_left_right_value:
                        retval.append([nums[i], nums[j], nums[left], nums[right]])
                        left = left + 1
                    elif rest_value > sum_left_right_value:
                        left = left + 1
                    else:
                        right = right - 1

        def sort_list(result: list[list[int]]) -> list[list[int]]:
            retval = []
            for ret_ele in result:
                retval.append(sorted(ret_ele))
            retval.sort()
            return retval

        sorted_retval = sort_list(retval)
        uniq_retval = []
        [uniq_retval.append(item) for item in sorted_retval if item not in uniq_retval]

        return uniq_retval
