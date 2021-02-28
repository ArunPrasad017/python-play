class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node is None:
            return None
        else:
            tempNode = node.next
            node.val = tempNode.val
            node.next = tempNode.next
