def binary_add1(a, b):
    x, y = int(a, 2), int(b, 2)

    while y:
        ans = x ^ y
        carry = (x & y) << 1
        x, y = ans, carry
    return bin(x)[2:]


a = "1010"
b = "1"

binary_add1(a, b)
