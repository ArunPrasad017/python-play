def hammingDistance(x,y):
    count =0
    val = x^y
    while val>0:
        if val&1:
            count+=1
        val>>=1
    return count 

x = 1; y = 4
print(hammingDistance(x,y))