def maxProfit(prices):
    return sum(
        prices[i] - prices[i - 1]
        for i in range(1, len(prices))
        if prices[i] > prices[i - 1]
    )

prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))