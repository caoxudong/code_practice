#!/bin/python3

"""
https://www.hackerrank.com/challenges/staircase?h_r=next-challenge&h_v=zen

Your teacher has given you the task of drawing a staircase structure. Being an expert programmer, you decided to make a program to draw it for you instead. Given the required height, can you print a staircase as shown in the example?

Input 
You are given an integer  depicting the height of the staircase.

Output 
Print a staircase of height  that consists of # symbols and spaces. For example for , here's a staircase of that height:

     #
    ##
   ###
  ####
 #####
######
Note: The last line has 0 spaces before it.
"""


import sys


n = int(input().strip())

for i in range(n):
    for j in range(n - 1 - i):
        print(" ", end='')
    for j in range(i + 1):
        print("#", end='')
    print()