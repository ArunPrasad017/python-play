def sort_letter(s):
        _id,key = s.split(' ',1)
        return (key,_id)

def reorderLogFiles(logs):
    dig_log,letter_log = [],[]
    for item in logs:
        if item.split()[1].isalpha():
            letter_log.append(item)
        else:
            dig_log.append(item)
    letter_log = sorted(letter_log,key=sort_letter)
    return letter_log+dig_log

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(reorderLogFiles(logs))
