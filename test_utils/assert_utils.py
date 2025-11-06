from typing import Optional

import common_data_structure
import common_data_structure.list_node


def assertListNodeEqual(
    result: Optional[common_data_structure.list_node.ListNode] = None,
    expected: Optional[common_data_structure.list_node.ListNode] = None,
):

    if result == None and expected == None:
        return
    if result == None and expected != None:
        raise AssertionError(
            "AssertionError, result is None, expected is {}".format(
                expected.to_string()
            )
        )
    if result != None and expected == None:
        raise AssertionError(
            "AssertionError, result is {}, expected is None".format(result.to_string())
        )

    result_tmp_node = result
    expected_tmp_node = expected
    while True:
        if result_tmp_node.val != expected_tmp_node.val:
            raise AssertionError(
                "AssertionError, result is {}, expected is {}".format(
                    result.to_string(), expected.to_string()
                )
            )

        result_tmp_node = result_tmp_node.next
        expected_tmp_node = expected_tmp_node.next
        if result_tmp_node == None and expected_tmp_node == None:
            return
        elif result_tmp_node != None and expected_tmp_node != None:
            continue
        else:
            raise AssertionError(
                "AssertionError, result is {}, expected is {}".format(
                    result.to_string(), expected.to_string()
                )
            )
