"""
给定数组，找出该数组中最大的连续子数组之和

e.g.
input:  5, -3, 2, 7, -5, 3, 9, -3
output: 5, -3, 2, 7, -5, 3, 9
"""


class Solution:
    def max_sub_array(self, nums: list[int] = []) -> list[int]:
        if len(nums) == 0:
            return []

        max_sum_list = []
        max_sum = float("-inf")
        current_sum_list = []
        current_sum = 0

        for tmp_num in nums:
            current_sum += tmp_num
            current_sum_list.append(tmp_num)

            if current_sum > max_sum:
                max_sum = current_sum
                max_sum_list = current_sum_list.copy()

            if current_sum < 0:
                current_sum = 0
                current_sum_list = []

        return max_sum_list
