def isPalindrome(head):
    if head is None:
        return True
    first_half_end = end_of_first_half(head)
    second_half_start = reverseLinkedList(first_half_end.next)
    result = True
    first_position = head
    second_position = second_half_start
    while result and second_position is not None:
        if first_position.val != second_position.val:
            result = False
        first_position = first_position.next
        second_position = second_position.next
    return result


def end_of_first_half(head):
    slow_ptr = head
    fast_ptr = head
    while fast_ptr.next is not None and fast_ptr.next.next is not None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
    return slow_ptr


def reverseLinkedList(head):
    prevNode, currNode, nextNode = None, None, None
    while head is not None:
        currNode = head
        nextNode = head.next
        head.next = prevNode
        prevNode = currNode
        head = nextNode
    return prevNode
