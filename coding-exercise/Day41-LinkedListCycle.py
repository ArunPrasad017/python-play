def hasCycle(self, head: ListNode) -> bool:
    if head is None or head.next is None:
        return False
    slow_ptr = head
    fast_ptr = head.next
    while slow_ptr!=fast_ptr:
        if fast_ptr.next is None or fast_ptr.next.next is None:
            return False
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
    return True