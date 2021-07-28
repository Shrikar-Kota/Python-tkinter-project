from tkinter import *
from novels import *
from movies import *
cart_total4=sum(cart6)+sum(cart7)
def Books1():
    Books=Toplevel()
    label1=Label(Books,text='Shop by Genre in Books :',font=('Calibri',20)).grid(row=0,column=1) 
    m1=PhotoImage(file='book2.png')
    m2=PhotoImage(file='book1.png')
    b1=Button(Books , image=m1,command=Novels).grid( row=1 ,column=0)
    b2=Button(Books , image=m2,command=Movies).grid( row=1 ,column=1)
    l1=Label(Books , text='Fiction Novels',font=('Calibri',15)).grid( row=2 ,column=0)
    l2=Label(Books , text='Movies',font=('Calibri',15)).grid( row=2 ,column=1)
    def Back():
        Books.destroy()
    label=Label(Books,text='Click to Go Back to Category',font=('Calibri',16)).grid(row=3,column=0)
    button=Button(Books,text='Go Back',bg='Blue',fg='White',font=('Calibri',16),command=Back).grid(row=3,column=1)
    def cart():
        cart_total4=sum(cart6)+sum(cart7)
        print(cart_total4)
        Books.destroy()
    b=Button(Books,text='Add to CART',font=('Calibri',16),command=cart)
    b.grid(row=3,column=2)
    Books.geometry('750x600')
    Books.attributes('-fullscreen', True)
    Books.mainloop()

