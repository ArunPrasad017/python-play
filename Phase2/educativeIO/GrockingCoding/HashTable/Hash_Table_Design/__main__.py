from HashTable import HashTable

ht = HashTable()
print(ht.slots)
ht.resize()
print(ht.slots)
ht.insert(2,"London")
ht.insert(7,"Cairo")
ht.insert(8,"Delhi")
ht.insert(28,"Canberra")
print(ht.get_size())
ht.delete(2)
print(ht.get_size())
ht.search(2)