from tkinter import *
import tkinter.messagebox
cart4=[]
def refrigerator():
    price=[22999,23390,24990,12740]
    def Whirlpool_240L():
        cart4.append(price[0])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    def Samsung_253L():
        cart4.append(price[1])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    def LG_260L():
        cart4.append(price[2])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    def Whirlpool_190L():
        cart4.append(price[3])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    Refrigerators=Toplevel()
    Refrigerators['bg']='White'
    Refrigerators.title('Refrigerators')
    m1=PhotoImage(file='Whirlpool240.png')
    m2=PhotoImage(file='Samsung253.png')
    m3=PhotoImage(file='LG260.png')
    m4=PhotoImage(file='Whirlpool190.png')
    b1=Label(Refrigerators , image=m1).grid( row=0 ,column=0)
    b2=Label(Refrigerators , image=m2).grid( row=1 ,column=0)
    b3=Label(Refrigerators , image=m3).grid( row=0 ,column=2)
    b4=Label(Refrigerators , image=m4).grid( row=1 ,column=2)
    l1=Button(Refrigerators , text='Whirlpool 240 L\nFrost Free Multi-Door Refrigerator\nPrice:22,999/-\n_______________\nAdd To Cart',font=('Calibri',20),bg='White',command=Whirlpool_240L).grid( row=0 ,column=1)
    l2=Button(Refrigerators , text='Samsung 253 L 4 Star\n Frost Free Double Door Refrigerator\nPrice: 23,390/-\n________________________\nAdd To Cart',font=('Calibri',20),bg='White',command=Samsung_253L).grid( row=1 ,column=1)
    l3=Button(Refrigerators , text='LG 260 L 4 Star \nFrost Free Double Door Refrigerator \nPrice: 24,990/-\n___________________________\nAdd To Cart',font=('Calibri',20),bg='White',command=LG_260L).grid( row=0 ,column=3)
    l4=Button(Refrigerators , text='Whirlpool 190 L 3 Star\n Direct Cool Single Door Refrigerator\nPrice: 12,740/-\n__________________________\nAdd To Cart',font=('Calibri',20),bg='White',command=Whirlpool_190L).grid( row=1 ,column=3)
    def Back():
        Refrigerators.destroy()
    label=Label(Refrigerators,text='Go Back to Appliances Category',font=('Calibri',16),bg='White').grid(row=2,column=0)
    button=Button(Refrigerators,text='Go Back',bg='Blue',fg='White',font=('Calibri',16),command=Back).grid(row=2,column=1)
    Refrigerators.attributes('-fullscreen', True)
    Refrigerators.mainloop()
    
