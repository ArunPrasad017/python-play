# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(headA, headB):
        if headA is None and headB is None:
            return None
        ptr1 = headA
        ptr2 = headB

        while ptr1 != ptr2:
            # if ptr2 is None:
            #     ptr2 = headA
            # else:
            #     ptr2=ptr2.next
            # if ptr1 is None:
            #     ptr1 = headB
            # else:
            #     ptr1=ptr1.next
            ptr2 = headA if ptr2 is None else ptr2.next
            ptr1 = headB if ptr1 is None else ptr1.next
        return ptr1
