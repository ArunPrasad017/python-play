def weighted_strings(num):
    d = {'a': 1, 'b': 3}
    temp,res = "",[]
    for i in range(2,27):
        key = chr(97+i)
        prev_key = chr(96+i)
        d[key] = ((i+1)*d[prev_key])+d[prev_key]
    lst = list(d.keys())
    for i in range(len(lst)-1,-1,-1):
        r=num//d[lst[i]]
        temp+=lst[i]*r
        num=num%d[lst[i]]
        if num==0:
            res.append(temp)
            temp=""
            continue
    return res

print(weighted_strings(200))