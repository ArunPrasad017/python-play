def reorderLogFiles(logs):
    letter_logs = []
    digit_logs = []
    for log in logs:
        if log.split()[1].isalpha():
            letter_logs.append(log)
        else:
            digit_logs.append(log)

    def letter_sorter(val):
        _id, key = val.split(" ", 1)
        print(key)
        return (key, _id)

    sorted_list = sorted(letter_logs, key=letter_sorter)
    return sorted_list + digit_logs


logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
print(reorderLogFiles(logs))
