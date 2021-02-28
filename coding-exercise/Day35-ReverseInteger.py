def reverse(x):
    if x==0 or x not in range(-2147483648,2147483647):
            return 0
    isNeg = False
    if x<0:
        isNeg=True
    s = str(abs(x))
    s2=""
    for i in range(len(s)-1,-1,-1):
        if i!=0 and s[i]=='0' and len(s2)<1:
            continue
        s2+=s[i]
    if isNeg and int(s2) in range(-2147483648,2147483647):
        return (-1)* int(s2)
    elif int(s2) in range (-2147483648,2147483647):
        return int(s2)
    return 0

x=901000
print(reverse(x))