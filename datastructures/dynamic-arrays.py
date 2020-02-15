#dynamic array test
"""
import sys
n = 50
data = []
for i in range(n):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a,b))
    data.append(n)
"""
import ctypes
import sys

class DynamicArray(object):

    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n
    
    def __getitem__(self,k):
        if not 0 <= k < self.n:
            return IndexError('K is out of bounds')

        return self.A[k]

    
    def append(self,elmnt):
        if self.n ==self.capacity:
            self._resize(2*self.capacity)  # 2x if capacity is not enough
        
        self.A[self.n]=elmnt
        self.n+=1

    def _resize(self,newcap):
        B = self.make_array(newcap)

        for k in range(self.n):
            B[k] = self.A[k]

            self.A = B
            self.capacity = newcap

    def make_array(self,newcap):
        return(newcap * ctypes.py_object)()


arr = DynamicArray()
arr.append(1)
print("first")
print(len(arr))
arr.append(2)
print("second")
print(len(arr))
print(sys.getsizeof(arr))