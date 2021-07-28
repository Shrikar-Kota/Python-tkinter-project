from tkinter import *
import tkinter.messagebox
cart12=[]
def menshoes():
    menshoes=Toplevel()
    menshoes.title('Men Shoes')
    menshoes['bg']='White'
    price=[4999,3499,2000,2499]
    def Puma():
        cart12.append(price[0])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    def Reebok():
        cart12.append(price[1])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    def Fila():
        cart12.append(price[2])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    def Crocs():
        cart12.append(price[3])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    mi1=PhotoImage(file='mshu1.png')
    mi2=PhotoImage(file='mshu2.png')
    mi3=PhotoImage(file='mshu3.png')
    mi4=PhotoImage(file='mshu4.png')
    l1=Label(menshoes, image=mi1).grid(row=0,column=0)
    l2=Label(menshoes, image=mi2).grid(row=2,column=0)
    l3=Label(menshoes, image=mi3).grid(row=0,column=2)
    l4=Label(menshoes, image=mi4).grid(row=2,column=2)
    b1=Button(menshoes, text='Puma\nColour: Black\nPrice: Rs.4999\n____________________\nAdd to Cart',command=Puma,font='20').grid(row=0,column=1)
    b2=Button(menshoes, text='Reebok\nColour: Brown\nPrice: Rs.3499\n____________________\nAdd to Cart',command=Reebok,font='20').grid(row=2,column=1)
    b3=Button(menshoes, text='Fila\nColour: Dark Blue\nPrice: Rs.2000\n____________________\nAdd to Cart',command=Fila,font='20').grid(row=0,column=3)
    b4=Button(menshoes, text='Crocs\nColour: Blue\nPrice: Rs.2499\n____________________\nAdd to Cart',command=Crocs,font='20').grid(row=2,column=3)
    def Back():
        menshoes.destroy()
    label=Label(menshoes,text='Go Back to Clothing Category',font=('Calibri',16),bg='White').grid(row=4,column=0)
    button=Button(menshoes,text='Go Back',bg='Blue',fg='White',font=('Calibri',16),command=Back).grid(row=4,column=2)
    menshoes.attributes('-fullscreen',True)
    menshoes.mainloop()

