"""
https://leetcode.com/problems/merge-k-sorted-lists/

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.


Example 1:
* Input: lists = [[1,4,5],[1,3,4],[2,6]]
* Output: [1,1,2,3,4,4,5,6]
* Explanation:
    * The linked-lists are:
        [
            1->4->5,
            1->3->4,
            2->6
        ]
    * merging them into one sorted linked list:
        * 1->1->2->3->4->4->5->6

Example 2:
* Input: lists = []
* Output: []

Example 3:
* Input: lists = [[]]
* Output: []

Constraints:
* k == lists.length
* 0 <= k <= 104
* 0 <= lists[i].length <= 500
* -104 <= lists[i][j] <= 104
* lists[i] is sorted in ascending order.
* The sum of lists[i].length will not exceed 104.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def to_string(self) -> str:
        list_values: list[int] = []

        node = self
        while True:
            list_values.append(node.val)
            node = node.next
            if node == None:
                break

        return "[{}]".format(",".join(map(str, list_values)))


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        result_nums = []

        for tmp_list in lists:
            while tmp_list != None:
                result_nums.append(tmp_list.val)
                tmp_list = tmp_list.next

        result_nums.sort()

        def create_ListNode(nums: list[int] = []) -> ListNode:
            last_listnode = None
            while len(nums) > 0:
                tmp_val = nums.pop()
                tmp_listnode = ListNode(tmp_val, last_listnode)
                last_listnode = tmp_listnode
            return last_listnode

        result_list = create_ListNode(result_nums)

        return result_list
