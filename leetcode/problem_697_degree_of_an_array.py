"""
https://leetcode.com/problems/degree-of-an-array/description/


Given a non-empty array of non-negative integers `nums`, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
* Input: nums = [1,2,2,3,1]
* Output: 2
* Explanation:
    * The input array has a degree of 2 because both elements 1 and 2 appear twice.
    * Of the subarrays that have the same degree:
        * [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
    * The shortest length is 2. So return 2.

Example 2:
* Input: nums = [1,2,2,3,1,4,2]
* Output: 6
* Explanation:
    * The degree is 3 because the element 2 is repeated 3 times.
    * So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.

Constraints:
* `nums.length` will be between 1 and 50,000.
* `nums[i]` will be an integer between 0 and 49,999.
"""


class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        degree_dict: dict[int, int] = {}
        for i in nums:
            if i in degree_dict.keys():
                degree_dict[i] += 1
            else:
                degree_dict[i] = 1

        max_nums: list[int] = []
        max_degree = 0
        for i in degree_dict.keys():
            tmp_degree = degree_dict[i]
            if tmp_degree > max_degree:
                max_nums = [i]
                max_degree = tmp_degree
            elif tmp_degree == max_degree:
                max_nums.append(i)
            else:
                continue

        retval = len(nums)
        for i in max_nums:
            min_index = len(nums)
            max_index = 0
            for index in range(len(nums)):
                if i == nums[index]:
                    min_index = min(min_index, index)
                    max_index = max(max_index, index)
            retval = min(retval, max_index - min_index + 1)
        return retval
