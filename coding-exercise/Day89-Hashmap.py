"""
You've created a new programming language, and now you've decided to add hashmap support to it. Actually you are quite disappointed that in common programming languages it's impossible to add a number to all hashmap keys, or all its values. 
So you've decided to take matters into your own hands and implement your own hashmap in your new language that has the following operations:

insert x y - insert an object with key x and value y.
get x - return the value of an object with key x.
addToKey x - add x to all keys in map.
addToValue y - add y to all values in map.

To test out your new hashmap, you have a list of queries in the form of two arrays: queryTypes contains the names of the methods to be called (eg: insert, get, etc), and queries contains the arguments for those methods (the x and y values).

Your task is to implement this hashmap, apply the given queries, and to find the sum of all the results for get operations.

Example

For queryType = ["insert", "insert", "addToValue", "addToKey", "get"] and query = [[1, 2], [2, 3], [2], [1], [3]], the output should be hashMap(queryType, query) = 5.

The hashmap looks like this after each query:

1 query: {1: 2}
2 query: {1: 2, 2: 3}
3 query: {1: 4, 2: 5}
4 query: {2: 4, 3: 5}
5 query: answer is 5
The result of the last get query for 3 is 5 in the resulting hashmap.
"""
class Hashmap:
    def __init__(self):
        self.size = 2069
        self.map = [None]*self.size
        # self.map = []

    def _get_hash(self, key):
        return (key%self.size)

    def insert(self,lst):
        key_hash = self._get_hash(lst[0])
        key_val = lst
        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_val])
        else:
            for pair in self.map[key_hash]:
                if pair[0] == lst[0]:
                    pair[1] = lst[1]
                    return True
            self.map[key_hash].append(key_val)
        return True

    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def addToKey(self,val):
        for item in self.map:
            if item:
                print(item[0][0])
                item[0][0] += val
        return "Key updates done"
    
    def addToValue(self,val):
        for item in self.map:
            if item:
                print(item[0][1])
                item[0][1] += val
        return "Key updates done"
    
    def printf(self):
        for item in self.map:
            if item is not None:
                print(str(item))
        
def main():
    h = Hashmap()
    h.insert([1, 2])
    h.insert([2,3])
    print(h.get(2))
    h.addToKey(1)
    h.printf()
    h.addToValue(10)
    h.printf()

if __name__ == "__main__":
    main()

### Below code is wrong for the mentioned use case - we need to design our own hashmap
# def insert(dict1,lst):
#     dict1[lst[0]] = lst[1]
#     return dict1

# def addToValue(dict1,val):
#     for k,v in dict1.items():
#         dict1[k] = (dict1.get(k),0)+val
#     return dict1

# def addToKey(dict1,val):
#     dict2 ={}
#     for k,v in dict1.items():
#         dict2[k+val] = v
#     return dict2

# def get(dict1, key):
#     if key in dict1:
#         return dict1[key]
#     else:
#         return None
    
# def hashMap(queryType, query):
#     dict1 = {}
#     for action,val in zip(queryType,query):
#         if action == "addToKey":
#             dict1 = addToKey(dict1,val)
#         elif action == "addToValue":
#             dict1 = addToValue(dict1,val)
#         elif action == "get":
#             print(get(dict1,key))
#         elif action == "insert":
#             dict1 = insert(dict1, val)
#     return dict1
