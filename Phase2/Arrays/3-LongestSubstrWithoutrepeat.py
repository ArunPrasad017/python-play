def longest_without_repeat(string):
    if not string:
        return 0
    res_lst =[string[0]]
    max_len = 1
    for i in range(1,len(string)):
        if string[i] not in res_lst:
            res_lst.append(string[i])
        else:
            if len(res_lst)>max_len:
                max_len=len(res_lst)
                res_lst.pop(0)
                res_lst.append(string[i])
    return max(max_len,len(res_lst))


s = 'pwwkew'
print(longest_without_repeat(s))