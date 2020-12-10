from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return None
        q, levels = deque([root]), []
        level = 0
        while q:
            if len(levels) == level:
                levels.append([])
            level_length = len(q)
            for _ in range(level_length):
                node = q.popleft()
                levels[level].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return levels
