from tkinter import *

tk = Tk()

global counter 
counter = 0

def click():
   global counter
   counter += 1


btn.pack()

btn = Button(text=counter, command = click)


while 1:
   tk.update()
