from collections import Counter
import heapq
if __name__ == '__main__':
    s = 'aabbbccde'
    d=Counter()
    for c in s:
        d[c]+=1
    lst =sorted(d,key= lambda x:(-d[x],x))
    for i in range(3):
        print(lst[i]+" "+str(d[lst[i]]))