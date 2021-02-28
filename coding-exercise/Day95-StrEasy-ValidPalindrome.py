def validPalindrome(s):
    start,end = 0,len(s)-1
    while start<end:
        while start<end and not s[start].isalnum():
            start+=1
        while start<end and not s[end].isalnum():
            end-=1
        if s[start].lower() !=s[end].lower() and start<end:
            return False
        start+=1
        end-=1
    return True

s = "  A man, a plan, a canal: Panama  "
# print(validPalindrome(s))

# def find_series(n):
#     d={'A':1}
#     for i in range(2,27):
#         key=chr(i+64)
#         d[key]=i*d[chr(i+63)]+d[chr(i+63)]
#     d1 ={}
#     l,l1=[],[]
#     string= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     for i in d:
#         if d[i]==l[i]:
#             a= n//l[i]
#             n-=(l[i]*a)
#         l1.append(string[len(l)-i-1]*a)
#         if n==0:
#             break
#     return ''.join(sorted(l1))

# n = 10
# print(find_series(n))



n = int(input())
di = {}
li = [1,3]
for i in range(4,29):
    li.append(i*li[-1])
    li = li[:27]
x = 0
for i in range(65,91):
    if li[x] not in di:
        di[li[x]] = chr(i)
x+= 1
s = ''
for i in range(26,-1,-1):
# print(n//li[i])
    if n//li[i] > 0:
        s+=di[li[i]]*(n//li[i])
        n = n%li[i]
print(''.join(sorted(s)))