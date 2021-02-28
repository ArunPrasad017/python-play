"""
LinkedList Practice from slides
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    def printList(self):
        temp = self.head
        while temp:
            print('{} ->'.format(temp.val),end=" ")
            temp = temp.next
        print()

    def reverseList(self):
        prevNode = None
        currNode = self.head
        while currNode:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
        self.head = prevNode

def removeNthFromEnd(head, n):
    dummyNode = ListNode(0)
    dummyNode.next = head
    slow_ptr =fast_ptr = dummyNode
    for _ in range(n):
        fast_ptr=fast_ptr.next
    while fast_ptr.next is not None:
        slow_ptr=slow_ptr.next
        fast_ptr=fast_ptr.next
    slow_ptr.next = slow_ptr.next.next
    return dummyNode.next

def removeElements(head, val):
    sentinel = ListNode(0)
    sentinel.next = head
    prev, curr = sentinel, head
    while curr is not None:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev=curr
        curr=curr.next
    return sentinel.next

def oddEvenShift(head):
    odd, even = head, head.next
    evenhead = even

    while even is not None and even.next is not None:
        odd.next = even.next
        odd = odd.next
        even = odd.next
        even =  even.next
    odd.next = evenhead
    return head

def isPalindrome(head):
    # easy method
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst==lst[::-1]


# driver code
def main():
    llist = LinkedList()
    llist.head = ListNode(20)
    # second node, third node definition
    secondNode = ListNode(24)
    thirdNode = ListNode(30)
    fourthNode = ListNode(36)
    fifthNode = ListNode(42)
    llist.head.next = secondNode
    secondNode.next = thirdNode
    thirdNode.next = fourthNode
    thirdNode.next.next = fifthNode
    print("Before")
    llist.printList()

    # actual function calls
    # 1. remove from end
    # removeNthFromEnd(llist.head, 2)

    #2. Reverse a LL
    # print(reverseList(llist.head))
    # llist.reverseList()

    # 3. Remove from LL
    # removeElements(llist.head, 30)

    # 4 Switch even and odd locations
    # oddEvenShift(llist.head) # this causes cyclic while 
    # print("After")
    # llist.printList()

    # 5 Palindromic Linked List
    print(isPalindrome(llist.head))
    
if __name__ == "__main__":
    main()