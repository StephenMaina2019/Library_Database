#import everything
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
import datetime

#create object window
window=Tk()
window.geometry("400x375+0+0")                                     
window.configure(bg="cadet blue")


# messagebox.showinfo("Message title", "Message content")

def message():
    messagebox.showinfo("My Crush", "I think I can win her over. Wish me luck!")


today = datetime.datetime.now()
str(today)

def time():
    for i in today:
        e5.delete(0, END)
        e5.insert(END, i)

#defining labels
l1 = Label(window, text="Title")
l1.grid(row=0, column=0)
l1.configure(bg="cadet blue")

l2 = Label(window, text="Year")
l2.grid(row=1, column=0)
l2.configure(bg="cadet blue")

l3 = Label(window, text="Author")
l3.grid(row=0, column=2)
l3.configure(bg="cadet blue")

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)
l4.configure(bg="cadet blue")

l5 = Label(window, text="Time")
l5.grid(row=2, column=0)
l5.configure(bg="cadet blue")
#defining entries
title_text=StringVar()
e1= Entry(window, width=15, textvariable = title_text)
e1.grid(row=0, column=1)

combo = Combobox(window)
combo['values'] = (2001, 2002, 2003, 2004)
combo.current(0)
combo.grid(row=1, column=1)
# year_text=StringVar()
# e2= Entry(window, textvariable = year_text)
# e2.grid(row=1, column=1)

Author_text=StringVar()
e3= Entry(window, textvariable = Author_text)
e3.grid(row=0, column=3)

ISBN_text=StringVar()
e4= Entry(window, textvariable = ISBN_text)
e4.grid(row=1, column=3)

e5 = Entry(window)
e5.grid(row=2, column=1)

#define Listbox
list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

#attach scrollbar to the list
sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

#Define Buttons
b1 = Button(window, text="View All", width=12)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search Entry", width=12)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add Entry", width=12)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update Selected", width=12)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete Selected", width=12, command=message)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=quit)
b6.grid(row=7, column=3)

bb6 = Button(window, text="Show Current Time", width=15, command=time)
bb6.grid(row=7, column=3)

window.mainloop()