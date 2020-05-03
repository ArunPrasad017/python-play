"""
Using dynamic programming

Some background: we use a list predeclared with false and then we try to add 
true to corresponding element when the exit happens with the word in list
We convert list to set for o(1) time parsed
"""
def word_break(s, wordDict):
    length = len(s)
    wordSet = set(wordDict)
    dp = [False for _ in range(length+1)]
    dp[0] = True

    for i in range(0,length):
        for j in range(i+1,length+1):
            if dp[i]==True and s[i:j] in wordSet:
                dp[j]=True
    return dp[-1]

wordList=["leet", "code"]
s = "leetcode"
print(word_break(s,wordList))