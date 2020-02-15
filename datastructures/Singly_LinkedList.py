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
    
    def delete_Node(self,head,val_to_delete):
        currentNode = head
        prevNode = None
        while currentNode is not None:
            if currentNode.value == val_to_delete:
                if prevNode is None:
                    newhead = currentNode.next
                    currentNode.next = None
                    return newhead
                prevNode.next = currentNode.next
                return head
                
            prevNode = currentNode
            currentNode=currentNode.next

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
print(head)
a.insert_Node_toEnd(a,5)
print_LinkedList(a)
a.delete_Node(a,2)
print("after")
print_LinkedList(a)
