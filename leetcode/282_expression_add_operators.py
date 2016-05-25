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
        numbers = [int(e) for e in num]
        numbers_length = len(num)


        if numbers_length == 0:
            return result

        PLUS_OPERATOR = 0
        MINUS_OPERATOR = 1
        MULTI_OPERATOR = 2
        JOINT_OPERATOR = 3

        searchStack = []
        path = str(numbers[0])
        value = numbers[0]
        
        """
        element content:
        * height, zero-based
        * operator
        * operand
        * current_value
        * current_path
        """
        searchStack.append([0, None, numbers[0], value, path])

        while len(searchStack) > 0:
            element = searchStack.pop()
            height = element[0]
            operator = element[1]
            operand = element[2]
            value = element[3]
            path = element[4]

            if operator == PLUS_OPERATOR:
                path += "+"
                path += str(operand)
                value += operand                
            elif operator == MINUS_OPERATOR:
                path += "-"
                path += str(operand)
                value -= operand
            elif operator == MULTI_OPERATOR:
                path += "*"                
                path += str(operand)
                value *= operand
            elif operator == JOINT_OPERATOR:
                value = value * 10 + operand
                path += str(operand)

            if height == (numbers_length - 1):
                if value == target:
                    result.append(path)
            elif height < (numbers_length - 1):
                next_height = height + 1
                next_index = numbers[next_height]
                searchStack.append([next_height, JOINT_OPERATOR, next_index, value, path])
                searchStack.append([next_height, MULTI_OPERATOR, next_index, value, path])
                searchStack.append([next_height, MINUS_OPERATOR, next_index, value, path])
                searchStack.append([next_height, PLUS_OPERATOR, next_index, value, path])
            
        return result

solution = Solution()
print(solution.addOperators("123", 6))
