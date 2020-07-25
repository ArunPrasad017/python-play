def allPathsSourceTarget(graph):
    res = []
    def dfs(path,u):
        if u==len(graph)-1:
            res.append(path+[u])
        else:
            for v in graph[u]:
                dfs(path+[u], v)
    dfs([],0)
    return res