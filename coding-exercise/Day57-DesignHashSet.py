"""
Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

add(value): Insert a value into the HashSet. 
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

Example:

MyHashSet hashSet = new MyHashSet();
hashSet.add(1);         
hashSet.add(2);         
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);          
hashSet.contains(2);    // returns true
hashSet.remove(2);          
hashSet.contains(2);    // returns false (already removed)

Note:

All values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashSet library.
"""

class MyHashSet:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.numBuckets = 15000
        self.buckets = [[] for _ in range(self.numBuckets)]
    
    def hashFunction(self,key):
        return (key%self.numBuckets)

    def add(self, key: int) -> None:
        i = self.hashFunction(key)
        if not self.contains(key):
            self.buckets[i].append(key)

    def remove(self, key: int) -> None:
        i = self.hashFunction(key)
        if self.contains(key):
            self.buckets[i].remove(key)
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        i = self.hashFunction(key)
        return key in self.buckets[i]

# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(5)
# obj.remove(5)
print(obj.contains(5))