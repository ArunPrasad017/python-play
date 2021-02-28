def isPrime(n):
    if n <= 1:
        return 0
    if n <= 3:
        return 1
    if n % 2 == 0 or n % 3 == 0:
        return 0
    i = 5
    while (i * i) <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return 0
        i += 6
    return 1


def countPrimes(n):
    i = 0
    dict1 = {}
    while i < n:
        dict1[i] = isPrime(i)
        i += 1
    print(dict1)
    return sum(dict1.values())


print(countPrimes(10))
