"""
A palindromic number reads the same both ways. 

The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import sys

def isPalindrome(number) :
    palindromeString = str(number)
    palindromeStringlength = len(palindromeString)
    flag = True
    for i in range(palindromeStringlength / 2):
        if palindromeString[i] != palindromeString[palindromeStringlength - i - 1]:
            flag = False
            break
    return flag    


maxNum=0
for i in range(500, 999):
    for j in range(500, 999):
        result = i * j
        if isPalindrome(result):
            if maxNum < result:
                maxNum = result

print(maxNum)
