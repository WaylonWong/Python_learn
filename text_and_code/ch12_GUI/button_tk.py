from tkinter import *
def clicked():
    print('I was clicked')
    
Button(text = 'click me', command = clicked).pack()
