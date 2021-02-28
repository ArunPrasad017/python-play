"""
A message containing letters from A-Z is being 
encoded to numbers using the following mapping - 
'A' ->1 'B' -> 2... 'Z' ->26

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Hint: Use the bottom up processing technique and iteratively find the answer

"""


def numDecodings(s):
    if not s:
        return 0
    dp = [0 for _ in range(0, len(s) + 1)]
    dp[0] = 1

    dp[1] = 0 if s[0] == "0" else 1
    for i in range(2, len(dp)):
        if s[i - 1] != "0":
            dp[i] += dp[i - 1]
        if int(s[i - 2 : i]) >= 10 and int(s[i - 2 : i]) <= 26:
            dp[i] += dp[i - 2]
    return dp[len(s)]


s = "01"
print(numDecodings(s))
