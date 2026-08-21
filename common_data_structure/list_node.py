from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next=None):
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


def create_ListNode(nums: list[int] = []) -> ListNode:
    last_listnode = None
    while len(nums) > 0:
        tmp_val = nums.pop()
        tmp_listnode = ListNode(tmp_val, last_listnode)
        last_listnode = tmp_listnode
    return last_listnode


def create_ListNodeList(nums: list[int] = []) -> List[ListNode]:
    retval = []
    last_listnode = None
    while len(nums) > 0:
        tmp_val = nums.pop()
        tmp_listnode = ListNode(tmp_val, last_listnode)
        last_listnode = tmp_listnode
        retval.insert(0, tmp_listnode)
    return retval


def assertListNodeEqual(
    result: Optional[ListNode] = None,
    expected: Optional[ListNode] = None,
):
    if result == None and expected == None:
        return
    if result == None and expected != None:
        raise AssertionError("AssertionError, result is None, expected is {}".format(expected.to_string()))
    if result != None and expected == None:
        raise AssertionError("AssertionError, result is {}, expected is None".format(result.to_string()))

    result_tmp_node = result
    expected_tmp_node = expected
    while True:
        if result_tmp_node.val != expected_tmp_node.val:
            raise AssertionError(
                "AssertionError, result is {}, expected is {}".format(result.to_string(), expected.to_string())
            )

        result_tmp_node = result_tmp_node.next
        expected_tmp_node = expected_tmp_node.next
        if result_tmp_node == None and expected_tmp_node == None:
            return
        elif result_tmp_node != None and expected_tmp_node != None:
            continue
        else:
            raise AssertionError(
                "AssertionError, result is {}, expected is {}".format(result.to_string(), expected.to_string())
            )
