def maxProfit(prices):
    # greedy algo
    total_price = 0
    for i in range(len(prices)-1):
        if prices[i]<prices[i+1]:
            total_price+=(prices[i+1] - prices[i])
    return total_price
    
lst = [7,1,5,3,6,4]
print(maxProfit(lst))