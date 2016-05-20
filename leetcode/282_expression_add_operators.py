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
        numbersLength = len(num)
        
        PLUS_OPERATOR = 0
        MINUS_OPERATOR = 1
        MULTI_OPERATOR = 2
        
        searchStack = []
        searchStack.append([0, None, numbers[0]])
        path = str(numbers[0])

        value = 0
        while len(searchStack) > 0 :
            element = searchStack.pop()
            height = element[0]
            operator = element[1]
            operand = element[2]
            
            if operator == PLUS_OPERATOR:
                path += "+"
                value += value + operand
                path += str(operator)            
            elif operator == MINUS_OPERATOR:
                path += "-"
                value += value - operand
                path += str(operator)
            elif operator == MULTI_OPERATOR:
                path += "*"
                value += value * operand
                path += str(operator)
            
            if height == (numbersLength - 1):
                print(path)
                if value == target:
                    result.append(path)
            else:
                if height < (numbersLength - 1):
                    nextHeight = height + 1
                    next = numbers[nextHeight]
                    searchStack.append([nextHeight, PLUS_OPERATOR, next])
                    searchStack.append([nextHeight, MINUS_OPERATOR, next])
                    searchStack.append([nextHeight, MULTI_OPERATOR, next])
                
        return result

solution = Solution()
print(solution.addOperators("123", 6))
            