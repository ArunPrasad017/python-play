# from - https://www.youtube.com/watch?v=BCZWQTY9xPE

# 1. prime print
# method 1
# for num in range(100):
#     if all(num%i!=0 for i in range(2,num//2)):
#         print(num)

# method 2 - eratosthenes sieve method(for returning a list)
def test_prime(n):
    res = [True for i in range(n + 1)]
    p = 2
    while p ** 2 <= n:
        if res[p] == True:
            for i in range(p ** 2, n + 1, p):
                res[i] = False
        p += 1
    return [i for i in range(1, len(res)) if res[i] == True]


print(test_prime(100))

# recursion loop
def fib_series(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib_series(n - 1) + fib_series(n - 2)


# print(fib_series(6))

# valid palnidrome checks (two pointer)
def is_palindrome(s, a, b):
    while a < b:
        if s[a] != s[b]:
            return False
        a += 1
        b -= 1
    return True


def palindromeChecker(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return is_palindrome(s.lower(), left + 1, right) or is_palindrome(
                s.lower(), left, right - 1
            )
        left += 1
        right -= 1
    return True


s = "ramar"
print(palindromeChecker(s))
