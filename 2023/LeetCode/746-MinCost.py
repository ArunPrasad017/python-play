def minCostClimbingStairs(cost):
    # bottom up dynamic approach/Recurrence relation
    n = len(cost) + 1
    cost_list = [0] * (n)
    for i in range(2, n):
        cost_list[i] = min(
            cost_list[i - 1] + cost[i - 1], cost_list[i - 2] + cost[i - 2]
        )
    return cost_list[n - 1]


cost = [10, 15, 20]
assert 15 == minCostClimbingStairs(cost)