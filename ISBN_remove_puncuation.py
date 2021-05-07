import math as m
from tkinter import *
from tkinter.messagebox import *
import tkinter as tk

root =tk.Tk()

canvas1 =tk.Canvas(root, width = 300, height=100)
canvas1.pack()

label1 = tk.Label(root,text='ISBN:')
label1.config(font=('helvetica',14))

canvas1.create_window(50, 25, window=label1)

entry1= tk.Entry(root)
canvas1.create_window(150, 25 , window=entry1)

def isbn():
    remove = set('-+ ')
    x1 = entry1.get()
    Ans=tk.Label(root,text=(''.join(cha for cha in x1 if not cha in remove)),font=('helvetica',12,'bold'))
    canvas1.create_window(150,80, window=Ans)
  
    
button1 = tk.Button(text='ISBN for SAP', command=isbn)
canvas1.create_window(70, 80, window=button1)


root.mainloop()

