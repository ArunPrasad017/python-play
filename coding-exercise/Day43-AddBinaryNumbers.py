def addBinary(a, b):
    n = max(len(a), len(b))
    a = a.zfill(n)
    b = b.zfill(n)
    carry = 0
    i = n - 1
    total = ""
    while i >= 0:
        _sum = int(a[i]) + int(b[i]) + carry
        total = "0" + total if _sum % 2 == 0 else "1" + total
        carry = _sum // 2
        i -= 1
    if carry:
        return str(carry) + total
    return total


a = "1010"
b = "1011"
print(addBinary(a, b))
