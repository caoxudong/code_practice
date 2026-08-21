"""
https://leetcode.com/problems/permutation-sequence/description/


The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"

Given n and k, return the kth permutation sequence.

Example 1:
* Input: n = 3, k = 3
* Output: "213"

Example 2:
* Input: n = 4, k = 9
*Output: "2314"

Example 3:
* Input: n = 3, k = 1
* Output: "123"

Constraints:
* 1 <= n <= 9
* 1 <= k <= n!
"""

import re
from typing import List


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [x for x in range(1, n + 1)]
        res = []
        stack = [([], nums)]
        while stack:
            path, remain = stack.pop()
            if not remain:
                res.append(path)
                if len(res) == k:
                    break
                continue
            for i in reversed(range(len(remain))):
                new_path = path + [remain[i]]
                new_remain = remain[:i] + remain[i + 1 :]
                stack.append((new_path, new_remain))
        return "".join(str(x) for x in res[-1])
