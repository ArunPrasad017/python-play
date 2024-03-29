class Node(object):
    def __init__(self, value):

        self.value = value
        self.nextnode = None


def cycle_check(node):
    head_node = node
    while node is not None:
        if node.nextnode == head_node:
            return True
            break
        node = node.nextnode
    return False


# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a  # Cycle Here!

print(cycle_check(a))
