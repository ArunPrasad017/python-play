from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# breadth first search level order traversal
def levelOrder(node):
    if node is None:
        return
    q = deque([node])
    while len(q) > 0:
        n = q.pop()
        print(n.val)
        if n.left is not None:
            q.appendleft(n.left)
        if n.right is not None:
            q.appendleft(n.right)


# def levelOrderSameLine(node):
#     if node is None:
#         return
#     q = deque([node])
#     size = len(q)
#     while size>0:
#         n=q.pop()
#         print(n.val)
#         size-=1
#         if n.left is not None:
#             q.appendleft(n.left)
#         if n.right is not None:
#             q.appendleft(n.right)
#     size = len(q)
#     print(size)

# def height(root):
#     if root is None:
#         return 0
#     return 1+max(height(root.left), height(root.right))

# def printLevels(root,h):
#     if root is None:
#         return
#     if h==1:
#         print(" "+str(root.val))
#     else:
#         printLevels(root.left,h-1)
#         printLevels(root.right,h-1)

# def levelOrderNaive(root):
#     h = height(root)
#     for i in range(1,h):
#         printLevels(root,i)
#         print("")


def levelOrderWidth(root):
    if root is None:
        return 0
    res = 1
    q = [[root, 0]]
    while len(q) > 0:
        count = len(q)
        start_idx = q[0][1]
        end_idx = q[-1][1]
        res = max(res, end_idx - start_idx + 1)
        for i in range(count):
            p = q[0]
            idx = p[1] - start_idx
            q.pop(0)
            if p[0].left is not None:
                q.append([p[0].left, 2 * idx + 1])
            if p[0].right is not None:
                q.append([p[0].right, 2 * idx + 2])
    return res


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(10)
    root.right = TreeNode(15)
    root.left.left = TreeNode(20)
    root.left.right = TreeNode(25)
    root.right.left = TreeNode(30)
    root.right.right = TreeNode(35)

    # print(levelOrder(root))
    print(levelOrderWidth(root))
