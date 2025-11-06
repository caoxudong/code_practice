def _linked_list_object_to_string(self) -> str:
    list_values: list[int] = []

    node = self
    while True:
        list_values.append(node.val)
        node = node.next
        if node == None:
            break

    return "[{}]".format(",".join(map(str, list_values)))


def add_linked_list_to_string_method_to_class_object(
    class_type, method_name="to_string"
):
    setattr(class_type, method_name, _linked_list_object_to_string)
