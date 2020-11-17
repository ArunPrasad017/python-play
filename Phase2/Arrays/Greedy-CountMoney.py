def find_min_coins(v, coins_available):
    res = []
    n=len(coins_available)
    for i in range(n-1,-1,-1):
        while v>=coins_available[i]:
            v-=coins_available[i]
            res.append(coins_available[i])
    return res
coins_available = [1,5,10,25]
v=19
print(find_min_coins(v,coins_available))