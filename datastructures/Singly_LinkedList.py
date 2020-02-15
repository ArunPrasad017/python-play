class Node(object):

    def __init__(self,value):
        self.value = value
        self.next = None

    def insert_Node_head(self,head,toInsert):
        currentNode = head
        while currentNode is not None:
            if currentNode.next is not None:
                currentNode.next = Node(toInsert)
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
a.insert_Node_head(a,5)
print_LinkedList(a)