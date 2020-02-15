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

def checkKeyValuePairExistence(d,key,value):
    try:
        return(d[key]==value)
    except KeyError:
        return False

def balance_checks(s):
    dict_balanced = {
        '(':')',
        '{':'}',
        '[':']',
    }

    stack1 = Stack()

    for char in s:
        is_balanced = False
        if(char in dict_balanced.keys()):
            stack1.push(char)
        elif(char in dict_balanced.values()):
            if(stack1.isEmpty()):
                return False
            else:
                element = stack1.peek()
                is_balanced = checkKeyValuePairExistence(dict_balanced,element,char)
                if(is_balanced):
                    stack1.pop()

    if(stack1.isEmpty()):
        return True
    else:
        return False


if __name__ == "__main__":
    s = '{[[[(([]   ))]]]}'
    bal_check = balance_checks(s)
    print(bal_check)
