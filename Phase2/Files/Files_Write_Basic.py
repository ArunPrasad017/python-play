with open("test.txt",'r') as rf:
    with open("test3.txt",'w') as wf:
        for line in rf:
            wf.write(line)

with open("flash-logo.jpg",'rb') as rf:
    with open("flash-logo2.jpg",'wb') as wf:
        for line in rf:
            wf.write(line)

with open("flash-logo.jpg",'rb') as rf:
    with open("flash-logo2.jpg",'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk)>0:
            wf.write(rf_chunk)
            rf_chunk=rf.read(chunk_size)