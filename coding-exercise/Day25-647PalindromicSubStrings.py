"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
"""
# Absolute brute force
# def palindromicSubString(s):
#     count = 0
#     for i in range(len(s)):
#         j = i 
#         k = i
#         while j>=0 and k<len(s) and s[k] == s[j]:
#             count+=1
#             j-=1
#             k+=1
#         j = i 
#         k = i+1
#         while j>=0 and k<len(s) and s[k] == s[j]:
#             count+=1
#             j-=1
#             k+=1
#     return count



def palindromicSubString(s):
    count = 0
    N = len(s)
    dp = [[0]* N for _ in range(N)]

    for i in range(len(s)):
        dp[i][i] = 1
        count+=1
    for col in range(1,len(s)):
        for row in range(col):
             if (row == col-1 and s[col] == s[row]):
                 dp[row][col] = 1
                 count+=1
             elif (dp[row+1][col-1] ==1 and s[col] == s[row]):
                 dp[row][col] = 1
                 count+=1
    print(dp)
    return count

s = 'aaa'
print(palindromicSubString(s))