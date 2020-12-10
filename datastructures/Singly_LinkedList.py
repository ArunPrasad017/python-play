class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def insert_Node_toEnd(self, head, val_to_insert):
        currentNode = head
        while currentNode is not None:
            if currentNode.next is None:
                currentNode.next = Node(val_to_insert)
                return head
            currentNode = currentNode.next

    def delete_Node(self, head, val_to_delete):
        currentNode = head
        prevNode = None
        while currentNode is not None:
            if currentNode.value == val_to_delete:
                # if value to be deleted is first node
                if prevNode is None:
                    newhead = currentNode.next
                    currentNode.next = None
                    return newhead
                prevNode.next = currentNode.next
                return head
            prevNode = currentNode
            currentNode = currentNode.next

    def insert_Node(self, head, val_to_Insert, position):
        currentNode = head
        prevNode = None
        currentpos = 0
        new_node = Node(val_to_Insert)
        if not head:
            head = new_node
        if position == 0:
            currentNode.next = head
            head = new_node
            return head
        while currentNode is not None:
            if currentpos == position and currentNode.next:
                prevNode.next = new_node
                new_node.next = currentNode
            elif currentNode.next == None:
                currentNode.next = new_node
                break
            prevNode = currentNode
            currentNode = currentNode.next
            currentpos += 1


a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c

# traverse and print linked list
def print_LinkedList(head):
    currentNode = head
    while currentNode is not None:
        print(currentNode.value)
        currentNode = currentNode.next


head = a
print(head)
# a.insert_Node_toEnd(a,5)
# print_LinkedList(a)
# a.delete_Node(a,2)
# print("after")
# print_LinkedList(a)

a.insert_Node(a, 5, 3)
print_LinkedList(a)
