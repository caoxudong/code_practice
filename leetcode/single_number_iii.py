"""
Single Number III 

https://leetcode.com/problems/single-number-iii/

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

"""

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def singleNumber(self, nums):
        x = 0
        y = 0
        tempXORValue = 0
        
        for i in nums: 
            tempXORValue ^= i

        diff = (tempXORValue & (tempXORValue -  1)) ^ tempXORValue

        for i in nums:
            if diff & i:
                x ^= i
            else:
                y ^= i

        return result

        