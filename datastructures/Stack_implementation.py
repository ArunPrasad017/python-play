class Stack(object):

    def __init__(self):
        self.items =[]
        
    def isEmpty(self):
        return self.items == []
    
    def push(self,item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

s = Stack()
s.push(1)
s.push('string')
x = s.peek()
print(x)
# s.push(True)
# print(s.size())
# print(s)
# s.pop()
# s.pop()
# s.pop()
# print(s.isEmpty())
