def coinChange(coins, amount):
    memo = [float("inf")] * (amount + 1)
    memo[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            memo[i] = min(memo[i], memo[i - coin] + 1)
    return memo[amount] if memo[amount] != float("inf") else -1


coins = [1, 2, 5]
amount = 11
print(coinChange(coins, amount))
