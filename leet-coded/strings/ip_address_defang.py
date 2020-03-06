def defangIPaddr(address):
    str2=""
    for i in range(0,len(address)):
        if address[i] =='.':
            str2+='[.]'
        else:
            str2+=address[i]
    return str2