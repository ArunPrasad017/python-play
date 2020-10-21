from collections import OrderedDict
N = int(input())
od = OrderedDict() 
for _ in range(N):
    key = input()
    if key not in od:
        od[key]=1
    else:
        od[key]+=1
# lst = [v for k,v in od.items()]
print(len(od))
print(*od.values())
