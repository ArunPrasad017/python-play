## add two numbers without using an operator
# using xor operator

def add(a,b):
    while b!=0:
        c = a&b
        a = a^b
        b=c<<1
    return a

print(add(3,5))