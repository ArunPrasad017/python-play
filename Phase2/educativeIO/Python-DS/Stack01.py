from stack import Stack

def convert_int_to_bin(dec_num):
    stack = Stack()
    res =0
    while dec_num>0:
        rem = dec_num%2
        stack.push(rem)
        dec_num//=2
    while stack.get_stack():
        res =(10*res)+stack.pop()
    return str(res)

def test_function():
    assert convert_int_to_bin(52) == '110100'

test_function()