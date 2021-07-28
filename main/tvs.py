from tkinter import *
import tkinter.messagebox
cart14=[]
def tv():   
    price=[313400,499990,329900,109900]    
    def samsung_curve():
        cart14.append(price[0])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    def lg():
        cart14.append(price[1])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    def sony():
        cart14.append(price[2])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    def samsung_hd():
        cart14.append(price[3])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    Electronics=Toplevel()
    Electronics['bg']='White'
    Electronics.title('Televisions')
    m1=PhotoImage(file='sc.png')
    m2=PhotoImage(file='lgo.png')
    m3=PhotoImage(file='sony4k.png')
    m4=PhotoImage(file='samsung.png')
    b1=Label(Electronics , image=m1).grid( row=0 ,column=0)
    b2=Label(Electronics , image=m2).grid( row=1 ,column=0)
    b3=Label(Electronics , image=m3).grid( row=0 ,column=2)
    b4=Label(Electronics , image=m4).grid( row=1 ,column=2)
    l1=Button(Electronics , text='Samsung 65" Curved TV \nPrice:3,13,400/-\n______________\nAdd To Cart',font=('Calibri',16),bg='White',command=samsung_curve).grid( row=0 ,column=1)
    l2=Button(Electronics , text='LG 65" OLED TV  \nPrice: 4,99,990/-\n________________\nAdd To Cart',font=('Calibri',16),bg='White',command=lg).grid( row=1 ,column=1)
    l3=Button(Electronics , text='SONY A8F 4K ULTRA HD TV \nPrice: 3,29,900/-\n____________\nAdd To Cart',font=('Calibri',16),bg='White',command=sony).grid( row=0 ,column=3)
    l4=Button(Electronics , text='Samsung 55" 4K UHF TV  \nPrice: 1,09,900/-\n____________\nAdd To Cart',font=('Calibri',16),bg='White',command=samsung_hd).grid( row=1 ,column=3)
    def Back():
        Electronics.destroy()
    def Checkout():
        print(sum(cart3))
        Electronics.destroy()
    label=Label(Electronics,text='Click to Go Back to Electronics Category',font=('Calibri',16),bg='White').grid(row=2,column=0)
    button=Button(Electronics,text='Go Back',bg='Blue',fg='White',font=('Calibri',16),command=Back).grid(row=2,column=1)
    Electronics.attributes('-fullscreen', True)
    Electronics.mainloop()
