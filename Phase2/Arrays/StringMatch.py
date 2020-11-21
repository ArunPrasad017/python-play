def stringMatching(words):
    words.sort(key=lambda x:len(x))
    res_set = set()
    for i in range(len(words)):
        for word in words[i+1:]:
            if words[i] in word :
                # res.append(words[i])
                res_set.add(words[i])
    return list(res_set)

words =  ["mass","as","hero","superhero"]
print(stringMatching(words))