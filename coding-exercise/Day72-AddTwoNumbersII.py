class Node(object):
    def __init__(self,value):
        self.data=value
        self.next=None

class LinkedList(object):
    def __init__(self):
        self.head=None
        self.tail=None

    def AddDigit(self,val):
        node = Node(val)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
    
    def PrintList(self):
        start= self.head
        temp = []
        while start is not None:
            temp.append(str(start.data))
            start = start.next
        return temp
    
    def reverseList(self):
        head = self.head
        currNode, prevNode, nextNode = None, None, None
        while head:
            currNode =head
            nextNode = head.next
            head.next = prevNode
            prevNode = currNode
            head = nextNode
        return prevNode

def AddTwoLists(lst1,lst2):
    
    pass

def main():
    
    lst1=LinkedList()
    lst1.AddDigit(7)
    lst1.AddDigit(2)
    lst1.AddDigit(4)
    lst1.AddDigit(3)
    print(lst1.PrintList())

    lst2 = LinkedList()
    lst2.AddDigit(5)
    lst2.AddDigit(6)
    lst2.AddDigit(4)
    print(lst2.PrintList())

    revLst1 = lst1.reverseList()
    revLst2 = lst2.reverseList()

    

main()