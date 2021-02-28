class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def flatten(root):
    if root is None:
        flattenRec(root)
    return root

def flattenRec(root):
    curr = root
    tail = root
    while curr is not None:
        child = curr.child
        next = curr.next
        if not child:
            curr = next
        else:
            _tail = flattenRec(child)
            _tail.next = next
            if next is not None:
                next.prev = _tail
                curr.next = child
                child.prev = curr
                curr.child = None
        if curr is not None:
            tail = curr
    return tail

if __name__ == "__main__":
    # lst = [1,2,3,4,5,6,None,None,None,7,8,9,10,None,None,11,12]

    flatten()
