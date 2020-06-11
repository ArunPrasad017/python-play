def isHappy(n):
    def get_next(n):
        total_sum = 0 
        while n>0:
            digit = n%10
            n = n//10
            total_sum += digit**2
        return total_sum
    seen = set()
    while n not in seen and n!=1:
        seen.add(n)
        n = get_next(n)
    return n==1

n = 19
print(isHappy(n))