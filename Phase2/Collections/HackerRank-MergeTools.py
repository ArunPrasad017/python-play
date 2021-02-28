def merge_the_tools(n, k):
    # your code goes here
    temp = [n[i:i+k] for i in range(0,len(n),k)]
    for item in temp:
        new_set=[]
        for c in item:
            if c not in new_set:
                new_set.append(c)
        print(''.join(new_set))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)