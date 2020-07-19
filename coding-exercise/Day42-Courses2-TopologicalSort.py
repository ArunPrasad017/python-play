def dfs(i,visited, stack,adj):
    visited[i] = 1
    for v in adj[i]:
        if visited[v]==1:return True
        if visited[v]==0 and dfs(v,visited,stack,adj):return True
    visited[i]=2
    stack.append(i)
    return False

def findOrder(numCourses, prerequisites):
    adj=[[] for _ in range(numCourses)]
    for courses in prerequisites:
        adj[courses[1]].append(courses[0])
    stack = []
    visited =[0]*numCourses
    for i in range(numCourses):
        if visited[i]==0 and dfs(i,visited,stack,adj):
            return []
    stack.reverse()
    return stack

n = 2
courses = [[0,1],[1,0]]
# courses = [[1,0],[2,0],[3,1],[3,2]]
print(findOrder(n, courses))