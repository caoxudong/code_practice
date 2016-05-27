#!/usr/bin/env python

"""
Expression Add Operators

Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Examples: 
"123", 6 -> ["1+2+3", "1*2*3"] 
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []

https://leetcode.com/problems/expression-add-operators/
"""


class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """       
        result = []
        for i in range(1, len(num) + 1):
            if i == 1 or (i > 1 and num[0] != "0"): 
                self.search(num[i:], num[:i], int(num[:i]), int(num[:i]), result, target)
        return result

    def search(self, numbers_left, current_path, current_value, value_to_be_processed, result, target):
        if not numbers_left:
            if current_value == target:
                result.append(current_path)
            return
        for i in range(1, len(numbers_left)+1):
            value_str = numbers_left[:i]
            value = int(value_str)
            if i == 1 or (i > 1 and numbers_left[0] != "0"): 
                self.search(numbers_left[i:], current_path + "+" + value_str, current_value + value, value, result, target)
                self.search(numbers_left[i:], current_path + "-" + value_str, current_value - value, -value, result, target)
                self.search(numbers_left[i:], current_path + "*" + value_str, current_value - value_to_be_processed + value_to_be_processed * value, value_to_be_processed * value, result, target)

solution = Solution()
print(solution.addOperators("0105", 5))
