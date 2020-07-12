def shortestDistance(words, word1, word2):
    res = {}
    i = 0
    dist = len(words) 
    for i,c in enumerate(words):
        if c==word1 or c==word2:
            res[c]=i
        if word1 in res.keys() and word2 in res.keys():
            dist = min(dist,abs(res[word1] - res[word2]))
    return dist 

words = ["a","c","b","a"]
word1 = "b"
word2 = "a"

print(shortestDistance(words,word1,word2))