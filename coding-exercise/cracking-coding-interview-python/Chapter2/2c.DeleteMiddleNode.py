class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        return "->".join(nodes)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


def deleteMiddleNode(head):
    # pattern found with these LL related questions is that there is
    # a usual formation of two pointer technique to identify
    # and narrow down the traversal, this is effective for identifying
    # because the size of LL is usually not know like normal list
    slowPtr = head
    fastPtr = head
    prev = head

    while fastPtr.next != None and fastPtr.next.next != None:
        prev = slowPtr
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next.next
    prev.next = slowPtr.next
    slowPtr.next = None


if __name__ == "__main__":
    linkedlist = LinkedList()
    first_node = Node("a")
    sec_node = Node("b")
    third_node = Node("c")
    fourth_node = Node("d")
    fifth_node = Node("e")
    sixth_node = Node("f")

    first_node.next = sec_node
    sec_node.next = third_node
    third_node.next = fourth_node
    fourth_node.next = fifth_node
    fifth_node.next = sixth_node

    linkedlist.head = first_node
    print("\n Initial linkedlist: {}".format(linkedlist))
    deleteMiddleNode(first_node)
    print("\n current linkedlist: {}".format(linkedlist))
