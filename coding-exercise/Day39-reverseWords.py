def reverseWords(s):
    """
    easy method that can be used in first round - please try using data structures
    """
    # s = s.strip()
    # s2 = ""
    # lst = s.split()
    # return ' '.join(iter(lst[::-1]))

    i = 0
    N = len(s)
    s2 = ""
    while i<N:
        while i<N and s[i]==" ":
            i+=1
        j=i+1
        while j<N and s[j]!=" ":
            j+=1
        if s2!="":
            s2=s[i:j]+" "+s2
        else:
            s2+=s[i:j]
        i=j+1
    return s2

s = "the sky is blue"
s2 = "  hello world!  "
s3 = "a good   example"
print(reverseWords(s2))