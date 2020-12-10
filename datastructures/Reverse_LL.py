class Node(object):
    def __init__(self, value):

        self.value = value
        self.nextnode = None


def reverse(a_head):

    next_node = None
    curr_node = None
    prev_node = None

    while a_head:
        next_node = a_head.nextnode
        curr_node = a_head

        a_head.nextnode = prev_node

        a_head = next_node
        prev_node = curr_node
    return curr_node


# Create a list of 4 nodes
a = Node(1)
b = Node(2)

# Set up order a,b,c,d with values 1,2,3,4
a.nextnode = b

print(reverse(a))

print(b.nextnode.value)
