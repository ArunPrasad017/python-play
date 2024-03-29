import random


class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashSet = set()

    def insert(self, val: int):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.hashSet:
            self.hashSet.add(val)
            return True
        else:
            return False

    def remove(self, val: int):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.hashSet:
            self.hashSet.remove(val)
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        """
        return random.sample(self.hashSet, 1)[0]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
