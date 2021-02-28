from collections import Counter
def find_permutation(str1, pattern):
    start, matched=0,0
    d = Counter(pattern)
    for end in range(len(str1)):
        if str1[end] in d:
            d[str1[end]]-=1
            if d[str1[end]]==0:
                matched+=1
        if matched == len(pattern):
            return True
        if end>=len(pattern)-1:
            start_ch = str1[start]
            start+=1
            if start_ch in d:
                if d[start_ch]==0:
                    matched-=1
                d[start_ch]+=1
    return False

def main():
    print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
    # print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
    # print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
    # print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))

main()