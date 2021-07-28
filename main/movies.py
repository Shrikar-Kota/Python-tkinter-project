from tkinter import *
import tkinter.messagebox
cart7=[]
def Movies():
    price=[459,799,900,499]
    def Half_Girlfriend():
        cart7.append(price[0])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    def Percy_Jackson():
        cart7.append(price[1])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    def Harry_Potter():
        cart7.append(price[2])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    def Journey():
        cart7.append(price[3])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    Books=Toplevel()
    Books['bg']='White'
    Books.title('Book Store')
    m1=PhotoImage(file='hgf.png')
    m2=PhotoImage(file='pj.png')
    m3=PhotoImage(file='hp.png')
    m4=PhotoImage(file='j2c.png')
    b1=Label(Books , image=m1).grid( row=0 ,column=0)
    b2=Label(Books , image=m2).grid( row=1 ,column=0)
    b3=Label(Books , image=m3).grid( row=0 ,column=2)
    b4=Label(Books , image=m4).grid( row=1 ,column=2)
    l1=Button(Books , text='Half Girlfriend \n by Chetan Bhagat \nPrice:459/-\n_______________\nAdd To Cart',font=('Calibri',20),bg='White',command=Half_Girlfriend).grid( row=0 ,column=1)
    l2=Button(Books , text='Percy Jackson \n The Lightning Thief  \n by Rick Riordon \nPrice: 799/-\n________________________\nAdd To Cart',font=('Calibri',20),bg='White',command=Percy_Jackson).grid( row=1 ,column=1)
    l3=Button(Books , text='Harry Potter \n Prisoner of Azkaban \n by J.K Rowling \nPrice: 900/-\n___________________________\nAdd To Cart',font=('Calibri',20),bg='White',command=Harry_Potter).grid( row=0 ,column=3)
    l4=Button(Books , text='Journey To The Centre of The Earth \n by Jules Verne \nPrice: 499/-\n__________________________\nAdd To Cart',font=('Calibri',20),bg='White',command=Journey).grid( row=1 ,column=3)
    def Back():
        Books.destroy()
    label=Label(Books,text='Click to Go Back to Books Category',font=('Calibri',16),bg='White').grid(row=2,column=0)
    button=Button(Books,text='Go Back',bg='Blue',fg='White',font=('Calibri',16),command=Back).grid(row=2,column=1)
    Books.attributes('-fullscreen', True)
    Books.mainloop()
