"""
Using the Greedy algorithm - piece by piece addition
"""

def partitionLabels(S):
    dict_label = {c:i for i,c in enumerate(S)}
    res=[]
    j,anchor =0,0

    for i,c in enumerate(S):
        j = max(j,dict_label[c])
        if i==j:
            res.append(i-anchor+1)
            anchor = i+1
    return res


S = "ababcbacadefegdehijhklij"
print(partitionLabels(S))
        