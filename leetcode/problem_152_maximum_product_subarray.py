"""
https://leetcode.com/problems/maximum-product-subarray/description/

Given an integer array `nums`, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Note that the product of an array with a single element is the value of that element.


Example 1:
* Input: nums = [2,3,-2,4]
* Output: 6
* Explanation: [2,3] has the largest product 6.

Example 2:
* Input: nums = [-2,0,-1]
* Output: 0
* Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Constraints:
* 1 <= nums.length <= 2 * 104
* -10 <= nums[i] <= 10
* The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
"""


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        retval: int = nums[0]
        max_product: int = retval
        min_product: int = retval

        for i in nums[1:]:
            tmp: int = max_product
            max_product = max(i, max_product * i, min_product * i)
            min_product = min(i, tmp * i, min_product * i)

            if max_product > retval:
                retval = max_product

        return retval
