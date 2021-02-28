import os
# f = open("test.txt",'r')
# print(f.name)
# f.close()

# using context manager
with open("test.txt",'r') as f:
    # f_contents = f.read()
    # f_contents = f.readline()
    # print(f_contents,end=' ')

    # f_contents = f.readline()
    # print(f_contents,end=' ')
    # for line in f:
    #     print(line, end=' ')
    # f_contents = f.read(10)
    # print(f_contents)

    # iterate over loop - small chunks at a time
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents)
    # while len(f_contents)>0:
    #     print(f_contents,end='*')
    #     f_contents = f.read(size_to_read)
    f.seek(0)
    f_contents = f.read(size_to_read)
    #  print(f.tell())
    print(f_contents)
