class TwoSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lst = []
        self.map = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.lst.append(number)
        self.map[number] = len(self.lst) - 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for i in range(len(self.lst)):
            rem = value - (self.lst[i])
            if rem in self.map and i != self.map[rem]:
                return True
        return False


res = []
res.insert()

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
