"""
https://leetcode.com/problems/zigzag-conversion/

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"

Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I

"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        arrs = [[] for i in range(numRows)]
        s_len = len(s)
        i = -1
        delta = 1
        for c in s:
            if i == 0:
                delta = 1
                if i == (numRows - 1):
                    delta = 0
            elif i == (numRows - 1):
                delta = -1
            i += delta
            arrs[i].append(c)
        return "".join(["".join(x) for x in arrs])

if __name__ == "__main__":
    test_str = "ab"
    solution = Solution()
    print(solution.convert(test_str, 1))