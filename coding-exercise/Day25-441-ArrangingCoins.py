"""
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

Ex:
n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2
"""


def arrangeCoins(n):
    # brute force
    # cnt = 0
    # i = 1
    # while i<=n:
    #     n-=i
    #     i+=i
    #     cnt+=1
    # return cnt

    # using the binary search and math method
    left = 0
    right = n
    while left <= right:
        k = (left + right) // 2
        current = (k * (k + 1)) // 2
        if current == n:
            return k
        if n < current:
            right = k - 1
        else:
            left = k + 1
    return right


n1 = 5
n2 = 8
print(arrangeCoins(n2))
