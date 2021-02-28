def reverseVowels(s):
    vowels = 'aeiouAEIOU'
    s=list(s)
    right = len(s)-1

    for left in range(right):
        if s[left] in vowels:
            while s[right] not in vowels:
                right-=1
            s[left],s[right] = s[right],s[left]
            right-=1
    return ''.join(s)