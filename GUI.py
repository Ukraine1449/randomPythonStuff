import tkinter
from tkinter import END
import third
import database

tk = tkinter.Tk()
tk.title('PogThing')

listbox = tkinter.Listbox(tk)

listbox.insert(0, 'Hi')
listbox.pack()


def add_to_list():
    name = name_var.get()
    listbox.insert(END, name)


def remove_from_list():
    listbox.delete(listbox.curselection())


def getalll():
    for i in range(0, listbox.size()):
        print(listbox.get(i))


def remove_all():
    for i in range(0, listbox.size()):
        listbox.delete(i)


name_var = tkinter.StringVar()

entry = tkinter.Entry(tk, textvariable=name_var)
entry.pack()

button = tkinter.Button(tk, text='Add Value', command=add_to_list)
buttonn = tkinter.Button(tk, text='Remove_Value', command=remove_from_list)
buttonnn = tkinter.Button(tk, text='Remove all', command=remove_all)
buttonnnn = tkinter.Button(tk, text='Get all', command=getalll)
button.pack()
buttonn.pack()
buttonnn.pack()
buttonnnn.pack()
tk.mainloop()
