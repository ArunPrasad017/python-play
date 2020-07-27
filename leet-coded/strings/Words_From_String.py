import collections
def countCharacters(words,chars):
    dict_chars = collections.Counter(chars)
    str_length = 0
    for word in words:
        word_dict = collections.Counter(word)
        status = all(word_dict[i] <= dict_chars[i] for i in word_dict)
        if status:
            str_length+=len(word)
    return str_length


    #     for k,v in word_dict.items():
    #         try:
    #             if dict_chars[k] >= word_dict[k]:
    #                 status = True
    #             else:
    #                 status = False
    #         except KeyError:
    #             status = False
    #             break
    #     if status:
    #         str_length+=len(word)
    # return str_length


word_list = ["hello","world","leetcode"]
chars = "welldonehoneyr"
print(countCharacters(word_list,chars))
