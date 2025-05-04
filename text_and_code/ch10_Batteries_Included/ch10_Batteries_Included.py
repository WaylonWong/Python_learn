
# hello4.py
def hello():
    print("Hello, world!")
def test():
    hello()
if __name__ == '__main__': test()


# Adding Line Numbers to a Python Script
# numberlines.py
import fileinput
for line in fileinput.input(inplace=True):
    line = line.rstrip()
    num = fileinput.lineno()
    print('{:<50} # {:2d}'.format(line, num))