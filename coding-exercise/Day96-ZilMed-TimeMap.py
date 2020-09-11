from collections import defaultdict
import bisect
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.Hashmap = defaultdict(list)
        
    def set(self,key, value, timestamp):
        self.Hashmap[key].append((value,timestamp))

    def get(self, key, timestamp):
        # trial with bisect fails
        # A = self.Hashmap.get(key,None)
        # if A is None:
        #     return ""
        # i = bisect(A,(timestamp,chr(127)))
        # return A[i-1][1] if i else ""

        if key not in self.Hashmap:
            return ""
        arr = self.Hashmap[key] 
        i = len(arr)-1
        while i>=0 and arr[i][1]>timestamp:
            i-=1
        return arr[i][0] if i>=0 else ""
    
    def printMap(self):
        print(self.Hashmap)
        


# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("foo","bar",1)
obj.printMap()
param_2 = obj.get('foo',1)
print(param_2)