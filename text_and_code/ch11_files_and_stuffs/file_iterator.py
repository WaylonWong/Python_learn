import sys
def process(string):
    print('processing: ', string)

with open(filename) as f:
    for line in f:
        process(line)
        
for line in open(filename):
    process(line)
    
for line in sys.stdin:
    process(line)