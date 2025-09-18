"""

leetcode    https://leetcode.com/problems/reverse-integer/

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321


"""

class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        xstr = str(x)
        length = len(xstr)
        if x < 0:
            xstr = xstr[length:0:-1]
            result = int(xstr) * -1
        else:
            xstr = xstr[::-1]
            result = int(xstr)
        if result > 2147483647:
            result = 0
        if result < -2147483648:
            result = 0
        return result