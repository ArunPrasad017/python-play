from collections import OrderedDict
class FirstUnique:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.od = OrderedDict()
        for num in self.nums:
            if num in self.od:
                self.od[num]+=1
            else:
                self.od[num]=1

    def showFirstUnique(self) -> int:
        for k,v in self.od.items():
            if v==1:
                return k
        return -1

    def add(self, value: int) -> None:
        if value in self.od:
            self.od[value]+=1
        else:
            self.od[value]=1
        
# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)