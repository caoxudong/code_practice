"""
Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).

You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.

Return the reformatted string or return an empty string if it is impossible to reformat the string.

Example 1:
Input: s = "a0b1c2"
Output: "0a1b2c"
Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.

Example 2:
Input: s = "leetcode"
Output: ""
Explanation: "leetcode" has only characters so we cannot separate them by digits.

Example 3:
Input: s = "1229857369"
Output: ""
Explanation: "1229857369" has only digits so we cannot separate them by characters.

Example 4:
Input: s = "covid2019"
Output: "c2o0v1i9d"

Example 5:
Input: s = "ab123"
Output: "1a2b3"

Constraints:
1 <= s.length <= 500
s consists of only lowercase English letters and/or digits.
"""

class Solution:
    def reformat(self, s: str) -> str:
        nums = []
        letters = []
        for c in s:
            if c.isdigit():
                nums.append(c)
            else:
                letters.append(c)
        
        nums_count = len(nums)
        letters_count = len(letters)
        if abs(nums_count - letters_count) > 1:
            return ""

        i = 0
        result = []
        is_letters_first = letters_count > nums_count
        while i < nums_count and i < letters_count:
            if is_letters_first:
                result.append(letters[i])
                result.append(nums[i])
            else:
                result.append(nums[i])
                result.append(letters[i])
            i += 1
        if i < nums_count:
            result.append(nums[i])
        if i < letters_count:
            result.append(letters[i])
        return "".join(result)

if __name__ == "__main__":
    tests = [
        ("a0b1c2", "0a1b2c"),
        ("leetcode", ""),
        ("1229857369", ""),
        ("covid2019", "c2o0v1i9d"),
        ("ab123", "1a2b3")
    ]
    s = Solution()
    for t in tests:
        result = s.reformat(t[0])
        print(t[0], t[1], result)
        assert(t[1] == result)