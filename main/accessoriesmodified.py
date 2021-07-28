from tkinter import *
import tkinter.messagebox
cart2=[]
def accessories():
    price=[5900,1475,2760,899]
    def samsung_pad():
        cart2.append(price[0])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    def samsung_usb():
        cart2.append(price[1])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    def sony_powerbank():
        cart2.append(price[2])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    def sandisk_drive():
        cart2.append(price[3])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    Electronics=Toplevel()
    Electronics['bg']='White'
    Electronics.title('Mobile Phone Accessories')
    m1=PhotoImage(file='Samsung FastCharge Pad+.png')
    m2=PhotoImage(file='Samsung 2-in-1 USB Cable.png')
    m3=PhotoImage(file='Sony CycleEnergy Power Bank+.png')
    m4=PhotoImage(file='SanDisk Cruzer Blade 64GB.png')
    b1=Label(Electronics , image=m1).grid( row=0 ,column=0)
    b2=Label(Electronics , image=m2).grid( row=1 ,column=0)
    b3=Label(Electronics , image=m3).grid( row=0 ,column=2)
    b4=Label(Electronics , image=m4).grid( row=1 ,column=2)
    l1=Button(Electronics , text='Samsung Fast Charge Pad Black\nPrice:5,900/-\n_____________________________\nAdd To Cart',font=('Calibri',20),bg='White',command=samsung_pad).grid( row=0 ,column=1)
    l2=Button(Electronics , text='Samsung 2-in-1 USB Cable \nPrice: 1,475/-\n________________________\nAdd To Cart',font=('Calibri',20),bg='White',command=samsung_usb).grid( row=1 ,column=1)
    l3=Button(Electronics , text='Sony CycleEnergy Power Bank Black\n20,000mAH \nPrice: 2,760/-\n_________________________________\nAdd To Cart',font=('Calibri',20),bg='White',command=sony_powerbank).grid( row=0 ,column=3)
    l4=Button(Electronics , text='SanDisk Cruzer Blade 64GB Storage\nPrice: 899/-\n_____________________________\nAdd To Cart',font=('Calibri',20),bg='White',command=sandisk_drive).grid( row=1 ,column=3)
    def Back():
        Electronics.destroy()
    label=Label(Electronics,text='Click to Go Back to Electronics Category',font=('Calibri',16),bg='White').grid(row=2,column=0)
    button=Button(Electronics,text='Go Back',bg='Blue',fg='White',font=('Calibri',16),command=Back).grid(row=2,column=1)
    Electronics.attributes('-fullscreen', True)
    Electronics.mainloop()
