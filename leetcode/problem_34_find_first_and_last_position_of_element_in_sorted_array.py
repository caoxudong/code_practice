"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/?utm_source=LCUS&utm_medium=ip_redirect&utm_campaign=transfer2china

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.

Example 1:
* Input: nums = [5,7,7,8,8,10], target = 8
* Output: [3,4]

Example 2:
* Input: nums = [5,7,7,8,8,10], target = 6
* Output: [-1,-1]

Example 3:
* Input: nums = [], target = 0
* Output: [-1,-1]

Constraints:
* 0 <= nums.length <= 105
* -109 <= nums[i] <= 109
* nums is a non-decreasing array.
* -109 <= target <= 109
"""


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        len_nums = len(nums)
        begin_left = 0
        end_left = len_nums - 1
        begin_right = 0
        end_right = len_nums - 1
        result_left = -1
        result_right = -1
        while begin_left <= end_left or begin_right <= end_right:
            mid_left = int((begin_left + end_left) / 2)
            mid_right = int((begin_right + end_right) / 2)
            if begin_left <= end_left and nums[mid_left] == target:
                result_left = mid_left
                end_left = mid_left - 1
            elif begin_right <= end_right and nums[mid_right] == target:
                result_right = mid_right
                begin_right = mid_right + 1
            elif (begin_left <= end_left and nums[mid_left] < target) or (
                begin_right <= end_right and nums[mid_right] < target
            ):
                if begin_left <= end_left and nums[mid_left] < target:
                    begin_left = mid_left + 1
                if begin_right <= end_right and nums[mid_right] < target:
                    begin_right = mid_right + 1
            else:
                if begin_left <= end_left:
                    end_left = mid_left - 1
                if begin_right <= end_right and nums[mid_right] >= target:
                    end_right = mid_right - 1

        return [result_left, result_right]
