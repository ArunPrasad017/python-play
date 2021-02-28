def reverseList(head):
    curNode=nextNode=prevNode = None
    while head:
        curNode = head
        nextNode = head.next
        head.next = prevNode
        prevNode =curNode
        head=nextNode
    return prevNode

