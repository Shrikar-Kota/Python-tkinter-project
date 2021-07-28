from tkinter import *
from mobilesmodified import *
from accessoriesmodified import *
from camerasmodified import *
cart_total1=sum(cart1)+sum(cart2)+sum(cart3)
def electronics1():
    Electronics=Toplevel()
    label1=Label(Electronics,text='Shop by Category in Electronics :',font=('Calibri',20)).grid(row=0,column=1) 
    m1=PhotoImage(file='001-smartphone-call.png')
    m2=PhotoImage(file='003-usb-cable.png')
    m3=PhotoImage(file='002-tripod.png')
    b1=Button(Electronics , image=m1,command=mobiles).grid( row=1 ,column=0)
    b2=Button(Electronics , image=m2,command=accessories).grid( row=1 ,column=1)
    b3=Button(Electronics , image=m3,command=camera).grid( row=1 ,column=2)
    l1=Label(Electronics , text='Mobile Phones',font=('Calibri',15)).grid( row=2 ,column=0)
    l2=Label(Electronics , text='Mobile Phone Accessories',font=('Calibri',15)).grid( row=2 ,column=1)
    l3=Label(Electronics , text='DSLR Cameras',font=('Calibri',15)).grid( row=2 ,column=2)
    def Back():
        Electronics.destroy()
    label=Label(Electronics,text='Click to Go Back to Category',font=('Calibri',16)).grid(row=3,column=0)
    button=Button(Electronics,text='Go Back',bg='Blue',fg='White',font=('Calibri',16),command=Back).grid(row=3,column=1)
    def cart():
        cart_total1=sum(cart1)+sum(cart2)+sum(cart3)
        print(cart_total1)
        Electronics.destroy()
    b=Button(Electronics,text='Add to CART',font=('Calibri',16),command=cart)
    b.grid(row=3,column=2)
    Electronics.geometry('750x600')
    Electronics.attributes('-fullscreen', True)
    Electronics.mainloop()
