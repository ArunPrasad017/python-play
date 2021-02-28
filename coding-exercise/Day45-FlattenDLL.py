class Solution:
    def flattenRec(self, prev, curr):
        if not curr:
            return prev
        curr.prev = prev
        prev.next = curr

        temp_next = curr.next
        tail = self.flattenRec(curr, curr.child)
        curr.child = None
        return self.flattenRec(tail, temp_next)

    def flatten(self, head: "Node") -> "Node":
        if not head:
            return head
        # pseudo node technique
        pseudoHead = Node(None, None, head, None)
        self.flattenRec(pseudoHead, head)
        pseudoHead.next.prev = None
        return pseudoHead.next
