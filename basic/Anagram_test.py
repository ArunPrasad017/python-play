def anagram(s1, s2):
    x1 = "".join(s1.split()).lower()
    x2 = "".join(s2.split()).lower()
    if len(x1) == len(x2):
        x1 = "".join(sorted(x1))
        x2 = "".join(sorted(x2))
        if x1 == x2:
            print("{0} and {1} are an anagram".format(s1, s2))
        else:
            print("Not an anagram")


anagram("Clint eastwood", "old west action")
anagram("dog", "god")
anagram("aa", "bb")

# Main solution


def anagram2(s1, s2):
    s1 = "".join(s1.split()).lower()
    s2 = "".join(s2.split()).lower()

    # edge case
    if len(s1) != len(s2):
        return False

    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False

    return True
