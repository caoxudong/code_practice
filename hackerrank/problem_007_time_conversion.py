#!/bin/python3

"""
https://www.hackerrank.com/challenges/time-conversion?h_r=next-challenge&h_v=zen

Given a time in AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.

Input Format

A single string containing a time in 12-hour clock format (i.e.: hh:mm:ssAM or hh:mm:ssPM), where 01 <= hh <= 12. 

Output Format

Convert and print the given time in 24-hour format, where 00 <= hh <= 23.

Sample Input

07:05:45PM

Sample Output

19:05:45

"""

import sys


time = input().strip()

timePartitionFlag = time[-2:]
hour = int(time[0]) * 10 + int(time[1])

if timePartitionFlag == "PM":
    if hour == 12:
        hour -= 12
    hour += 12
else:
    if hour == 12:
        hour = 0

if hour < 10:
    hour = "0" + str(hour)
else:
    hour = str(hour)

result = time[2:-2]
result = hour + result

print(result)