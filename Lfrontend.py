import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os
import Lbackend

def get_selected_row(event):
    global selected_t
    if len(lb.curselection()) > 0:
        index = lb.curselection()[0]            # index of selected row in listbox 
        selected_t = lb.get(index)              # access the whole row based on index 
        print(selected_t[0])



def insert_fun():
    if tit.get()  == "" or auth.get() == "" or year.get() == "" or isbn.get() == "":
        messagebox.showerror("Empty Fields","Please fill all the Fields!")

    #   <-- VALIDATE THE DATA TYPES BEING INSERTED IN TABLE -->
    # 
    # 
    # 
    # 
    #     

    else:
        Lbackend.insert(tit.get().lower(),auth.get().lower(),year.get(),isbn.get())
        lb.insert(END,(tit.get(),auth.get(),year.get(),isbn.get()))

        # empty the Entry field texts
        e1.delete(0,END) , e2.delete(0,END) , e3.delete(0,END) , e4.delete(0,END)
        

def viewall_fun():
    lb.delete(0,END)                        # delete previous data from start to end
    for row in Lbackend.view():             # for every row returned in view()
        lb.insert(END,row)                  # insert row into list box    

def update_fun():
    Lbackend.update(selected_t[0],tit.get().lower(),auth.get().lower(),year.get(),isbn.get())
    lb.delete(0,END)
    for row in Lbackend.view():             
        lb.insert(END,row)   

def delete_fun():
    Lbackend.delete(selected_t[0])
    lb.delete(0,END)
    viewall_fun()
    

def search_fun():
    lb.delete(0,END)

    if Lbackend.search(tit.get().lower(),auth.get().lower(),year.get(),isbn.get()) == 0:
        messagebox.showerror("","NO RESULT FOUND !")
    else:
        for row in Lbackend.search(tit.get().lower(),auth.get().lower(),year.get(),isbn.get()):
            lb.insert(END,row)




window = tk.Tk()

window.wm_title("Library MGMT")

frame = tk.Frame(window, bg="black")
frame.place(relwidth=1,relheight=1)

l1 = tk.Label(window,text='Title',bg="black",fg="white",width=8,padx=5,pady=2)
l1.grid(row=0,column=0)
tit = StringVar()
e1 = tk.Entry(window,textvariable=tit)
e1.grid(row=0,column=1)

l2 = tk.Label(window,text='Author',bg="black",fg="white",width=8,padx=5,pady=2)
l2.grid(row=0,column=2)
auth=StringVar()
e2 = tk.Entry(window,textvariable=auth,width=18)
e2.grid(row=0,column=3)

l3 = tk.Label(window,text='Year',bg="black",fg="white",width=8,padx=5,pady=2)
l3.grid(row=1,column=0)
year = StringVar()
e3 = tk.Entry(window,textvariable=year)
e3.grid(row=1,column=1)

l4 = tk.Label(window,text='ISBN',bg="black",fg="white",width=8,padx=5,pady=2)
l4.grid(row=1,column=2)
isbn = StringVar()
e4 = tk.Entry(window,textvariable=isbn,width=18)
e4.grid(row=1,column=3)


lb = tk.Listbox(window,height=10,width=35)
lb.grid(row=2,column=0,columnspan=2,rowspan=6,padx=5,pady=5)

# when a row is selected(EVENT) , a function will be called 
lb.bind('<<ListboxSelect>>',get_selected_row)

sb = tk.Scrollbar(window)
sb.grid(row=2,column=2,rowspan=6)


lb.configure(yscrollcommand=sb.set)     # bind scrollbar to list box
sb.configure(command=lb.yview)          # on scrollbar change vertical view of list box should change



b1 = tk.Button(window,text='View All',command=viewall_fun,width=15,bg="black",fg="white")
b1.grid(row=2,column=3)

b2 = tk.Button(window,text='insert',command=insert_fun,width=15,bg="black",fg="white")
b2.grid(row=3,column=3)

b3 = tk.Button(window,text='update',command=update_fun,width=15,bg="black",fg="white")
b3.grid(row=4,column=3)

b4 = tk.Button(window,text='delete',command=delete_fun,width=15,bg="black",fg="white")
b4.grid(row=5,column=3)

b5 = tk.Button(window,text='search',command=search_fun,width=15,bg="black",fg="white")
b5.grid(row=6,column=3)

b6 = tk.Button(window,text='close',command=window.destroy,width=15,bg="black",fg="white")
b6.grid(row=7,column=3)

window.mainloop()