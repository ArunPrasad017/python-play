"""
Leetcode 2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    l3 = ListNode(0)
    curr = l3
    carry = 0
    while l1 or l2:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        sumVal = x+y+carry
        carry = sumVal//10
        value = sumVal%10
        curr.next = ListNode(sumVal%10)
        curr = curr.next
        if l1: l1= l1.next
        if l2: l2= l2.next
    if carry:
        node = ListNode(carry)
        curr.next = node
    return l3.next