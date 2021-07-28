from tkinter import *
import tkinter.messagebox
cart5=[]
def washingmachine():
    price=[13299,21199,16299,29490]
    def Samsung_Top():
        cart5.append(price[0])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    def Samsung_Front():
        cart5.append(price[1])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    def IFB_Top():
        cart5.append(price[2])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    def Bosch_Front():
        cart5.append(price[3])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    WashingMachines=Toplevel()
    WashingMachines['bg']='White'
    WashingMachines.title('Washing Machines')
    m1=PhotoImage(file='SamsungTop.png')
    m2=PhotoImage(file='SamsungFront.png')
    m3=PhotoImage(file='IFBTop.png')
    m4=PhotoImage(file='BoschFront.png')
    b1=Label(WashingMachines , image=m1).grid( row=0 ,column=0)
    b2=Label(WashingMachines , image=m2).grid( row=1 ,column=0)
    b3=Label(WashingMachines , image=m3).grid( row=0 ,column=2)
    b4=Label(WashingMachines, image=m4).grid( row=1 ,column=2)
    l1=Button(WashingMachines , text='Samsung 6.2 kg\nFully-Automatic\nTop load Washing Machine\nPrice:13,299.00/-\n_______________\nAdd To Cart',font=('Calibri',20),bg='White',command=Samsung_Top).grid( row=0 ,column=1)
    l2=Button(WashingMachines , text='Samsung 6 kg\nFully-Automatic\nFront Loading Washing Machine\nPrice:  21,199./-\n________________________\nAdd To Cart',font=('Calibri',20),bg='White',command=Samsung_Front).grid( row=1 ,column=1)
    l3=Button(WashingMachines , text='IFB 6.5 kg\nFully-Automatic\nTop Loading Washing Machine\nPrice-16,299/-\n___________________________\nAdd To Cart',font=('Calibri',20),bg='White',command=IFB_Top).grid( row=0 ,column=3)
    l4=Button(WashingMachines , text='Bosch 7 kg\nFully-Automatic\nFront Loading Washing Machine\nPrice:29,490/-\n__________________________\nAdd To Cart',font=('Calibri',20),bg='White',command=Bosch_Front).grid( row=1 ,column=3)
    def Back():
        WashingMachines.destroy()
    label=Label(WashingMachines,text='Go Back to Appliances Category',font=('Calibri',16),bg='White').grid(row=2,column=0)
    button=Button(WashingMachines,text='Go Back',bg='Blue',fg='White',font=('Calibri',16),command=Back).grid(row=2,column=1)
    WashingMachines.attributes('-fullscreen', True)
    WashingMachines.mainloop()
    
    
