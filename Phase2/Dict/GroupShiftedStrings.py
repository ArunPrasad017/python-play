from collections import defaultdict
def groupStrings(strings):
    # design key properly and uniquely
    dict1 = defaultdict(list)
    for s in strings:
        key =()
        for i in range(len(s)-1):
            temp=ord(s[i+1])-ord(s[i])
            key+=(temp,)
        dict1[key].append(s)
    return dict1.values()


lst = ["abc","bcd","acef","xyz","az","ba","a","z"]
print(groupStrings(lst))
