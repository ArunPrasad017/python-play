"""
121
"""


def maxProfit(prices):
    maxProfit = float("-inf")
    for i in range(len(prices) - 1):
        maxVal = max(prices[i + 1 :]) - prices[i]
        maxProfit = max(maxProfit, maxVal)
    return maxProfit if maxProfit >= 0 else 0


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))
