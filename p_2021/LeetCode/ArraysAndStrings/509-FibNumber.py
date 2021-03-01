def rec_fib(n):
    if n in [0, 1]:
        return 1
    return rec_fib(n-1)+rec_fib(n-2)
            
def fib(n):
    if not n:
        return 0
    return rec_fib(n-1)

n = 5
print(fib(n))