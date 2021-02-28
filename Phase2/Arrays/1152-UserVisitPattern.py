"""
Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], 
timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]
# Output: ["home","about","career"]
# Explanation: 
# The tuples in this example are:
# ["joe", 1, "home"]
# ["joe", 2, "about"]
# ["joe", 3, "career"]
# ["james", 4, "home"]
# ["james", 5, "cart"]
# ["james", 6, "maps"]
# ["james", 7, "home"]
# ["mary", 8, "home"]
# ["mary", 9, "about"]
# ["mary", 10, "career"]
# The 3-sequence ("home", "about", "career") was visited at least once by 2 users.
# The 3-sequence ("home", "cart", "maps") was visited at least once by 1 user.
# The 3-sequence ("home", "cart", "home") was visited at least once by 1 user.
# The 3-sequence ("home", "maps", "home") was visited at least once by 1 user.
# The 3-sequence ("cart", "maps", "home") was visited at least once by 1 user.
"""
from collections import defaultdict
from itertools import combinations

def mostVisitedPattern(username, timestamp, website):
    d1 = defaultdict(list)
    d2 = defaultdict(int)
    tuple_list = sorted([(b,a,c) for a,b,c in zip(username,timestamp,website)])
    for time,user,site in tuple_list:
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

username= ["h","eiy","cq","h","cq","txldsscx","cq","txldsscx","h","cq","cq"]
timestamp = [527896567,334462937,517687281,134127993,859112386,159548699,51100299,444082139,926837079,317455832,411747930]
website= ["hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","yljmntrclw","hibympufi","yljmntrclw"]

username = ["dowg","dowg","dowg"]
timestamp=[158931262,562600350,148438945]
website = ["y","loedo","y"]
print(mostVisitedPattern(username, timestamp, website))
