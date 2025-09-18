"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:
Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
"""

class Solution:
    def innerLengthOfLIS(self, nums, prev_pos, cur_pos, middle_result):
        if cur_pos == len(nums):
            return 0

        middle_result_value = middle_result[prev_pos + 1][cur_pos]
        if middle_result_value >= 0:
            return middle_result_value

        including = 0
        if prev_pos < 0 or nums[cur_pos] > nums[prev_pos]:
                including = self.innerLengthOfLIS(nums, cur_pos, cur_pos + 1, middle_result) + 1

        not_including = self.innerLengthOfLIS(nums, prev_pos, cur_pos + 1, middle_result)
        middle_result_value = max(including, not_including)
        middle_result[prev_pos + 1][cur_pos] = middle_result_value

        return middle_result_value

    def lengthOfLIS(self, nums):
        middle_result = [[-1] * len(nums) for i in range(len(nums) + 1)]
        return self.innerLengthOfLIS(nums, -1, 0, middle_result)

if __name__ == "__main__":
    tests = [
        # ([10,9,2,5,3,7,101,18], 4),
        # ([4,10,4,3,8,9], 3),
        ([10,9,2,5,3,4], 3)
    ]
    s = Solution()
    for t in tests:
        print(t[0], t[1], s.lengthOfLIS(t[0]))