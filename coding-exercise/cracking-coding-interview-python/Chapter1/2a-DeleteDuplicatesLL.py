"""
Single LinkedList implementation + remove duplicates
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return "->".join(nodes)


def removeDupes(ll):
    current = ll.head
    seen = set([current.data])
    while current.next:
        if current.next.data in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.data)
            current = current.next
    return ll


if __name__ == "__main__":
    linkedlist = LinkedList()
    first_node = Node("5")
    sec_node = Node("5")
    third_node = Node("15")
    first_node.next = sec_node
    sec_node.next = third_node
    linkedlist.head = first_node
    print(linkedlist)

    removeDupes(linkedlist)

    print(linkedlist)
