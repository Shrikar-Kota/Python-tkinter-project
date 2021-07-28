from tkinter import *
import tkinter.messagebox
cart3=[]
def camera():
    
    price=[25220,20560,27560,42599]
    
    def canon_77d():
        cart3.append(price[0])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    def canon_1300d():
        cart3.append(price[1])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    def nikon_d7200():
        cart3.append(price[2])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    def nikon_d5300():
        cart3.append(price[3])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    Electronics=Toplevel()
    Electronics['bg']='White'
    Electronics.title('DSLR Cameras')
    m1=PhotoImage(file='Canon EOS 77D 24mp.png')
    m2=PhotoImage(file='Canon EOS 1300D 18.png')
    m3=PhotoImage(file='Nikon D7200 24.2MP .png')
    m4=PhotoImage(file='Nikon D5300 27.2MP DSLR Camera.png')
    b1=Label(Electronics , image=m1).grid( row=0 ,column=0)
    b2=Label(Electronics , image=m2).grid( row=1 ,column=0)
    b3=Label(Electronics , image=m3).grid( row=0 ,column=2)
    b4=Label(Electronics , image=m4).grid( row=1 ,column=2)
    l1=Button(Electronics , text='Canon EOS 77D \n24MP DSLR Camera\nPrice:25,220/-\n______________\nAdd To Cart',font=('Calibri',20),bg='White',command=canon_77d).grid( row=0 ,column=1)
    l2=Button(Electronics , text='Canon EOS 1300D \n18MP DSLR Camera \nPrice: 20,560/-\n________________\nAdd To Cart',font=('Calibri',20),bg='White',command=canon_1300d).grid( row=1 ,column=1)
    l3=Button(Electronics , text='Nikon D7200 \n24.2MP DSLR Camera \nPrice: 27,560/-\n____________\nAdd To Cart',font=('Calibri',20),bg='White',command=nikon_d7200).grid( row=0 ,column=3)
    l4=Button(Electronics , text='Nikon D5300 \n27.2MP DSLR Camera \nPrice: 42,599/-\n____________\nAdd To Cart',font=('Calibri',20),bg='White',command=nikon_d5300).grid( row=1 ,column=3)
    def Back():
        Electronics.destroy()
    def Checkout():
        print(sum(cart3))
        Electronics.destroy()
    label=Label(Electronics,text='Click to Go Back to Electronics Category',font=('Calibri',16),bg='White').grid(row=2,column=0)
    button=Button(Electronics,text='Go Back',bg='Blue',fg='White',font=('Calibri',16),command=Back).grid(row=2,column=1)
    #l5=Button(Electronics , text='CheckOut',font=('Calibri',16),command=Checkout).grid(row=2,column=2)
    Electronics.attributes('-fullscreen', True)
    Electronics.mainloop()
