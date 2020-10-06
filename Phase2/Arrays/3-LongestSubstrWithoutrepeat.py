def longest_without_repeat(s):
    if not s:
        return 0
    res_dict={}
    l,output =0,0

    for r in range(len(s)):
        if s[r] not in res_dict:
            output = max(output,r-l+1)
        else:
            if res_dict[s[r]]<l:
                output = max(output,r-l+1)
            else:
                l = res_dict[s[r]]+1
        res_dict[s[r]] = r
    return output

s = 'abcdabde'
#s = 'bbbbbb'
print(longest_without_repeat(s))