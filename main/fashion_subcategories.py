from tkinter import *
from menclothes import *
from womenclothes import * 
from menshoes import *
from womenshoes import *
cart_total3=sum(cart10)+sum(cart11)+sum(cart12)+sum(cart13)
def fashion1():
    fashion=Toplevel()
    l1=Label(fashion, text='MEN FASHION',font='75').grid(row=0,column=0,columnspan=2)
    l2=Label(fashion, text='WOMEN FASHION',font='75').grid(row=0,column=2,columnspan=2)
    i1=PhotoImage(file='ms.png')
    i2=PhotoImage(file='mshu3.png')
    i3=PhotoImage(file='ws.png')
    i4=PhotoImage(file='wshu1.png')
    b1=Button(fashion, image=i1,command=menclothes).grid(row=1,column=0)
    b2=Button(fashion, image=i2,command=menshoes).grid(row=1,column=1)
    b3=Button(fashion, image=i3,command=womenclothes).grid(row=1,column=2)
    b4=Button(fashion, image=i4,command=womenshoes).grid(row=1,column=3)
    l3=Label(fashion, text='Men Clothing',font='20').grid(row=2,column=0)
    l4=Label(fashion, text='Men Shoes',font='20').grid(row=2,column=1)
    l5=Label(fashion, text='Women Clothing',font='20').grid(row=2,column=2)
    l6=Label(fashion, text='Women Shoes',font='20').grid(row=2,column=3)
    def exit1():
        fashion.destroy()
    def cart():
        cart_total3=sum(cart10)+sum(cart11)+sum(cart12)+sum(cart13)
        print(cart_total3)
        fashion.destroy()
    label=Label(fashion,text='Click to Go Back to Categories',font='16').grid(row=3,column=0)
    button=Button(fashion,text='Go Back',bg='Blue',fg='White',font='16',command=exit1).grid(row=3,column=1)
    button=Button(fashion,text='Add to CART',font='18',command=cart).grid(row=3,column=2)
    fashion.attributes('-fullscreen',True)
    fashion.mainloop()
