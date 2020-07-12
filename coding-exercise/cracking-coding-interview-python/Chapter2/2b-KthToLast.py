class LinkedList():
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node=node.next
        nodes.append("None")
        return "->".join(nodes)

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return self.data

def removeKthToLast(k,head):
    dummyNode = Node(0)
    slow = dummyNode
    fast = dummyNode
    dummyNode.next = head

    for i in range(0,k):
        fast = fast.next
    
    while fast.next!=None:
        slow = slow.next
        fast = fast.next
    
    return slow.next.data




if __name__ == "__main__":
    linkedlist = LinkedList()
    first_node = Node('1')
    sec_node = Node('2')
    third_node = Node('8')
    fourth_node = Node('3')
    fifth_node = Node('7')
    sixth_node = Node('0')
    seventh_node = Node('4')

    first_node.next = sec_node
    sec_node.next = third_node
    third_node.next = fourth_node
    fourth_node.next = fifth_node
    fifth_node.next = sixth_node
    sixth_node.next = seventh_node
    
    linkedlist.head = first_node
    print(linkedlist)

    print(removeKthToLast(3,first_node))
    print(removeKthToLast(5,first_node))