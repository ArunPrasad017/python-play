def subtractProductAndSum(n):
    product, total_sum = 1, 0
    while n > 0:
        rem = n % 10
        product = product * rem
        total_sum += rem
        n //= 10
    return product - total_sum


print(subtractProductAndSum(234))