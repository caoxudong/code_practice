"""

Max Points on a Line 

Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

https://leetcode.com/problems/max-points-on-a-line/

"""

# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    def maxPoints(self, points):
      """
      :type points: List[Point]
      :rtype: int
      """
      length = len(points)
      if length < 3: 
        return length
      result = -1
      for i in range(length):
        slope = {'inf': 0}
        sameNum = 1

        for j in range(length):
          if i == j:
            continue
          elif points[i].x == points[j].x and points[i].y != points[j].y:
            slope['inf'] += 1
          elif points[i].x != points[j].x:
            k = 1.0 * (points[i].y - points[j].y) / (points[i].x - points[j].x)
            if k not in slope:
              slope[k] = 1
            else:
              slope[k] += 1
          else:
            sameNum += 1
        result = max(result, max(slope.values()) + sameNum)
      return result

        