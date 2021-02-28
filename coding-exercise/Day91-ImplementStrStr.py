"""
Avoid using built-in functions to solve this challenge. Implement them yourself, since this is what you would be asked to do during a real interview.

Implement a function that takes two strings, s and x, as arguments and finds the first occurrence of the string x in s. 
The function should return an integer indicating the index in s of the first occurrence of x. If there are no occurrences of x in s, return -1.

Example

For s = "CodefightsIsAwesome" and x = "IA", the output should be
strstr(s, x) = -1;
For s = "CodefightsIsAwesome" and x = "IsA", the output should be
strstr(s, x) = 10.

passed for 25/27 cases
"""

def strstr(s, x):
    if s==x:
        return 0
    if len(s)<len(x):
        return -1
    for i in range((len(s) - len(x))+1):
        if x==s[i:(i+len(x))]:
            return i
    return -1

# Additional
def baseConversion(n, x):
    return hex(int(str(n),x))[2:]
