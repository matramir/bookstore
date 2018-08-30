from tkinter import *
from backend_oop import Database
"""
Program that stores Title, Author, Year, ISBN

User can View, Search, Add, Update, Delete, close
"""

database = Database("books.db")

def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except:
        pass

def view_all():
    for row in database.view():
        list1.delete(0,END)
        list1.insert(END, row)

def search_entry():
    try:
        list1.delete(0, END)
        for row in database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
            list1.insert(END, row)
    except:
        list1.delete(0, END)
        list.insert(END, ("Search Error",))
def add_entry():
    try:
        database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
        list1.delete(0, END)
        list.insert(END,(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))
    except:
        list1.delete(0, END)
        list.insert(END, "Add Error")
def update_entry():
    try:
        database.update(selected_tuple[0],title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    except:
        list1.delete(0, END)
        list.insert(END, "Update Error")
def delete_data():
    try:
        database.delete(selected_tuple[0])
    except:
        list1.delete(0, END)
        list.insert(END, "Delete Error")

#def close_app():


window = Tk()

window.title("Bookstore")
#labels
lb1 = Label(window,text="Title")
lb2 = Label(window,text="Year")
lb3 = Label(window,text="Author")
lb4 = Label(window,text="ISBN")

#entry values
title_text = StringVar()
year_text = StringVar()
author_text = StringVar()
isbn_text = StringVar()

#entries
e1 = Entry(window, textvariable=title_text)
e2 = Entry(window, textvariable=year_text)
e3 = Entry(window, textvariable=author_text)
e4 = Entry(window, textvariable=isbn_text)

#buttons
b1 = Button(window, width=12, text="View All", command=view_all)
b2 = Button(window, width=12, text="Search Entry", command=search_entry)
b3 = Button(window, width=12, text="Add Entry", command=add_entry)
b4 = Button(window, width=12, text="Update Selected", command=update_entry)
b5 = Button(window, width=12, text="Delete Selected", command=delete_data)
b6 = Button(window, width=12, text="Close",command=window.destroy)

#fist entry column
lb1.grid(row=0, column=0)
e1.grid(row=0, column=1)
lb2.grid(row=1, column=0)
e2.grid(row=1, column=1)
#second entry column
lb3.grid(row=0, column=2)
e3.grid(row=0, column=3)
lb4.grid(row=1, column=2)
e4.grid(row=1, column=3)
#button column
b1.grid(row=2, column=3)
b2.grid(row=3, column=3)
b3.grid(row=4, column=3)
b4.grid(row=5, column=3)
b5.grid(row=6, column=3)
b6.grid(row=7, column=3)

#listbox
list1=Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

#scrollbar
sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

window.mainloop()
