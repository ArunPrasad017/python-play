def areFollowingPatterns(strings, patterns):
    map = {}
    p = set()
    for i in range(len(strings)):
        if strings[i] not in map: 
            map[strings[i]] = patterns[i]
            if patterns[i] in p: return False
            p.add(patterns[i])
        else:
            if patterns[i] != map[strings[i]]:
                return False
    return True

# strings= ["aaa", 
#  "aab", 
#  "aaa"]
# patterns= ["aaa", 
#  "aaa", 
#  "aaa"]

strings = ["cat", 
 "dog", 
 "dog"]
patterns =  ["a", 
 "b", 
 "b"]

print(areFollowingPatterns(strings, patterns))