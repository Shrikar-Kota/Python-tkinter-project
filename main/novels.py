from tkinter import *
import tkinter.messagebox
cart6=[]
def Novels():
    price=[259,899,700,499]
    def The_Power_of_your_Subconscious_Mind():
        cart6.append(price[0])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    def Wuthering_Heights():
        cart6.append(price[1])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    def Eleven_Hours():
        cart6.append(price[2])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    def Her_Last_Wish():
        cart6.append(price[3])
        tkinter.messagebox.showinfo("Alert Box","Added To CART! Continue Shopping")
    Books=Toplevel()
    Books['bg']='White'
    Books.title('Book Store')
    m1=PhotoImage(file='1.png')
    m2=PhotoImage(file='2.png')
    m3=PhotoImage(file='3.png')
    m4=PhotoImage(file='4.png')
    b1=Label(Books , image=m1).grid( row=0 ,column=0)
    b2=Label(Books , image=m2).grid( row=1 ,column=0)
    b3=Label(Books , image=m3).grid( row=0 ,column=2)
    b4=Label(Books , image=m4).grid( row=1 ,column=2)
    l1=Button(Books , text='The Power of your Subconscious Mind\n by Joseph Murphy\nPrice:259/-\n_______________\nAdd To Cart',font=('Calibri',20),bg='White',command=The_Power_of_your_Subconscious_Mind).grid( row=0 ,column=1)
    l2=Button(Books , text='Wuthering Heights\n by Emily Bronte\nPrice: 899/-\n________________________\nAdd To Cart',font=('Calibri',20),bg='White',command=Wuthering_Heights).grid( row=1 ,column=1)
    l3=Button(Books , text='11 Hours\n by Daniel Paul Singh \nPrice: 700/-\n___________________________\nAdd To Cart',font=('Calibri',20),bg='White',command=Eleven_Hours).grid( row=0 ,column=3)
    l4=Button(Books , text='Her Last Wish()\n by Ajay K. Pandey \nPrice: 499/-\n__________________________\nAdd To Cart',font=('Calibri',20),bg='White',command=Her_Last_Wish).grid( row=1 ,column=3)
    def Back():
        Books.destroy()
    label=Label(Books,text='Click to Go Back to Books Category',font=('Calibri',16),bg='White').grid(row=2,column=0)
    button=Button(Books,text='Go Back',bg='Blue',fg='White',font=('Calibri',16),command=Back).grid(row=2,column=1)
    Books.attributes('-fullscreen', True)
    Books.mainloop()
