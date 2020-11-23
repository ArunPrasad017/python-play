class HashEntry:
    def __init__(self,key,data):
        self.key = key
        self.value = data
        self.next = None # reference to a new entry using a linked list