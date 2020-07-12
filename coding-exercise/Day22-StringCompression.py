def compress(chars):
    index = 0
    count =1
    for j in range(1,len(chars)+1):
        if j<len(chars) and chars[j]==chars[j-1]:
            count+=1
        else:
            chars[index] = chars[j-1]
            index+=1
            if count>1:
                for i in str(count):
                    chars[index] = i
                    index+=1
            count=1
    chars = chars[:]
    return index,chars
lst = ["a","a","b","b","c","c","c"]
lst2 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(compress(lst2))