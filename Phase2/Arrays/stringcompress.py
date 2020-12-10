def compress(chars):
    idx,cnt = 0,1
    for i in range(1,len(chars)+1):
        if i<len(chars) and chars[i-1]==chars[i]:
            cnt+=1
        else:
            chars[idx]=chars[i-1]
            idx+=1
            if cnt>1:
                for c in str(cnt):
                    chars[idx]=c
                    idx+=1
            cnt=1
    return idx


chars = ["a","a","b","b","c","c","c"]
print(compress(chars))