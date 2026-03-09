"""
we have some sorted lists, we want to merge them into one sorted list.
"""

import re


class Solution:
    def merge_sorted_lists(self, lists: list[list[int]]) -> list[int]:
        # O(n,k) = O(nlogn) where n is the total number of elements in all lists, and k is the number of lists.
        retval = []
        for lst in lists:
            retval.extend(lst)
            retval.sort()
        return retval

    def merge_sorted_lists_2(self, lists: list[list[int]]) -> list[int]:
        retval = []
        lists_indexes = [0] * len(lists)
        while True:
            min_value = None
            min_index = None
            for i in range(len(lists)):
                if lists_indexes[i] < len(lists[i]):
                    if min_value is None or lists[i][lists_indexes[i]] < min_value:
                        min_value = lists[i][lists_indexes[i]]
                        min_index = i
            if min_index is None:
                break
            retval.append(min_value)
            lists_indexes[min_index] += 1

        return retval
