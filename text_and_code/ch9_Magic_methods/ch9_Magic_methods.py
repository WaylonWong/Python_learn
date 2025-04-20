class FooBar:
    def __init__(self):
        self.somevar = 42

class Foo:
    def __init__(self, value=42):
        self.somevar = value

class Bird:
    def __init__(self):
        self.hungry=True
    def eat(self):
        if self.hungry:
            print('Ahhh...')
            self.hungry=False
        else:
            print('No, thank you!')

class SongBird(Bird):
    def __init__(self):
        # Bird.__init__(self)
        super().__init__()
        self.sound = 'Squark!'
    def sing(self):
        print(self.sound)
        
 
def check_index(key):
"""
Is the given key an acceptable index?
To be acceptable, the key should be a non-negative integer. If it
is not an integer, a TypeError is raised; if it is negative, an
IndexError is raised (since the sequence is of infinite length).
"""
if not isinstance(key, int): raise TypeError
if key < 0: raise IndexError

ArithmeticSequence:
    def __init__(self, start=0, step=1):
        """
        Initialize the arithmetic sequence.
        start - the first value in the sequence
        step - the difference between two adjacent values
        changed - a dictionary of values that have been modified by
        the user
        """
        self.start = start # Store the start value
        self.step = step # Store the step value
        self.changed = {} # No items have been modified
    def __getitem__(self, key):
        """
        Get an item from the arithmetic sequence.
        """
        check_index(key)
        try: return self.changed[key] # Modified?
        except KeyError: # otherwise ...
        return self.start + key * self.step # ... calculate the value
    def __setitem__(self, key, value):
        """
        Change an item in the arithmetic sequence.
        """
        check_index(key)
        self.changed[key] = value # Store the changed value
        
class CountList(list):
    def __init__(self, *args):
        super().__init(*args)
        self.count = 0
    def __getitem__(self, index):
        self.count += 1
        return super(CountList, self).__getitem__(index)

class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def set_size(self, size):
        self.width, self.height = size
    def get_size(self):
        return self.width, self.height
    size = property(get_size, set_size)

class Myclass:
    @staticmethod
    def smeth():
        print('this is a static method')
    # smeth = staticmethod(smeth)
    @classmethod
    def cmeth(cls):
        print('this is a class method of ', cls)
    # cmeth = classmethod(cmeth)

class Rectangle_1:
    def __init__ (self):
        self.width = 0
        self.height = 0
    def __setattr__(self, name, value):
        if name == 'size':
            self.width, self.height = value
        else:
            self. __dict__[name] = value
    def __getattr__(self, name):
        if name == 'size':
            return self.width, self.height
        else:
            raise AttributeError()

class Fibs:
    def __init__(self):
        self.a = 0
        self.b =1
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a
    def __iter__(self):
        return self

def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element
            
def recur_flatten(nested):
    try:
        # Don't iterate over string-like objects:
        try: nested + ''
        except TypeError: pass
        else: raise TypeError
        for sublist in nested:
            for element in recur_flatten(sublist):
                yield element
    except TypeError:
        yield nested