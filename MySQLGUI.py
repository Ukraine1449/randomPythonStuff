import tkinter
import database
from tkinter import END

tk = tkinter.Tk()
tk.title('MySQL Requests')
listbox = tkinter.Listbox(tk)
listbox.pack(side="left", fill="both", expand=True)
for i in database.getall():
    listbox.insert(END, i)
tk.geometry("500x200")

entry1 = tkinter.Entry()
entry1.pack()
entry2 = tkinter.Entry()
entry2.pack()
entry3 = tkinter.Entry()
entry3.pack()
var = tkinter.StringVar()


def addbook():
    title = entry1.get()
    author = entry2.get()
    pages = entry3.get()
    database.add(title, author, pages)
    label = tkinter.Label(tk, textvariable=var)
    var.set("Success")
    label.pack()


button = tkinter.Button(tk, text='Add Value', command=addbook)
button.pack()
tk.mainloop()
