"""
557. Reverse Words in a String III

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

"""
def reverseWords(s):
    lst = s.split()
    return ' '.join([i[::-1] for i in lst])

s = "Let's take LeetCode contest"
print(reverseWords(s))