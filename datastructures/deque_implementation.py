class deque(object):
    def __init__(self, *args, **kwargs):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        return self.items.append(item)

    def addRear(self, item):
        return self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeLast(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


dq = deque()
dq.addFront("hello")
dq.addRear("world")
dq.addFront("Program: ")
print(dq.items)

dq.removeFront()
print(dq.items)

dq.removeLast()
print(dq.items)
