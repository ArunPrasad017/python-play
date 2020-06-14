"""
String Compression - not as same as the RunLengthEncoding
"""

from collections import OrderedDict

def string_Compression(s):
    encode_str =''
    prev=''
    count = 1

    if s=='':
        return encode_str
    for c in s:
        if c==prev:
            count+=1
        elif c!=prev:
            if prev:
                encode_str+=(prev+str(count))
            count=1
        prev = c
    else:
        return encode_str

s='aaaabbbbbbccccaa'
print(string_Compression(s))