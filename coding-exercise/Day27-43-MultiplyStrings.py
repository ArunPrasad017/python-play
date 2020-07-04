def multiply(num1,num2):
    if len(num1) ==0 or len(num2)==0:
        return "0"
    n1= len(num1)
    n2= len(num2)
    
    num1=num1[::-1]
    num2=num2[::-1]

    res = [0]*(n1+n2)
    for j in range(n2):
        for i in range(n1):
            res[i+j] = res[i+j]+(int(num1[i]) * int(num2[j]))
            res[i+j+1] = res[i+j+1]+res[i+j]//10
            res[i+j] = res[i+j]%10
    i=len(res)-1
    while i>0 and res[i]==0:
        i-=1
    res=res[:i+1]
    return "".join(map(str,res[::-1]))

num1 = "123" 
num2 = "456"

print(multiply(num1,num2))