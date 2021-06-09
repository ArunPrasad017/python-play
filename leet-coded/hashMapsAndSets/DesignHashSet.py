class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_set = []
        

    def add(self, key: int) -> None:
        if key not in self.hash_set:
            self.hash_set.append(key) 
        else:
            return
        
    def remove(self, key: int) -> None:
        if key not in self.hash_set:
            return False
        else:
            self.hash_set.remove(key) 

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return if key in self.hash_set
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)