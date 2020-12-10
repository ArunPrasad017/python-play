def calculateTime(keyboard, word):
    dict1 = {c: i for i, c in enumerate(keyboard)}
    current_pos = 0
    val = 0
    for c in word:
        if c in dict1:
            val += abs(current_pos - dict1[c])
            current_pos = dict1[c]
    return val


# keyboard = "abcdefghijklmnopqrstuvwxyz"; word = "cba"
keyboard = "pqrstuvwxyzabcdefghijklmno"
word = "leetcode"

print(calculateTime(keyboard, word))
