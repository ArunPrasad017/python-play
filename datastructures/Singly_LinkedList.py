class Node(object):

    def __init__(self,value):
        self.value = value
        self.next = None

    def insert_Node_toEnd(self,head,val_to_insert):
        currentNode = head
        while currentNode is not None:
            if currentNode.next is None:
                currentNode.next = Node(val_to_insert)
                return head
            currentNode = currentNode.next

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
        currentNode=currentNode.next

head = a
print_LinkedList(a)
a.insert_Node_toEnd(a,5)
print_LinkedList(a)