def letterCombinations(digits):
    if len(digits) ==0:
        return None
    output = [] 
    phone = {
        '2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o'],
        '7':['p','q','r','s'],
        '8':['t','u','v'],
        '9':['w','x','y','z']
    }

    def backtrack(combination, next_digit, output):
        if len(next_digit)==0:
                output.append(combination)
        else:
            for letter in phone[next_digit[0]]:
                backtrack((combination+letter), next_digit[1:],output)
    if digits:
        backtrack("", digits,output)
    return output

digits = '234'
print(letterCombinations(digits))