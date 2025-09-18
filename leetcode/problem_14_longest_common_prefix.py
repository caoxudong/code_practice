"""
https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        strs_count = len(strs)
        if strs_count == 0:
            return ""
        strs_len_array = [len(s) for s in strs]
        min_strs_len = min(strs_len_array)

        result_c_array = []
        c_index = 0
        while c_index < min_strs_len:
            temp_c = strs[0][c_index]
            all_matched = True
            for str_index in range(1, strs_count):
                if temp_c != strs[str_index][c_index]:
                    all_matched = False
                    break
            if not all_matched:
                break
            c_index += 1
            result_c_array.append(temp_c)
        return "".join(result_c_array)


if __name__ == "__main__":
    test_params = [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        ([], ""),
    ]
    s = Solution()
    for test in test_params:
        result = s.longestCommonPrefix(test[0])
        print(test[0], test[1], result)
        assert result == test[1]
