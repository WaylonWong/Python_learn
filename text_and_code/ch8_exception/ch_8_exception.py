class MuffledCalculator:
    muffled = False
    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print("Division by zero is illegal")
            else:
                raise

try:
x = int(input('Enter the first number: '))
y = int(input('Enter the second number: '))
print(x / y)
except ZeroDivisionError:
print("The second number can't be zero!")
except TypeError:
print("That wasn't a number, was it?")

try:
x = int(input('Enter the first number: '))
y = int(input('Enter the second number: '))
print(x / y)
except (ZeroDivisionError, TypeError, NameError):
print('Your numbers were bogus ...')

try:
x = int(input('Enter the first number: '))
y = int(input('Enter the second number: '))
print(x / y)
except (ZeroDivisionError, TypeError) as e:
print(e)

while True:
    try:
        X = int(input('Enter the first number:'))
        Y = int(input('Enter the second number:'))
        print('X/Y = ',X/Y)
    except:
        print('invalid input, please input again...')
    else:
        break
        
while True:
    try:
        X = int(input('Enter the first number:'))
        Y = int(input('Enter the second number:'))
        print('X/Y = ',X/Y)
    except Exception as e:
        print('invalid input',e)
        print('please input again...')
    else:
        break
        
x = None
try:
    x = 1 / 0
finally:
    print('Cleaning up ...')
    del x

def faulty():
    raise Exception('Something is wrong')

def ignore_exception():
    faulty()

def handle_exception():
    try:
        faulty()
    except:
        print('Exception handled!')
  

# inefficient because it has to look up the key 'occupation' twice, once to see if teh key exsits and once to get the value 
# def describe_person(person):
    # print('Description of person: ',person[name])
    # print('Age: ', person[age])
    # if 'occupation' in person:
        # print('occupation: ',preson[occupation])

def describe_person(person):
    print('Description of person: ',person[name])
    print('Age: ', person[age])
    try:
        print('occupation: ',preson[occupation])
    except keyError:
        pass
 
try:
    obj.write
except AttributeError:
    print('the object is unwritalbe')
else:
    print('the object is writable')


