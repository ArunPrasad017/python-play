from collections import defaultdict


class Solution:

    WHITE = 1
    GRAY = 2
    BLACK = 3

    def findOrder(self, numCourses, prerequisites):
        adjlist = defaultdict(list)

        # A pair [a,b] in the input represents edge from b-->a
        for dest, src in prerequisites:
            adjlist[src].append(dest)
        topological_sorted = []
        is_possible = True
        color = {k: Solution.WHITE for k in range(numCourses)}

        def dfs(node):
            nonlocal is_possible

            if not is_possible:
                return

            color[node] = Solution.GRAY
            if node in adjlist:
                for n in adjlist[node]:
                    if color[n] == Solution.WHITE:
                        dfs(n)
                    elif color[n] == Solution.GRAY:
                        is_possible = False

            color[node] = Solution.BLACK
            topological_sorted.append(node)

        for vertex in range(numCourses):
            if color[vertex] == Solution.WHITE:
                dfs(vertex)
        return topological_sorted


n = 4
prereq = [[1, 0], [2, 0], [3, 1], [3, 2]]
p1 = Solution()
print(p1.findOrder(n, prereq))
