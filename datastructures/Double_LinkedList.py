class Node(object):
    
    def __init__(self,value, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev
    
    def insertToFirst(self,head,val_to_insert):
        new_node = Node(val_to_insert)

        new_node.next = head
        new_node.prev = None

        if head is not None:
            head.prev = new_node
        head = new_node

    def traverse_DLL(self,head):
        currentNode = head
        while currentNode is not None:
            print(currentNode.value)
            currentNode = currentNode.next

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
a.insertToFirst(a,0)
a.traverse_DLL(a)
