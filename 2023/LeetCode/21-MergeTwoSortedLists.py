# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list2):
        list3 = ListNode(0)
        curr = list3
        while self and list2:
            if self.val <= list2.val:
                curr.next = ListNode(self.val)
                self = self.next
            else:
                curr.next = ListNode(list2.val)
                list2 = list2.next
            curr = curr.next
        if self:
            curr.next = self
        elif list2:
            curr.next = list2

        return list3.next