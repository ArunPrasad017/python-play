"""
  Odd Even Linked List
A well-formed LinkedList need two pointers head and tail to support operations at both ends. The variables head and odd are the head pointer 
and tail pointer of one LinkedList we call oddList; the variables evenHead and even are the head pointer and tail pointer of another LinkedList we call evenList.

"""


def oddEvenList(head):
    while head is None:
        return None
    odd = head
    even = head.next
    evenhead = even

    while even is not None and even.next is not None:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = evenhead
    return head
