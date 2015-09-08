#!/usr/bin/env python

"""
First Bad Version 

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

https://leetcode.com/problems/first-bad-version/
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
  def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    if n == 0 :
      return 0

    if n == 1 :
      if isBadVersion(1) :
        return 1
      else :
        return 0

    if n == 2 :
      if isBadVersion(1) :
        return 1
      else :
        return 2

    if n == 3 :
      if isBadVersion(2) :
        if isBadVersion(1) :
          return 1
        else :
          return 2
      else :
        return 3

    begin = 1
    end = n    
    while begin <= end :      
      middle = (end + begin) // 2
      print(begin, middle, end)
      if isBadVersion(middle) :
        if not isBadVersion(middle - 1) :
          return middle
        else :
          end = middle - 1
      else :
        if isBadVersion(middle + 1) :
          return middle + 1
        else :
          begin = middle + 1
      print(begin, end)
    return 0

def isBadVersion(n) :
  global bad
  if n >= bad :
    return True
  else :
    return False

if __name__ == "__main__" :
  count = 4
  bad = 1
  solution = Solution()
  print(solution.firstBadVersion(count))