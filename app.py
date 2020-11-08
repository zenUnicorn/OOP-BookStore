from tkinter import *
from  engine import Database

#create and instance of the Database class
database=Database("books.db")

#getting the index of all the data in the db using event listener
def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    # print(selected_tuple)
    #return(selected_tuple)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])

#Add the data into the list box by pressing viewall button
def view_command():
    list1.delete(0,END) #clears all data and avoids duplicating
    for row in database.view():
        list1.insert(END,row)

#Searching for inputs sent by the user in the entry widgets, and getting the texts as a string
def search_command():
    list1.delete(0,END)
    for row in database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END,row)

#Adding data
def add_command():
    database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()) #add enrty to db
    list1.delete(0,END) #clears the list box
    list1.insert(END,(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())) #Adds the new entry to the end of the list inside the lisbox
    
def delete_command():
    database.delete(selected_tuple[0])

def update_command():
    database.update(selected_tuple[0],title_text.get(), author_text.get(), year_text.get(), isbn_text.get())





window = Tk()

window.wm_title("Book-Store Version 1.0.0")

l1 = Label(window,text="Title")
l1.grid(row=0, column=0)

l1 = Label(window,text="Author")
l1.grid(row=0, column=2)

l1 = Label(window,text="Year")
l1.grid(row=1, column=0)

l1 = Label(window,text="ISBN")
l1.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

#adding scrollbar
sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

#binding an event to the list, button up
list1.bind('<<ListboxSelect>>', get_selected_row) #takes event type and takes the function you want to bind to the event type


b1 = Button(window, text="View all", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add entry", width=12, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update Selected", width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete selected", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
