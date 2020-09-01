"""
122. Best Time to Buy and Sell Stock II
Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:
Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
"""
# one pass execution for a greedy algo
def maxProfit(prices):
    max_profit = 0
    for i in range(len(prices)-1):
        if prices[i+1]>prices[i]:
            max_profit+=(prices[i+1]-prices[i])
    return max_profit

# uses two pointer with greedy algorithm - similar to the mountain array program
def maxProfitCtr(prices):
    peak = prices[0]
    valley = prices[0]
    i, maxProfit = 0,0
    while i+1<len(prices):
        while i+1<len(prices) and prices[i]>prices[i+1]:
            i+=1
        valley = prices[i]
        while i+1<len(prices) and prices[i]<prices[i+1]:
            i+=1
        peak = prices[i]
        maxProfit+=peak-valley
    return maxProfit


lst = [7,1,5,3,6,4]
print(maxProfitCtr(lst))