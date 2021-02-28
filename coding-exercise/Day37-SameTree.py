# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# recursive
def isSameTree(p, q):  # sourcery skip: remove-redundant-if
    if not (p or q):
        return True
    if not (p and q):
        return False
    if p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


# Iterative
def isSame(p, q):  # sourcery skip: remove-redundant-if
    if not (p or q):
        return True
    if not (p and q):
        return False
    return p.val == q.val


def isSameTree_Iterative(p, q):
    if not isSame(p, q):
        return False
    Q1, Q2 = [], []
    Q1.append(p)
    Q2.append(q)
    while len(Q1):
        n1 = Q1.pop()
        n2 = Q2.pop()
        if not isSame(n1, n2):
            return False
        if n1:
            if not isSame(n1.left, n2.left):
                return False
            if n1.left:
                Q1.append(n1.left)
                Q2.append(n2.left)
            if not isSame(n1.right, n2.right):
                return False
            if n1.right:
                Q1.append(n1.right)
                Q2.append(n2.right)
    return True


if __name__ == "__main__":
    p = TreeNode(1)
    q = TreeNode(1)
    p1 = TreeNode(2)
    q1 = TreeNode(2)
    p2 = TreeNode(1)
    q2 = TreeNode(1)

    p.left = p1
    p.right = p2

    q.left = q1
    q.right = q2

    print(isSameTree_Iterative(p, q))
