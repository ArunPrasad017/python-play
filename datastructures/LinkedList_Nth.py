class Node:
    def __init__(self, value):
        self.value = value
        self.nextnode = None


def nth_to_last_node(n, head):
    cnt = 0
    temp = head
    while head:
        cnt += 1
        head = head.nextnode
    for i in range(0, (cnt - n)):
        temp = temp.nextnode
    return temp.value


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

# This would return the node d with a value of 4, because its the 2nd to last node.
target_node = nth_to_last_node(4, a)
print(target_node)
