"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left = 0 
        right = len(heights) - 1

        while left != right:
            if heights[left] >= heights[right]:
                temp_max_area = heights[right] * (right - left)
                right -= 1
            else:
                temp_max_area = heights[left] * (right - left)
                left += 1
            if temp_max_area > max_area:
                max_area = temp_max_area
        return max_area