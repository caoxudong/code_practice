"""
https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/?utm_source=LCUS&utm_medium=ip_redirect&utm_campaign=transfer2china

You are given a string `s` and an array of strings `words`. All the strings of `words` are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of `words` concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in `s`. You can return the answer in any order.

Example 1:
* Input: s = "barfoothefoobarman", words = ["foo","bar"]
* Output: [0,9]
* Explanation:
    * The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
    * The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:
* Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
* Output: []
* Explanation:
    * There is no concatenated substring.

Example 3:
* Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
* Output: [6,9,12]
* Explanation:
    * The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
    * The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
    * The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].



Constraints:
* 1 <= s.length <= 104
* 1 <= words.length <= 5000
* 1 <= words[i].length <= 30
* s and words[i] consist of lowercase English letters.
"""


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        # return self.solution1(s, words)
        return self.solution2(s, words)

    def solution2(self, s: str, words: list[str]) -> list[int]:
        word_freq = {}
        for word in words:
            word_freq[word] = 1 + word_freq.get(word, 0)

        word_size: int = len(words[0])
        whole_sub_string_length = word_size * len(words)
        s_length = len(s)

        retval: list[int] = []
        start_index = 0
        while start_index < s_length - whole_sub_string_length + 1:
            substr_freq = {}
            cur_index = start_index
            while cur_index < start_index + whole_sub_string_length:
                cur_word = s[cur_index : cur_index + word_size]
                if cur_word not in word_freq:
                    break
                substr_freq[cur_word] = substr_freq.get(cur_word, 0) + 1

                if substr_freq[cur_word] > word_freq[cur_word]:
                    break
                cur_index += word_size

            if cur_index == start_index + whole_sub_string_length:
                retval.append(start_index)

            start_index += 1

        return retval

    def solution1(self, s: str, words: list[str]) -> list[int]:
        concatenations_set: set = set()

        def permutations(arr, result: set, current):
            if not arr:
                result.add("".join(current))
                return
            for i in range(len(arr)):
                current.append(arr[i])
                permutations(arr[:i] + arr[i + 1 :], result, current)
                current.pop()

        permutations(words, concatenations_set, [])

        retval = []
        for item in concatenations_set:
            tmp_start = 0
            while True:
                tmp_index = s.find(item, tmp_start)
                if tmp_index == -1:
                    break
                retval.append(tmp_index)
                tmp_start += 1

        return list(set(retval))
