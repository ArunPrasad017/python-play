def removeVowels(S):
    str2=""
    for char in S:
        if char not in ['a','e','i','o','u']:
            str2+=char
    return str2