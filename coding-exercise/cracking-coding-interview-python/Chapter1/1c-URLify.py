"""
In Python strings are immutable and hence we need to have them as 
new strings and the runtime complexity and space complexity is o(n)
"""


def urlify(string, length):
    string2 = ""
    for i in range(0, length):
        if string[i] == " ":
            string2 += "%20"
        else:
            string2 += string[i]
    return string2


# string = 'Mr John Smith    '
# length = 13
string = "much ado about nothing"
length = 22
print(urlify(string, length))
