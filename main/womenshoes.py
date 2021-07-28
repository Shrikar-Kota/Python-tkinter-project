from tkinter import *
import tkinter.messagebox
cart13=[]
def womenshoes():
    womenshoes=Toplevel()
    womenshoes.title('Women Shoes')
    womenshoes['bg']='White'
    price=[3699,2999,1999,1850]
    def Adidas():
        cart13.append(price[0])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    def LeeCooper():
        cart13.append(price[1])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    def HushPuppies():
        cart13.append(price[2])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    def RedTape():
        cart13.append(price[3])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    mi1=PhotoImage(file='wshu1.png')
    mi2=PhotoImage(file='wshu2.png')
    mi3=PhotoImage(file='wshu3.png')
    mi4=PhotoImage(file='wshu4.png')
    l1=Label(womenshoes, image=mi1).grid(row=0,column=0)
    l2=Label(womenshoes, image=mi2).grid(row=2,column=0)
    l3=Label(womenshoes, image=mi3).grid(row=0,column=2)
    l4=Label(womenshoes, image=mi4).grid(row=2,column=2)
    b1=Button(womenshoes, text='Adidas\nColour: White\nPrice: Rs.3699\n____________________\nAdd to Cart',command=Adidas,font='20').grid(row=0,column=1)
    b2=Button(womenshoes, text='LeeCooper\nColour: Dark Blue\nPrice: Rs.2999\n____________________\nAdd to Cart',command=LeeCooper,font='20').grid(row=2,column=1)
    b3=Button(womenshoes, text='HushPuppies\nColour: Silver\nPrice: Rs.1999\n____________________\nAdd to Cart',command=HushPuppies,font='20').grid(row=0,column=3)
    b4=Button(womenshoes, text='RedTape\nColour: Brown\nPrice: Rs.1850\n____________________\nAdd to Cart',command=RedTape,font='20').grid(row=2,column=3)
    def Back():
        womenshoes.destroy()
    label=Label(womenshoes,text='Go Back to Clothing Category',font=('Calibri',16),bg='White').grid(row=4,column=0)
    button=Button(womenshoes,text='Go Back',bg='Blue',fg='White',font=('Calibri',16),command=Back).grid(row=4,column=2)
    womenshoes.attributes('-fullscreen',True)
    womenshoes.mainloop()


