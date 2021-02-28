def reverseVowels(s):
    vowels = "aeiouAEIOU"
    s = list(s)
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] in vowels:
            while s[right] not in vowels:
                right -= 1
            s[left], s[right] = s[right], s[left]
            right -= 1
        left += 1
    return "".join(s)
