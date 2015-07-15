"""

Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

For C programmers: Try to solve it in-place in O(1) space.

Clarification:
* What constitutes a word?
    A sequence of non-space characters constitutes a word.
* Could the input string contain leading or trailing spaces?
    Yes. However, your reversed string should not contain leading or trailing spaces.
* How about multiple spaces between two words?
    Reduce them to a single space in the reversed string.

https://leetcode.com/problems/reverse-words-in-a-string/

"""

class Solution:
  # @param s, a string
  # @return a string
  def reverseWords(self, s):