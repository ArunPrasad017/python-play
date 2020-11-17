def min_cost(pipes):
    cost=0
    n=len(pipes)
    pipes.sort()
    for i in range(n-1):
        prev_cost = cost
        cost=pipes[i]+pipes[i+1]
        pipes[i+1]=cost
        cost += prev_cost
    return cost
pipes = [4, 3, 2, 6]
print(min_cost(pipes))