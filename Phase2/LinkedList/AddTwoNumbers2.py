# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(self,head):
    prevNode=currNode=nextNode = None
    while head:
        currNode=head
        nextNode=head.next
        head.next=prevNode
        prevNode = currNode
        head=nextNode
    return prevNode
        
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    if not l1 and not l2:
        return None
    ll1 = self.reverseList(l1)
    ll2 = self.reverseList(l2)
    head,carry=None,0
    while ll1 or ll2:
        x = ll1.val if ll1 else 0
        y = ll2.val if ll2 else 0
        sumVal = x+y+carry
        carry = sumVal//10
        curr=ListNode(sumVal%10)
        curr.next = head
        head=curr
        ll1 = ll1.next if ll1 else None
        ll2 = ll2.next if ll2 else None
    if carry:
        curr = ListNode(carry)
        curr.next = head
        head=curr
    return head