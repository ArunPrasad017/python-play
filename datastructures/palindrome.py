#code
def check_palindrome(str1):
    str2=""
    for i in range(len(str1)-1,-1,-1):
        str2+=str1[i]
    if str1==str2:
        return 'Yes'
    else:
        return 'No'

T = int(input())
len_str = int(input())
str1 = input()

for i in range(T,0,-1):
    print(check_palindrome(str1))