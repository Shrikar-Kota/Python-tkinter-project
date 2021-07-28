from tkinter import *
from washingmodified import *
from refrigeratorsmodified import *
from tvs import *
cart_total2=sum(cart4)+sum(cart5)+sum(cart14)
def appliances1():
    Appliances=Toplevel()
    label1=Label(Appliances,text='Shop by Category in Appliances :',font=('Calibri',20)).grid(row=0,column=1) 
    m1=PhotoImage(file='washing-machine.png')
    m2=PhotoImage(file='fridge.png')
    m3=PhotoImage(file='tv.png')
    b1=Button(Appliances , image=m1,command=washingmachine).grid( row=1 ,column=0)
    b2=Button(Appliances , image=m2,command=refrigerator).grid( row=1 ,column=1)
    b3=Button(Appliances , image=m3,command=tv).grid( row=1 ,column=2)
    l1=Label(Appliances , text='Washing Machines',font=('Calibri',15)).grid( row=2 ,column=0)
    l2=Label(Appliances , text='Refrigerators',font=('Calibri',15)).grid( row=2 ,column=1)
    l3=Label(Appliances , text='Televisions',font=('Calibri',15)).grid( row=2 ,column=2)
    def Back():
        Appliances.destroy()
    label=Label(Appliances,text='Click to Go Back to Category',font=('Calibri',16)).grid(row=3,column=0)
    button=Button(Appliances,text='Go Back',bg='Blue',fg='White',font=('Calibri',16),command=Back).grid(row=3,column=1)
    def cart():
        cart_total2=sum(cart4)+sum(cart5)
        print(cart_total2)
        Appliances.destroy()
    b=Button(Appliances,text='Add to CART',font=('Calibri',16),command=cart)
    b.grid(row=3,column=2)
    Appliances.geometry('750x600')
    Appliances.attributes('-fullscreen', True)
    Appliances.mainloop()

