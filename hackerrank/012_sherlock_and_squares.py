#!/bin/python3

"""
https://www.hackerrank.com/challenges/sherlock-and-squares?h_r=next-challenge&h_v=zen

Watson给了Sherlock两个整数A和_B_，现在Watson问Sherlock他是否可以计算A和_B_之间（包含A和 B）的完全平方数的个数。

完全平方数指的是任何整数的平方。例如，1， 4， 9， 16是完全平方数，因为它们分别是1， 2， 3，4的平方。

输入格式 
第一行包含一个整数T, 测试数据的组数。 后面跟T组测试数据，每组占一行。 
每组数据是两个整数A和_B_。

输出格式 
对每组测试数据，输出一行结果。

约束条件 
1 ≤ T ≤ 100 
1 ≤ A ≤ B ≤ 1000000000

输入样例

2
3 9
17 24
输出样例

2
0
解释n 
第一组测试数据中， 4和9是完全平方数。 第二组测试数据中， 17和24之间（包含17和24），没有完全平方数。
"""

import sys
import math

t = int(input().strip())
for a0 in range(t):
    a_and_b = input().strip()
    a_and_b_array = a_and_b.split(" ")
    a = int(a_and_b_array[0])
    b = int(a_and_b_array[1])
    sqrt_a = math.sqrt(a)
    sqrt_b = math.sqrt(b)
    ceil_sqrt_a = math.ceil(sqrt_a)
    floor_sqrt_b = math.floor(sqrt_b)
    print(floor_sqrt_b - ceil_sqrt_a + 1)
    
    