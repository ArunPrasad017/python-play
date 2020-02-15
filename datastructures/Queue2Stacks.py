
class Queue2Stacks(object):
    
    def __init__(self):
        
        # Two Stacks
        self.stack1 = []
        self.stack2 = []
     
    def enqueue(self,element):
        self.stack1.append(element)
        self.stack2 = self.stack1[::-1]
    
    def dequeue(self):
        if(len(self.stack2)>0):
            return(self.stack2.pop())
        else:
            for i in range(0,len(self.stack1)):
                self.stack1.pop()
            return("Empty queue")

q = Queue2Stacks()

# for i in range(0,5):
#     print(q.enqueue(i))

for i in range(0,5):
    print(q.dequeue())