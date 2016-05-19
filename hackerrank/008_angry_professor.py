#!/bin/python3

"""
https://www.hackerrank.com/challenges/angry-professor

教授正在为一个包含N个学生的班级讲授离散数学。他对这些学生缺乏纪律性很不满并决定如果课程开始后，上课的人数小于K就取消这门课程。

给定每个学生的到达时间，你的任务是找出该课程是否被取消。

Input Format

输入第一行包含T，后面测试数据的组数。 
每组测试数据包含2行。 每组测试数据的第一行包含两个空格分隔的整数N和K。 
下一行包含N个空格分隔的整数，表示每个学生的到达时间。

如果一个学生的到达时间是非正整数(<=0)，则该学生在上课前进入教室。如果一个学生的到达时间是正整数(>=0)，则该学生在上课后进入教室。 在时刻0开始上课。 
如果一个学生在时刻0进入教室，他被认为在上课前进入教室。

约束条件

1<=T<=10
1<=N<=1000
1<=K<=N
 
到达时间的绝对值不超过100。

Output Format

对每组测试数据，如果该门课程被取消 ，则输出YES，否则输出NO。

Sample Input

2
4 3
-1 -3 4 2
4 2
0 -1 2 1

Sample Output

YES
NO

Explanation

对第一组测试数据，K = 3，即教授希望至少3个学生在教室。但只有两个学生准时到达( -3, -1 )，因此该课程被取消。 
对第二组测试数据，K = 2，即教授希望至少2个学生在教室，并且有两个学生准时到达(0, -1)，因此该课程不被取消。
"""

import sys

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    
    presentCount = 0
    for i in range(n):
        if a[i] <= 0:
            presentCount += 1
    
    if presentCount < k:
        print("YES")
    else:
        print("NO")
