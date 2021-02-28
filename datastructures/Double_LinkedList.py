class Node(object):
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def insertToFirst(self, head, val_to_insert):
        new_node = Node(val_to_insert)
        new_node.next = head
        new_node.prev = None

        if head is not None:
            head.prev = new_node
        head = new_node
        return head

    def traverse_DLL(self, head):
        currentNode = head
        while currentNode is not None:
            print(currentNode.value)
            currentNode = currentNode.next

    def inserttoPosition(self, head, position, val_to_Insert):
        if position == 0:
            insertToFirst(head, val_to_Insert)
        else:
            new_node = Node(val_to_Insert)
            currentNode = head
            currentpos = 0
            while position > currentpos and currentNode.next:
                currentpos += 1
                currentNode = currentNode.next
            currentNode.prev.next = new_node
            new_node.next = currentNode
            new_node.prev = currentNode.prev
            currentNode.prev = new_node

        return head

    def deleteNode(self, head, position):
        if position == 0:
            head = head.next
            head.prev = None
        else:
            currentNode = head
            currentpos = 0

            while position > currentpos and currentNode.next:
                currentpos += 1
                currentNode = currentNode.next
            currentNode.prev.next = currentNode.next
            currentNode.prev = currentNode.next.prev
            return head


if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)

    a.next = b
    a.prev = None
    b.next = c
    b.prev = a
    c.next = None
    c.prev = b

    a.traverse_DLL(a)
    print("---------------------")
    new_head = a.insertToFirst(a, 0)
    a.traverse_DLL(new_head)
    print("---------------------")
    a.inserttoPosition(new_head, 2, 5)
    a.traverse_DLL(new_head)
    print("---------------------")
    a.deleteNode(new_head, 6)
    a.traverse_DLL(new_head)
