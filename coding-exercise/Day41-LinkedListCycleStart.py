class Solution:
    def getIntersect(self, head):
        slow_ptr = head
        fast_ptr = head
        while fast_ptr is not None and fast_ptr.next is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if slow_ptr == fast_ptr:
                return slow_ptr
        return None

    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        intersect = self.getIntersect(head)
        if intersect is None:
            return None
        ptr1 = head
        ptr2 = intersect
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ptr1
