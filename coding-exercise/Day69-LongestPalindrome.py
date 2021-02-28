from collections import Counter
def longestPalindrome(s):
    if len(s)==0:
        return 0
    d = Counter(s)
    odd_count = 0
    even_count =0
    odd_present = False
    for v in d.values():
        if v%2==0:
            even_count+=int(v)
        else:
            odd_present = True
            odd_count+=(int(v)-1)
    if odd_present:
        return even_count+odd_count+1
    return even_count+odd_count

s= 'abccccdd'
print(longestPalindrome(s))
