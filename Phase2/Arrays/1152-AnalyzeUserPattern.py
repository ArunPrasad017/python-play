from collections import defaultdict, Counter
from itertools import combinations

def mostVisitedPattern(username, timestamp, website):
    tuples_lst = sorted([(a,b,c) for a,b,c in zip(username,timestamp,website)],key=lambda x:x[1])
    d1 = defaultdict(list)
    d2 = Counter()
    for user,ts,site in tuples_lst:
        d1[user].append(site)
    for k,v in d1.items():
        keys = set(combinations(v,3))
        for key in keys:
            d2[key]+=1
    sorted_dict = sorted(d2,key=lambda x:(-d2[x],x))
    return sorted_dict[0]

username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
timestamp = [1,2,3,4,5,6,7,8,9,10]
website = ["home","about","career","home","cart","maps","home","home","about","career"]

print(mostVisitedPattern(username, timestamp, website))