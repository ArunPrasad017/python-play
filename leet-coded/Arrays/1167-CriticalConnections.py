"""
Utilizes DFS and uses the Tarjan's algorithm
we identify the strongly connected components in the network
"""
from collections import defaultdict
def criticalConnections(n,connections):
    dic = defaultdict(list)
    for c in connections:
        u,v = c
        dic[u].append(v)
        dic[v].append(u)
    visited =[False]*n
    res =[]
    root_seq =[n]*n
    parent = [n]*n
    seq = 0

    def dfs(u):
        nonlocal seq
        visited[u] = True
        curr_seq = root_seq[u] = seq
        seq+=1

        for v in dic[u]:
            if not visited[v]:
                parent[v]=u
                dfs(v)
                if root_seq[v] > curr_seq:
                    res.append([u,v])
            if parent[u]!=v:
                root_seq[u] = min(root_seq[u],root_seq[v])
    dfs(0)
    return res
n = 4
connections = [[0,1],[1,2],[2,0],[1,3]]

print(criticalConnections(n,connections))