#!/bin/python3

"""
https://www.hackerrank.com/challenges/bear-and-workbook?h_r=next-challenge&h_v=zen

Lisa just got a new math workbook. A workbook contains exercise problems, grouped into chapters.

* There are n chapters in Lisa's workbook, numbered from 1 to n.
* The i-th chapter has ti problems, numbered from 1 to ti.
* Each page can hold up to k problems. There are no empty pages or unnecessary spaces, so only the last page of a chapter may contain fewer than k problems.
* Each new chapter starts on a new page, so a page will never contain problems from more than one chapter.
* The page number indexing starts at 1.

Lisa believes a problem to be special if its index (within a chapter) is the same as the page number where it's located. Given the details for Lisa's workbook, can you count its number of special problems?

Note: See the diagram in the Explanation section for more details.

Input Format

The first line contains two integers n and k — the number of chapters and the maximum number of problems per page respectively. 
The second line contains n integers t1, t2,...,tn, where ti denotes the number of problems in the i-th chapter.

Contraints

1 <= n,k,ti <= 100

Output Format

Print the number of special problems in Lisa's workbook.

Sample Input

5 3  
4 2 6 1 10

Sample Output

4

Explanation

The diagram below depicts Lisa's workbook with n = 5 chapters and a maximum of k = 3 problems per page. Special problems are outlined in red, and page numbers are in yellow squares.

    +-Chap1+--------+ +-Chap1+---+ +-Chap2+---+ +-Chap3+---+ +-Chap3+--------+
    |               | |          | |          | |          | |               |
    | Problem1(RED) | | Problem4 | | Problem1 | | Problem1 | | Problem4      |
    | Problem2      | |          | | Problem2 | | Problem2 | | Problem5(RED) |
    | Problem3      | |          | |          | | Problem3 | | Problem6      |
    |               | |          | |          | |          | |               |
    +---------------+ +----------+ +----------+ +----------+ +---------------+
         P1                P2           P3           P4           P5

    +-Chap4----+ +-Chap5----+ +-Chap5----+ +-Chap5---------+ +-Chap5----------+
    |          | |          | |          | |               | |                |
    | Problem1 | | Problem1 | | Problem4 | | Problem7      | | Problem10(RED) |
    |          | | Problem2 | | Problem5 | | Problem8      | |                |
    |          | | Problem3 | | Problem6 | | Problem9(RED) | |                |
    |          | |          | |          | |               | |                |
    |          | |          | |          | |               | |                |
    +----------+ +----------+ +----------+ +---------------+ +----------------+
         P6           P7           P8           P9                P10

There are 4 special problems and thus we print the number 4 on a new line.
"""

import sys


arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
n, k = arr[0], arr[1]
t_arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

page_number = 1
result = 0
for problems_count in t_arr:
    pages_count = (problems_count - 1) // k + 1
    