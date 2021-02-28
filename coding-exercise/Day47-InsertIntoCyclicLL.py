"""
Given a node from a Circular Linked List which is sorted in ascending order, write a function to insert a value insertVal into the list 
such that it remains a sorted circular list. The given node can be a reference to any single node in the list, 
and may not be necessarily the smallest value in the circular list.

If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the circular list should remain sorted.

If the list is empty (i.e., given node is null), you should create a new single circular list 
and return the reference to that single node. Otherwise, you should return the original given node.

Input: head = [3,4,1], insertVal = 2
Output: [3,4,1,2]
Explanation: In the figure above, there is a sorted circular list of three elements. 
You are given a reference to the node with value 3, and we need to insert 2 into the list. The new node should be inserted between node 1 and node 3. 
After the insertion, the list should look like this, and we should still return node 3.

Input: head = [], insertVal = 1
Output: [1]
Explanation: The list is empty (given head is null). We create a new single circular list and return the reference to that single node.

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def insert(head, insertVal):

    # case1 where the head is none
    if head is None:
        node = ListNode(insertVal)
        node.next = node
        return node
    maximum = head

    # case 2
    while maximum != head and maximum.val <= insertVal:
        maximum = maximum.next
    minimum = maximum.next
    cur = minimum

    if insertVal >= maximum.val or insertVal <= minimum.val:
        node = ListNode(insertVal, minimum)
        node.next = maximum
    else:
        while cur.next.val <= insertVal:
            cur = cur.next
        node = ListNode(insertVal, cur.next)
        cur.next = node
    return head
