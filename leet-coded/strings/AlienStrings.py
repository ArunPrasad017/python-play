def AlienStrings(words,order):
    #order dictionary:
    order_dict = {c:i for i,c in enumerate(order)}
    for j in range(0,len(words)-1):
        word1 = words[j]
        word2 = words[j+1]

        for k in range(0,min(len(word1),len(word2))):
            if word1[k] != word2[k]:
                if order_dict[word1[k]]> order_dict[word2[k]]:
                    return False
                break
        else:
            if len(word1) > len(word2):
                return False
    return True

words = ["apple","app"]
order = 'abcdefghijklmnopqrstuvwxyz'
print(AlienStrings(words,order))