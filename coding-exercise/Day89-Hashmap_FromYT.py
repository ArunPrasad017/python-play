# # Hash Map

# class HashMap:
#     def __init__(self):
#         self.size = 6
#         self.map = [None] * self.size
#     def _get_hash(self, key):
#         hash = 0
#         for char in str(key):
#             hash += ord(char)
#         return hash % self.size
	
#     def add(self, key, value):
#         key_hash = self._get_hash(key)
#         key_value = [key, value]
#         if self.map[key_hash] is None:
#                 self.map[key_hash] = list([key_value])
#                 return True
#         else:
#             for pair in self.map[key_hash]:
#                 if pair[0] == key:
#                     pair[1] = value
#                     return True
#         self.map[key_hash].append(key_value)
#         return True
		
#     def get(self, key):
#         key_hash = self._get_hash(key)
#         if self.map[key_hash] is not None:
#             for pair in self.map[key_hash]:
#                 if pair[0] == key:
#                     return pair[1]
#         return None
		
#     def delete(self, key):
#         key_hash = self._get_hash(key)
#         if self.map[key_hash] is None:
#                 return False
#         for i in range (0, len(self.map[key_hash])):
#             if self.map[key_hash][i][0] == key:
#                 self.map[key_hash].pop(i)
#                 return True
#         return False

#     def keys(self):
#         arr = []
#         for i in range(0, len(self.map)):
#             if self.map[i]:
#                 print(self.map[i])
#                 arr.append(self.map[i][0])
#         return arr

#     def printf(self):
#         print('---PHONEBOOK----')
#         for item in self.map:
#             if item is not None:
#                 print(str(item))

# h = HashMap()
# h.add('Bob', '567-8888')
# h.add('Ming', '293-6753')
# h.add('Ming', '333-8233')
# h.add('Ankit', '293-8625')
# h.add('Aditya', '852-6551')
# h.add('Alicia', '632-4123')
# h.add('Mike', '567-2188')
# h.add('Aditya', '777-8888')
# h.printf()
# h.delete('Bob')
# h.printf()
# print('Ming: ' + h.get('Ming'))
# print(h.keys())

class Bucket:
    def __init__(self):
        self.bucket = []

    def get(self, key):
        for (k, v) in self.bucket:
            if k == key:
                return v
        return -1

    def update(self, key, value):
        found = False
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = [key, value]
                found = True
                break
        if not found:
            self.bucket.append([key, value])

    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]

class MyHashMap(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # better to be a prime number, less collision
        self.key_space = 2069
        self.hash_table = [Bucket() for i in range(self.key_space)]

    def insert(self, lst):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        key = lst[0]
        value = lst[1]
        hash_key = key % self.key_space
        self.hash_table[hash_key].update(key, value)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        hash_key = key % self.key_space
        return self.hash_table[hash_key].get(key)
    
    def addToKey(self,val):
        for i in range(len(self.hash_table)):
            if self.hash_table[i]:
                print(self.hash_table[i][0])
                self.map[i]+=val
        return "Key updates done"

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

def main():
    h = MyHashMap()
    h.insert([1, 2])
    h.insert([2,3])
    print(h.get(2))
    h.addToKey(1)

if __name__ == "__main__":
    main()