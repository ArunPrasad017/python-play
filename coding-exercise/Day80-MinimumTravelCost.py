"""
983. Minimum Cost For Tickets

In a country popular for train travel, you have planned some train travelling one year in advance.  The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

Train tickets are sold in 3 different ways:

a 1-day pass is sold for costs[0] dollars;
a 7-day pass is sold for costs[1] dollars;
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: 
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total you spent $11 and covered all the days of your travel.
"""


def minCostTravel(days, costs):
    n = len(days)
    dp = [0] * (n + 1)
    dp[n] = 0

    for i in range(n - 1, -1, -1):
        d7, d30 = i, i
        while d7 < n and days[d7] < (days[i] + 7):
            d7 += 1
        while d30 < n and days[d30] < (days[i] + 30):
            d30 += 1
        dp[i] = min((costs[0] + dp[i + 1]), (costs[1] + dp[d7]), (costs[2] + dp[d30]))
    return dp[0]


days = [1, 4, 6, 7, 8, 20]
costs = [2, 7, 15]

print(minCostTravel(days, costs))
