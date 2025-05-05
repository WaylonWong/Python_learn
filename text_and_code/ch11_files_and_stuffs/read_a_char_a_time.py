def process(string):
    print('processing: ', string)

with open(filename) as f:
    while True:
        char = f.read(1)
        if not char: break
        process(char)
  

with open(filename) as f:
    for char in f.read():
        process(char)