"""
https://leetcode.com/problems/3sum/

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        nums_count = len(nums)
        result = []
        for i in range(nums_count - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = nums_count - 1

            while j < k:
                sum_result = nums[i] + nums[j] + nums[k]
                if sum_result == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif sum_result > 0:
                    k -= 1
                else:
                    j += 1
        return result


if __name__ == "__main__":
    params = [-1, 0, 1, 2, -1, -4]
    s = Solution()
    print(s.threeSum(params))
