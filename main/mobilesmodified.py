from tkinter import *
import tkinter.messagebox
cart1=[]
def mobiles():
    price=[100990,39560,91560,24599]
    def apple():
        cart1.append(price[0])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    def oneplus():
        cart1.append(price[1])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    def samsung_s10():
        cart1.append(price[2])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    def samsung_a50():
        cart1.append(price[3])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    Electronics=Toplevel()
    Electronics['bg']='White'
    Electronics.title('Mobile Phones')
    m1=PhotoImage(file='Apple iPhone XS 256GB.png')
    m2=PhotoImage(file='OnePlus 6T .png')
    m3=PhotoImage(file='Samsung Galaxy S10+.png')
    m4=PhotoImage(file='Samsung Galaxy A50+.png')
    b1=Label(Electronics , image=m1).grid( row=0 ,column=0)
    b2=Label(Electronics , image=m2).grid( row=1 ,column=0)
    b3=Label(Electronics , image=m3).grid( row=0 ,column=2)
    b4=Label(Electronics , image=m4).grid( row=1 ,column=2)
    l1=Button(Electronics , text='Apple iPhone XS\n 256GB Storage\nPrice:100,990/-\n_______________\nAdd To Cart',font=('Calibri',20),bg='White',command=apple).grid( row=0 ,column=1)
    l2=Button(Electronics , text='OnePlus 6T Black 6GB RAM\n 128GB Storage \nPrice: 39,560/-\n________________________\nAdd To Cart',font=('Calibri',20),bg='White',command=oneplus).grid( row=1 ,column=1)
    l3=Button(Electronics , text='Samsung Galaxy S10+ 8GB RAM\n 512GB Storage \nPrice: 91,560/-\n___________________________\nAdd To Cart',font=('Calibri',20),bg='White',command=samsung_s10).grid( row=0 ,column=3)
    l4=Button(Electronics , text='Samsung Galaxy A50 4GB RAM\n 64GB Storage \nPrice: 24,599/-\n__________________________\nAdd To Cart',font=('Calibri',20),bg='White',command=samsung_a50).grid( row=1 ,column=3)
    def Back():
        Electronics.destroy()
    def Checkout():
        print(sum(cart1))
        Electronics.destroy()
    label=Label(Electronics,text='Click to Go Back to Electronics Category',font=('Calibri',16),bg='White').grid(row=2,column=0)
    button=Button(Electronics,text='Go Back',bg='Blue',fg='White',font=('Calibri',16),command=Back).grid(row=2,column=1)
    #l5=Button(Electronics , text='CheckOut',font=('Calibri',16),command=Checkout).grid(row=2,column=2)
    Electronics.attributes('-fullscreen', True)
    Electronics.mainloop()
