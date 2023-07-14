
#tkinter image

from tkinter import *
from tkinter import ttk
root = Tk()
goldmember = PhotoImage(file = 'C:\\Users\\jasmi\\OneDrive\Desktop\\Developer tools\\goldmember.jpg')
label = ttk.label(root, image = goldmember)
PhotoImage(file = 'C:\\Users\\jasmi\\OneDrive\Desktop\\Developer tools\\goldmember.jpg')
label.pack()
