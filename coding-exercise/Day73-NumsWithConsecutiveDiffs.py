"""
967. Numbers With Same Consecutive Differences

Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.
Note that every number in the answer must not have leading zeros except for the number 0 itself. 
For example, 01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.

Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.

Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
"""


def dfs(self, num, n, k, res):
    if n == 0:
        res.append(num)
        return
    last_digit = num % 10
    if last_digit >= k:
        self.dfs(num * 10 + (last_digit - k), n - 1, k, res)
    if k > 0 and last_digit + k < 10:
        self.dfs(num * 10 + (last_digit + k), n - 1, k, res)


def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
    res = []
    if N == 0:
        res.append(0)
    for d in range(1, 10):
        self.dfs(d, N - 1, K, res)
    return res
