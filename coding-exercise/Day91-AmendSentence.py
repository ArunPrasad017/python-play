"""
You have been given a string s, which is supposed to be a sentence. However, someone forgot to put spaces 
between the different words, and for some reason they capitalized the first letter of every word. Return the sentence after making the following amendments:

Put a single space between the words.
Convert the uppercase letters to lowercase.
Example

For s = "CodesignalIsAwesome", the output should be
amendTheSentence(s) = "codesignal is awesome";
For s = "Hello", the output should be
amendTheSentence(s) = "hello".

"""
def amendTheSentence(s):
    res=""
    for i,c in enumerate(s):
        if ord(c) in range(65,92):
            if i!=0:
                res+=str(" " +c.lower())
            else:
                res+=c.lower()
        else:
            res+=c
    return res
            

def amendTheSentence(s):
    res=""
    for i,c in enumerate(s):
        if ord(c) in range(65,92):
            res += str(" " +c.lower()) if i!=0 else c.lower()
        else:
            res+=c
    return res