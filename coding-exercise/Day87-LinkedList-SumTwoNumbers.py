# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    l3 = ListNode(0)
    curr = l3
    carry,x,y = 0,0,0
    while l1 or l2:
        if l1: x = l1.val
        if l2: y = l2.val
        sum_val = (carry+x+y)
        carry = sum_val//10
        curr.next = ListNode(sum_val%10)
            
        curr = curr.next
        if l1:l1=l1.next
        if l2:l2=l2.next
    if carry:
        node = ListNode(carry)
        curr.next = node
    return l3.next