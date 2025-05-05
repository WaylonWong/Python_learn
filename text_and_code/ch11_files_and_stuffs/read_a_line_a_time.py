def process(string):
    print('processing: ', string)
    
with open(filename) as f:
    while(True):
        line = f.readline()
        if not line: break
        process(line)

with open(filename) as f:
    for line in f.readlines():
        process(line)        