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
