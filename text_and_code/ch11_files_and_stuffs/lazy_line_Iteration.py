def process(string):
    print('processing: ', string)

import fileinput
for line in fileinput.input(filename):
    process(line)