def defangIPaddr(address):
    str2=""
    for addres in address:
        str2 += '[.]' if addres == '.' else addres
    return str2