def decryptString(s):
    string = 'abcdefghijklmnopqrstuvwxyz'
    dic1 = {}
    for i,c in enumerate(string):
        if i<9:
            dic1[str(i+1)] = c
        else:
            dic1[str(i+1)+'#'] = c
    str2 = ""
    i = 0
    l = len(s)
    while i<len(s):
        if i+2<l and s[i+2]=='#':
            str2+=dic1[s[i:i+3]]
            i+=3
        else:
            str2+=dic1[s[i]]
            i+=1
    return str2

s = "10#11#12"
print(decryptString(s))